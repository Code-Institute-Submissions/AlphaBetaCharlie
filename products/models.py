from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
# Create your models here.



class ProductBase(models.Model):

    """Model representing base for all products - currently 3 - Alpha, Beta, Charlie, create those in Database via admin"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class ProductTypeManager(models.Manager):

    def get_user_alphas(self, user_id, exclusion_value_list):
        consumed_alpha_price_list = []
        for alpha in consumed_alpha_list:
            consumed_alpha_price_list.append(alpha.type.price)
        return ProductType.objects.filter(base__name='alpha').exclude(price__in=consumed_alpha_price_list)

class ProductType(models.Model):

    """Model representing type of a product - currently alpha, beta, charlie"""
    base = models.ForeignKey('ProductBase', on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_available = models.ImageField(upload_to='images', blank=True)
    image_consumed = models.ImageField(upload_to='images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = ProductTypeManager()

    def __str__(self):
        """String for representing the Model object."""
        return self.name



class ProductManager(models.Manager):

    def create_consumed_alpha(self, product, consumed_by_id):
        print('Creating consumed alpha')
        type = ProductType.objects.get(pk=product.id)
        consumed_by = get_user_model().objects.get(pk=consumed_by_id)
        alpha_new = self.create(type=type, status='consumed', consumed_by=consumed_by)
        # do something with the book
        return alpha_new

    def create_all_available_children(self, parent, created_by_id):
        #fetch all children available for that particular value, except alphas. eg. for 1$ get all children = 1$ alpha, 1$ beta, 1$ charlie. now exclude alpha
        children_list = ProductType.objects.filter(price=parent.type.price).exclude(base__name='alpha')
        created_by = get_user_model().objects.get(pk=created_by_id)
        for child in children_list:
            print(child)
            new_product = self.create(type=child, status='available', parent=parent, created_by=created_by)

        return True

    def consume(self, product, consumed_by_id):
        product.status='consumed'
        consumed_by = get_user_model().objects.get(pk=consumed_by_id)
        product.consumed_by = consumed_by
        product.save()
        return product


class Product(models.Model):

    PRODUCT_STATUS = (
        ('available', 'Available'),
        ('held', 'Held'),
        ('consumed', 'Consumed'),
    )

    type = models.ForeignKey('ProductType', blank=True, on_delete=models.DO_NOTHING, null=True)
    parent = models.ForeignKey('self', related_name='product', on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(
        choices=PRODUCT_STATUS,
        blank=True,
        default='available',
        help_text='Product Status',
        max_length=15
    )
    created_by = models.ForeignKey( get_user_model(), related_name="user_created_by", on_delete=models.DO_NOTHING, null=True, )
    consumed_by = models.ForeignKey( get_user_model(), related_name="user_consumed_by", on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = ProductManager()

    def __str__(self):
        return self.type.name + ', id = '+ str(self.id)


