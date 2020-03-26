 Status](https://travis-ci.org/Jmcclain0129/ecommerce.svg?branch=master)](https://travis-ci.org/Jmcclain0129/ecommerce)

# Welcome To The Alpha Beta Charlie eCommerce Platform

## An Introduction

Alpha Beta Charlie is the worlds first eCommerce solution dedicated to selling absolutely nothing.

Users of this site buy and sell virtual items known as Beta and Charlie Transactions. These are not physical items nor are they available for digital download.

Once a buyer successfully completes the purchase of a Beta or Charlie Transaction the owenrship of the originally purchased Beta or Charlie Transaction is voided and that original Transaction is archived. Two new Transactions replace the original Transaction with ownership of these Transactions belonging to the buyer of the original Transaction that is now deprecated.

To accomplish this the site uses its cart system to generate new inventory for sellers once they successfully complete a transaction as a buyer through the checkout process.

Once the buyer successfully completes a transaction purchase on the site that buyer becomes the seller.

## Roles

The Buyer 
The Seller
The Supplier

In this system the buyer is the seller and the seller is the buyer. Both must consume items to spawn inventory they can turn-a-round and sell.

The system supplies all the inventory to the buyers and the sellers which means the system is the Supplier. There is no mechanism to populate a store in this system with items other than the process of store owners consuming other store owners items. Each time a store owner consumes an item two new items are generated and placed in that store owners inventory and put up for sale automatically through the marketplace.

## Transaction types

This system has three items affectionately known as Alpha, Beta and Charlie Transactions. These items are available in various sizes with a specific value assigned to each one. Currently the items values are based on the various paper money denominations of the USD Fiat currency otherwise known as the US dollar. 

$1
$5
$10
$20
$50
$100

These three transaction types are the only commodities for sale on this platform. They exist in name only because they are not tangible items, they are virtual items or Fiat transactions.

Revenue is earned by trading in these commodities through the site.

Alpha transactions are used to generate income for the site owner.
Beta and Charlie transactions are used to generate revenue for sellers.

## Inventory Procurement and Managment

As with any other online marketplace its sellers must have inventory to offer for sale to the buyers. This marketplace is no different. What makes this platform unique is the method with which inventory is acquired and managed.

Inventory management is automated by the system. The sellers inventory is depleted as it is consumed by others which increases the inventory of those who are consuming it. To increase inventory sellers must consume items. To decrease inventory sellers simply stop consuming items.

For users to acquire their first inventory items they must consume Alpha Transactions. This process is known as initiating their Alpha.

Once an Alpha is initiated the user can buy and sell Beta and Charlie transaction of equal value from the marketplace. For example, if a user wishes to sell $5 Beta or $5 Charlie Transactions they must first initiate their $5 Alpha. This action spawns their first $5 Beta and $5 Charlie transactions which are placed in the martplace for sale on thier behalf.

When a transaction is consumed the system spawns two new inventory items for the user that spawned them. Before a user can consume any transactions they must initiate the Alpha transaction equal to the value of the transaction they wish to consume.

To acquire more inventory a user must consume Beta and Charlie transactions.

## Foreign Keys

The system uses foreign keys to keep track of transactions. Attributes related to a transaction include the following

Transaction Type: Identifies whether transaction is an ALpha, Beta or Charlie and what denominations it is associated with

Parent Transaction: Identifies where the transaction originated from.

Status: Available, Held or Consumed must be one or the other but not a combination of any.

Created by: Name of user who consumed the parent of the item
Consumed by: Name of user who consumed th eitem

## Selling Items and Tracking Transactions

To get these items a seller must consume another sellers Beta or Charlie item. Once they do and successfully complete the checkout process the consumed Beta or Charlie transaction item is archived and a new Beta and Charlie transaction is spawned. These new items are associated with the buyers account and when they are consumed by another user the account they are associated with is credited with the value of the transaction.

This site generates new inventory items for its users each time an item is purchased by another user. This process is known as consuming items and is necessary for the sellers to stock their store with items to sell.

## Accessing Site Assets

Live site is hosted on:
[Heroku Pages](https://alpha-beta-charlie.herokuapp.com/)

The Repository is located at:
[GitHub](https://github.com/Jmcclain0129/AlphaBetaCharlie/)

## License

This project is not open source therefore the use or distribution of the software contained within it is explicitedly forbidden without written consent from the copyright holder.

If a repository has no license, then all rights are reserved and it is not Open Source or Free. You cannot modify or redistribute this code without explicit permission from the copyright holder.

From GitHub's licensing help page:

"You're under no obligation to choose a license. However, without a license, the default copyright laws apply, meaning that you retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work. If you're creating an open source project, we strongly encourage you to include an open source license. The Open Source Guide provides additional guidance on choosing the correct license for your project.

Note: If you publish your source code in a public repository on GitHub, according to the Terms of Service, other GitHub users have the right to view and fork your repository within the GitHub site. If you have already created a public repository and no longer want users to have access to it, you can make your repository private. When you convert a public repository to a private repository, existing forks or local copies created by other users will still exist."

In short, the only thing you can safely assume is that you have no rights to do anything at all with this code. In the particular case of GitHub, you can fork the repository and view the code, but nothing more.
    
## UX

![Mobile index page](/media/mobile-index.png)

![Mobile inner page](/media/mobile-inner-page.png)

### Users 
The site is open to any and all users from all walks of life. It is anticipated that the site would be most attractive to students age 14 to 24 years as they would most likely be the demographic looking for passive income to support their lifestyles.

The hope is that the student will quickly spread the word amongst their peers and that the site will instantly go viral. If it proves itself useful at generating free money by selling nothing we anticipate these students will be more than willing to share their experiences on the site especially considering the more users on the site the more everyone makes.

### User Stories
1. A new user, alpha_john, is a first year college student from San Diego, California. He has managed to spawn 48 new Beta's and 40 new Charlie's in the first 24 hours since initiating his Alpha. This netted the user $140.00 with the potential to earn another $56 if others transact with his remaining Beta and Charlie transactions that are still floating around the marketplace. The excitement is to much to keep contained so he contacts his mother and tells her about the site. She shares this info with her husband and their daughter who is a final year of high school. All three decide to join the community. ALl three also mention the site to friends and colleagues in passing throughout the day. The result of John's success has seen the sites San Diego membership increase by 37 new members the same day alpha_john shared the news with his family.
2. Following on from the story about alpha_john's success... The 37 new members the site gained in the San Diego area presumably as a result of alpha_john sharing his success with his family and them spreading the word. The system has seen 467 new members join in the Southern California region within 2 days of alpha_john sharing his story.
3. Karen, a homemaker in London stumbled across a a friends facebook post who is a society member. The post mentioned how easy it was to earn extra income using the sites gaming engine so she decided to give it a go. She became a member and within 10 minutes had already earned £7 and had the possibility of earning another £3. She was so delighted she posted her results on her facebook page where she has 462 friends. We're hoping those a good portion of those friends see her post and take the time to become members themselves.

### Design
Website Logo - Text Based

- Colour scheme consists exclusively through Bootstrap colour schema
  -  Navbar:
     ![#1995dc](https://placehold.it/15/1995dc/000000?text=+) `#1995dc`
  -  Buttons:
     ![#26a69a](https://placehold.it/15/73a839/000000?text=+) `#73a839`
  -  Font P:
     ![#555555](https://placehold.it/15/555555/000000?text=+) `#555555`
  -  Font H3:
     ![#317eac](https://placehold.it/15/317eac/000000?text=+) `#317eac`
  -  Footer:
     ![#999999](https://placehold.it/15/999999/000000?text=+) `#999999`
  -  Background:
     ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff`

- fonts used throughout the website
    - Helvetica Neue, Helvetica, Arial

### Mockups
The web app is a multi page with different displays given for different
functions:
- [Admins - add/edit/delete - admin](https://alpha-beta-charlie.herokuapp.com/admin/)
- [Admins - add/edit/delete - orders](https://alpha-beta-charlie.herokuapp.com/admin/checkout/order/)
- [Admins - add/edit/delete - users](https://alpha-beta-charlie.herokuapp.com/admin/auth/user/)
- [Admins - add/edit/delete - products](https://alpha-beta-charlie.herokuapp.com/admin/products/product/)
- [Members View Index](https://alpha-beta-charlie.herokuapp.com)
- [Members View Society Page](https://alpha-beta-charlie.herokuapp.com/accounts/home/)
- [Members View Registration](https://alpha-beta-charlie.herokuapp.com/accounts/register/)
- [Members View Checkout](https://alpha-beta-charlie.herokuapp.com/accounts/checkout/)
- [Members View Cart](https://alpha-beta-charlie.herokuapp.com/cart/)

### Balsamiq Mockups
- https://www.evernote.com/l/APAwU_6IjmRNZqlfNAflYVVwiREnz19uhpE/

## Features

Features planned, implemented and outlined for later development

### Planned Features
- Documentation - ReadMe File, Licence & Mockups
- Django upgrade Python focused development
- Data input from forms
- Page refreshes
- Breadcrumbs - Pending
- Colour Scheme
- Custom Logo - Pending
- Favicon - Pending
- Materialize - HTML, CSS Framework Grid System - Columns and Rows
    - Cards
    - Icons
    - Buttons
    - Image Carousel
    - Collapsible Table
    - Popout Cells
- Responsive design - Mobile First
- UX elements
    - User Flow
    - Animations
    - Transitions
- Accesibility
- Git - Version Control System
- GitHub - Remote Repository
- Deployed - Hosted on Heroku Pages
- 
### Existing Features
- Documentation - ReadMe File, Licence & Mockups
- Django Python focused development
- Data input from forms
- Page refreshes
- Dynamic content switching by house
  -   Alpha
  -   Beta
  -   Charlie
- Colour Scheme
- Materialize - HTML, CSS Framework Grid System - Columns and Rows
    - Cards
    - Icons
    - Buttons
    - Image Carousel
    - Collapsible Table
    - Popout Cells
- Responsive design - Mobile First
- UX elements
    - User Flow
    - Animations
    - Transitions
- Accesibility
- Git - Version Control System
- GitHub - Remote Repository
- Deployed - Hosted on Heroku Pages
- Cloud Database - aws amazon s3 buckets
- 
### Features Left to Implement
- Dynamic content switching by house
  -   Course
  -   Modules
  -   Units
- Pagination
- Breadcrumbs
- Custom Logo
- Favicon
- Search
  - by item type
  - by Alpha, Beta, Charlie
  - by Offered by

## Technologies Used

This project makes use of:
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - HTML for strucutre
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
    - CSS for Styling
- [JavaScript](https://www.w3schools.com/jsref/)
    - **JavaScript** for application controller
- [Google Chrome](https://www.google.com/chrome/)
    - Used for browser and dev tools
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new)
    - Used for browser and dev tools
- [Google](https://www.google.com/)
    - **Google** was used for research.
- [Bootstrap](https://getbootstrap.com/)
    - HTML and CSS Framework from **Bootstrap**
- [Cloud9](https://aws.amazon.com/cloud9/)
- [Git](https://git-scm.com/)
    - **Git** used for Version Control
- [GitHub](https://github.com/)
    - Repository hosted on **GitHub**
- [Heroku](https://decoder-cookbook.herokuapp.com/get_index) Website
  hosted on **Heroku**
- [Django](https://www.djangoproject.com/)
  -   version 1.11.15
- [Am I Responsive](http://ami.responsivedesign.is)
    - Testing responsiveness of the website

## Testing

- [Travis](https://travis-ci.org)

### Testing of this site was done manually using desktop, tablet and mobile devices. Corrections were made to improve responsiveness. More work needs to be done for site to be fully responsive.

1. Tested PC version using google chrome inspect tool
2. Tested Mobile and Tablet versions manually by visiting each page

Alternatively:

1. Visit the hosted version of the
   [website](https://alpha-beta-charlie.herokuapp.com/)

Tests concluded site is fully responsive in mobile displays

To deploy your own version of the website:
- Have git installed
- Visit the [repository]([GitHub](https://github.com/Jmcclain0129/AlphaBetaCharlie))
- Click 'Clone or download' and copy the code for http
- Open your chosen IDE (Cloud9, VS Code, etc.)
- Open a terminal in your root directory
- Type 'git clone ' followed by the code taken from github repository
    - ```git clone https://github.com/Jmcclain0129/AlphaBetaCharlie
- When this completes you have your own version of the website

## Known Bugs

- The site operates as intended

## Credits

to all who provided input via
django-users@googlegroups.com
https://github.community
https//stackoverflow.com

### Content
The text on the website has been written by the web designer:

### Acknowledgements
Thank you to the following for inspiration, motivation and the direction I needed:

- Seun Owonikoko    @seun_mentor
- Simen Daehlin     @Eventyret_mentor
- Michael Park      @michael_ci
- Niel McEwen       @niel_ci
- Naman Gupta       Mentor, coder and friend who provided bug work-a-rounds
- Goran Nikic       Mentor, coder and friend who provided more than one swift kick in the butt as well as a boat load of coffee (usually around 3am)
