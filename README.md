# DeepBlue
## Full-Stack-Frameworks-with-Django-Milestone-Project4

## DEMO

A live demo website can be found here : <https://bh-deepblue.herokuapp.com/>


## Context
DeepBlue is a mobile-responsive ecommerce store that serves as a platform between divers and dive trips providers. Vendors looking to promote their 
upcoming dive trips can post it on DeepBlue, while divers looking to go on a trip can sign up an account as a customer and view all upcoming trips.

With many small dive operators with no huge marketing budgets, DeepBlue aims to provide them a cost effective way to advertise for their service. 


# UX
### STRATEGY
* Target audience
    - Divers looking for a dive trip
    - Dive instructors looking to arrange a dive trip for the students
    - Vendors looking to promote their dive packages
    - Vendors look to create awareness for their ongoing promotions
* Goals
	- User to be able to browse and purchase dive packages
	- Vendors to advertise their upcoming dive packages

## SCOPE
### User Stories
|Who| Want to| So that|
|------ | ------ |------ |
| Site Visitor | register for an customer account | have a personal account | 
| Site Visitor | register for an vendor account | have a vendor account to post trips | 
| User | view a list of all upcoming trips | choose a trip to purchase or add to wishlist | 
| User | view a trip details | to find out more information | 
| User | easy view of total amount in cart | determine if it fits my budget |
| User | search for a dive | to find specific dive trips I'm interested in |
| User | easy selection of quantity when purchasing | select exact quantity to purchase |
| User | view items in cart | double check on my purchases |
| User | easy checkout | hassle free online payment |
| Vendor | CRUD functions for me to post | able to advertise on upcoming trips |

### Sitemap/Wireframes/Database Structure
The sitemap was created to help me conceptualise the User Flow when visiting the website. It can be viewed [here](resources/sitemap.jpg).

The wireframe helps me to visualise the page layout. It can be viewed [here](resources/wireframe.png).

# FEATURES

### 1. Landing Page
* Site visitor will be prompted to create or login as they click on the 'Get Started' button
* Site visitor able to view all trips without signing in 

### 2. User accounts
* During registration, user is able to select the account type to sign up - Customer/Vendor
* A confirmation email will be sent to email address

### 3. Vendor
* As a vendor, user will be able to access the 'Vendor' tab on the Nav Bar.
* CRUD functionalities for vendors to post their Dive packages

### 4. Customer
* As a customer, user will be able to view all trips, add to cart or add to wishlist any of the trip.
* User can do a search for a specific trip containing the search keyword
* User will be able to delete items off wishlist, wishlist can be access through the icon beside Username shown on the Nav Bar

### 5. Cart and checking out
* Trips can be added to cart
* User is able to view all items in cart
* Quantity of items can be adjusted in cart
* Cart will show the total cost of all items
* Upon checkout, user will be directed to Stripe payment

### 6. Testing accounts
|Type| User | Password |
|------ | ------ | ------ |
|Vendor| johndoe | django123 |
|Customer| bluescuba | django123 |

## FUTURE FEATURES
* User to be able to filter by dates
* User to be able to 'like' a trip, and post a review
* More functions on User Profile
* Vendors to be able to post multiple photos when creating a Dive Trip

# TECHNOLOGIES USED
* HTML5
* CSS3
* Bootstrap4
* Javascript
* Python
* Django
* PostgresSQL
* Stripe
* [UploadeCare](https://uploadcare.com/) - User to upload photos (limited to 1MB per upload for free account)
* Git and Gitpod
* Heroku

# TESTING
### Manual Testing

|Test Description| Results|
|------ | ------ |
| Call to action button("Get Started") redirects to sign up page if user is not logged in | Pass |
| Call to action button("Get Started") redirects to product page if user is logged in | Pass |
| User able to view products page when not logged in | Pass |
| User to be able to create a customer account | Pass |
| User to be able to create a vendor account | Pass |
| Log in and log out | Pass |
| Vendor able to access 'vendor' tab | Pass |
| Vendor able to perform CRUD functions | Pass |
| Customer to add trip to wishlist | Pass |
| Customer to delete trip to wishlist | Pass |
| All trips carousel | Pass |
| Add to cart | Pass |
| Change quantity in cart | Pass |
| Delete cart items | Pass |
| Shows total cost of all items in cart | Pass |
| Checkout | Pass |
| Handles all 404 routes | Pass |
| Mobile Responsive | Pass |

# DEPLOYMENT
This site is hosted using Heroku, deployed directly from the master branch. This site can be viewed [here](https://bh-deepblue.herokuapp.com/). 
The deployed site will update automatically upon new commits from the master branch.

To run locally, clone this repository directly into the editor of your choice by pasting git clone 
`heroku git:clone -a bh-deepblue` into your terminal.


# CREDITS
* Images
    - https://giphy.com/
    - https://www.pexels.com/

* Logos
    - https://www.freelogodesign.org/

* Icons
    - https://www.flaticon.com

# Acknowledgements
* Nav side bar - https://www.w3schools.com/
* Get Started Button - https://dev.to/webdeasy/top-20-css-buttons-animations-f41
* All trips carousel - https://codepen.io/kreigd/pen/ybYNoN

**This is for educational use** 