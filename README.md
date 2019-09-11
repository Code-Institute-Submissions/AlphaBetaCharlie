[![Build Status](https://travis-ci.org/Jmcclain0129/ecommerce.svg?branch=master)](https://travis-ci.org/Jmcclain0129/ecommerce)

# The Alpha Beta Charlie Society

## Introduction

This Society is a community of individuals seeking financial freedom. To achieve their goal they must work together
culminating friends in the societies gaming platform. 

The platform is not a traditional gaming platform at all. In fact, the platform is a simple ecommerce marketplace where
the buyer becomes the seller and the seller becomes the buyer.

To make matters more confusing, the platform sells absolutely nothing. The site consists of two items known simply as
Beta and Charlie. Beta and Charlie are friendly bots who spend their virtual days looking for more friends. This is
where the gamification of the ecommerce platform comes to light.

The idea was born on the notion that you could not create an ecommerce platform that sold nothing. The sites creator is
a student of Code Institute and the project itself was born out of necessity because the coursework required students to
develop an ecommerce solution as the last in a series of milestone projects. While contemplating ideas for the site the
creator wanted to try something new. Something that was way outside of the box and this is when it dawned on him that
there was no real need to actually use the platform to sell items and/or services. There was nothing in the directive that
specified you had to so the concept quickly started to focus on the possibility of creating a platform that sells
absolutely nothing while at the same time has the potential to earn a substantial amount of wealth for those that engaged
with it.

Once the idea was envisioned the name came immediately. The creator was already fixated on a site name that contained the
word alpha because alpha often represents the first of something and often the best of something. This project was going
to be the creators first, or alpha django project so it made sense to him to want to intern the word alpha into the project
name. Beta was introduced because the project is a beta that will be used as an mvp. Charlie naturally followed because
of the urban alphabet known to the author as alpha beta charlie. Alpha Beta Charlie is a phonetic alphabet used to
spell words over radio transmissions. Alpha for the letter A, Beta for the letter B, Charlie for the letter C and so on.
There is an actual alphabet with a dictionary known as the Nato Phonetic Dictionary which defines the code word and
pronunciation for each of the 26 letters of the english ALPHAbet, non pun intended, lol.

You can view that dictionary here: http://www.alphabravocharlie.info/alphabet.php
Further credit's associated to the origin information related to the NATO dictionary is available on the reference site
listed above.

The idea to create a society built around generating something from nothing through an ecommerce gaming platform wasn't
as easy to imagine as the naming of the project. Originally the concept was to sell Alpha's on the site which would
spawn Beta and Charlie transactions the users could turn-a-round and sell for a profit. But when designing the workflow
for that concept it seemed a bit illogical considering the site was not supposed to be selling anything in the first place.

To solve the issue it was determined that the Alpha transaction could be used to allow the user
to donate a small fee to the society in exchange for a Beta and Charlie set which they could use to find new friends
willing to donate to their cause. This way, the site is not selling anything. There is also another added benefit in that
Alpha is not used to generate Beta and Charlie even though the site cannot spawn a Beta or Charlie unless the user trying
to do the spawning is an Alpha.

## Tracking Transactions

Technically, the user becomes an Alpha once they inaugurate their lifetime membership. Alpha is simply a transaction related
to the form used to accept a donation to the society. Since every member is an Alpha the system will concatenate their username
with the term Alpha so that the system can identify each Alpha user uniquely. The system will concatenate the alpha_username
with each Beta Charlie the Alpha_username is associated with so that each Beta and Charlie assume a unique username as well
such as alpha_username+beta_username+transaction_id# In technical terms this means the system will use foreign keys or
composite keys to track users and their transactions.

To learn more about the Alpha Beta Charlie Society visit the website here:
https://jmc-django-ecommerce.herokuapp.com/accounts/home/


Hosted on 
[Heroku Pages](https://jmc-django-ecommerce.herokuapp.com/)
Repository on
[GitHub](https://github.com/Jmcclain0129/ecommerce)

## License

The project is shared for use with the [GNU General Public License v3](https://github.com/Pattern-Projects/oireachtas-ifd-project/blob/master/LICENSE)

>   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
## UX

![Responsive Views of Index Page](/media/images/mobile_index.PNG)

![Responsive Views of inner page](media/images/mobile_inner_page.PNG)

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
- [Admins - add/edit/delete - admin](https://jmc-django-ecommerce.herokuapp.com/admin/)
- [Admins - add/edit/delete - orders](https://jmc-django-ecommerce.herokuapp.com/admin/checkout/order/)
- [Admins - add/edit/delete - users](https://jmc-django-ecommerce.herokuapp.com/admin/auth/user/)
- [Admins - add/edit/delete - products](https://jmc-django-ecommerce.herokuapp.com/admin/products/product/)
- [Members View Index](https://jmc-django-ecommerce.herokuapp.com)
- [Members View Society Page](https://jmc-django-ecommerce.herokuapp.com/accounts/home/)
- [Members View Registration](https://jmc-django-ecommerce.herokuapp.com/accounts/register/)
- [Members View Checkout](https://jmc-django-ecommerce.herokuapp.com/accounts/checkout/)
- [Members View Cart](https://jmc-django-ecommerce.herokuapp.com/cart/)

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
- Flask Python focused development
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
  - by keyword
  - by Alpha, Beta, Charlie

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
   [website](https://jmc-django-ecommerce.herokuapp.com/)

Tests concluded site is fully responsive in mobile displays

To deploy your own version of the website:
- Have git installed
- Visit the [repository]([GitHub](https://github.com/Jmcclain0129/decoder_cookbook))
- Click 'Clone or download' and copy the code for http
- Open your chosen IDE (Cloud9, VS Code, etc.)
- Open a terminal in your root directory
- Type 'git clone ' followed by the code taken from github repository
    - ```git clone https://github.com/Pattern-Projects/oireachtas-ifd-project.git```
- When this completes you have your own version of the website
    - Feel free to make any changes to it
- The website can be run by opening one of the HTML files within a web browser
- Visit the link provided
- Your website with any made changes will appear
- Saved changes to the website will appear here after refreshing the page

The benefits of hosting your website on GitHub pages is that any pushed changes to your project will automatically update the website. Development branches can be created and merged to the master when complete.

It may take a moment for changes to appear on the hosted website.

During development the site is written in PyCharm. It is run using Live
Server plugin for PyCharm.

## Known Bugs

- CSS denied via AWS after installing gitpod in github. No time to debug
- Search not working
- Alpha, Beta nor Charlie are spawning themselves yet


## Credits

### Content
The text on the website has been written by the web designer:

### Acknowledgements
Thank you to the following for inspiration, motivation and the direction I needed:

- Seun Owonikoko    @seun_mentor
- Simen Daehlin     @Eventyret_mentor
- Michael Park      @michael_ci
- Niel McEwen       @niel_ci
