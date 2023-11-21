# Shape Shift

![header](addimg)

Welcome to ShapeShift - Your Ultimate Destination for Premium Fitness Gear!

Explore our extensive range of high-quality fitness apparel and accessories tailored for both men and women. Dive into a world of top-notch activewear designed to elevate your workout experience to new heights.

Discover the perfect fit for your fitness routine with our diverse collection. From moisture-wicking tops to flexible leggings and supportive accessories, we've got you covered for every workout need.

Effortlessly navigate through our selection using our intuitive interface and search options. Each product listing provides upfront details and the ability to explore specific features, ensuring you find the ideal gear for your active lifestyle.

Experience convenience and security with our Stripe payment integration, ensuring safe and secure transactions for your purchases. Stay updated on the latest trends and offerings by subscribing to our newsletter via Mailchimp. Receive exclusive updates, promotions, and fitness tips directly to your inbox, empowering you to stay ahead in your fitness journey.

ShapeShift - Where quality meets performance. Gear up with confidence and style, as you strive towards your fitness goals with our premium collection.


Live link to [Shape Shift](#addhere#)



## TABLE OF CONTENTS
* [Market Research](#market-research)
    - [Target Audience](#target-audience)
    - [Market Strategy](#market-strategy)
* [Agile](#agile)
* [User Experience](#user-experience)
    + [User Stories](#user-stories)
* [Design Scheme](#design_scheme)
    - [Wireframes](#wireframes)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Images](#images)
* [Data Scheme](#data_scheme)
* [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Hero](#hero)
    + [All Cars](#all-cars)
    + [Car Detail](#car-detail)     
    + [Sign Up Page](#sign-up-page)
    + [Log In Page](#log-in-page)
    + [Log Out Page](#log-out-page)  
    + [Product Management](product-management)      
    + [Admin Page](#admin-page)
* [SEO](#seo)
* [Stripe](#stripe)
* [Testing](#testing)
    + [Manual Testing](#manual-testing)
    + [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Technology Used](#technology-used)
* [Credits](#credits)



# Market Research

Market research unveils a growing trend among health-conscious individuals seeking both performance and style in their fitness apparel. ShapeShift, a B2C platform, targets this clientele, offering a curated selection of high-quality activewear and accessories.

Much like luxury cars symbolize status, fitness apparel has become a statement of dedication to wellness. Shapeshift is aiming to promote itself by driving an increased interest in premium fitness wear that seamlessly blends functionality and fashion.

Statistics highlight a rising consumer inclination towards investing in top-tier activewear. ShapeShift's B2C model strategically positions it to cater to this evolving demand, providing consumers with a range of stylish yet performance-driven options. It's a go-to destination for those seeking to enhance their fitness journey with premium, trendsetting activewear.

![statista](#ADD STATISTIC IMG HERE)

## Target Audience

From the research I've done on sites like Google Analytics and Statista.com there are THREE types of people who "Shapeshift" will appeal to.

### Lower Class: 
People who do not have lots of money can still find the website appealing as it offers free diet and workout advice and can buy acessories as they do not cost a lot.


### Middle Class :

People who make average income and can afford  some of the clothes that are on offer and acessories.

### Wealthy People :

People that can afford to buy anything on the website as they make a lot of money and are looking for either very expensive sport clothes which the website has or they are looking for cool acessories.

## Market Strategy

### Utilizing Facebook as our primary marketing platform presents an opportunity to reach a vast audience of potential customers. With its extensive user base and diverse targeting options, we can tailor our campaigns to resonate with specific demographics interested in fitness, fashion, and active lifestyles.


We would use the shapeshift facebook page to create campaigns and promote our page by boosting our posts and using facebook ads.


![facebook](Add screenshot of facebook page)

### Our secondary marketing platform is Instagram as it has a lot of users interested in working out and clothing and works very well with Facebook.

On Instagram we could collab with a popular instagram user and ask them to promote our shapeshift merch we would send them free clothes and acessories and ask them for a promotion or a hashtag in return to create views and potential customers for our website.


![instagram](add insta influencer)

## Mailchimp

Our newsletter sign-up is a vital part of our marketing strategy. It lets users subscribe for exclusive promotions and updates. The collected email lists enable our admin to send subscribers rewards, discounts, and insider info, fostering a loyal customer base.
![chimp](mailchimpform here)


# Agile

In order to complete this project I have used the Agile Methodology. This involves breaking down the project into smaller tasks called User Stories. These user stories were added using githubs Issues functionality. Each user story was made into an issue and added to the projects kanban board. 


You can view my user stories in the kanban [board here.](https://github.com/users/Gabriel5638/projects/7/views/1)

![kanban](Add kanban img with posts)


# User Experience

## Scope

In order to present the user with a compelling experience and have him enjoy his visit on our website, Shapeshift needs to tick a few boxes. The list below is an absolute must if we would like the user to return and recommend us to others.

Shapeshift needs to have these features: 


- Users can create and maintain their accounts using Django All-Auth registration and functionality.

- A landing page that makes it very apparent what the site is used for.

- A user profile page where users may view their order history and save billing information for quicker orders in the future.

- A Products Page that displays all of the Products found in the category or through the search.

- Products Cards that display an image of the item, its name, price, and an option to click for further information.

- A Search Bar, My Account Links, Shopping Cart Links, and Product Categories sections are included in the site navigation.

## User Stories

### Super-users

1. As a **superuser** I can **add products** so that **I can have more then 1 product at a time**

2. As a **superuser** I can **edit a product** so that **I can change its description,price, and category**

3. As a **superuser** I can **delete a users account if needed**

4. As a **superuser** I can **send emails to customers** so that **I can easily sell my merchendise and make offers**

5. As a **superuser** I can **add different categories of clothes or acessories** so that **I am able to manage each entry properly**

6. As a **superuser** I can **delete a Product** so that **I can manage my website properly and remove old items when they are out of stock or not selling them anymore**

### Users

7. As a **user** I can **use the recover password options** so that **to recover my password in case i forget**

8. As a **user** I can **receive a confirmation email when registering** so that **click the confirmation link be sure i am registered**
9. As a **user** I can **easily register for an account on the website** so that **receive benefits of a logged in user**
10. As a **user** I can **search by using a simple searchbar** so that **I can find exactly the item I want to buy**
11. As a **user** I can **sort items by specific category easily** so that **I can choose what to buy**
12. As a **user** I can **see my order details** so that **I can verify the item I chose and the price**
13. As a **user** I can **pay safely without having to worry about my details being stole** so that **I can shop with confidence**
14. As a **user** I can **easily view a list of items** so that **decide which one to buy**
15. As a **user** I can **click on a specific item** so that I can see relevant information about its price size and quantity
16. As a **user** I can **sign up for the newsletter** so that I can receive the latest updates
17. As a **user** I can **add payment info easily when checking out** so that **I dont have to spend much time before buying**
18. As a **user** I can **visit their facebook store page** so that **interact with the comunity closer**
19. As a **user** I can **add products to my shopping cart** so that **I can see how much i am spending and the total cost**

# Design Scheme
To make this project stand out among other fitness websites that offer similar things I decided to offer free diets and workout routines and make the pages look very attractive and flashy especially the diet page using videos of food related to the specific diet as where other subscription based websites ask for money I would offer these for free to attract customers.

This was done with aid of cool videos, of foods being prepared I found on pexels I will go more into detail about them in the "Features" section.

## Wireframes

### Homepage
![wire](addhomepagewireframe)

### Product View
![wire](adddetailwireframe)

### Product Detail
![wire](addproductwireframe)

### Shopping Cart
![wire](addshopingcartwireframe)

## Colors

I chose a very simple yet easy to view color scheme. Black and White while in some parts I used blue for the buttons and in the diets sections I used more greens just to make it stand out. But the website color scheme is mostly black and white and easy on the eyes

The Hero image dark background on the home page works very well with the black and white scheme which is why I chose it.

I used COOLORS to generate this:

![colors](add collors)


## Fonts

- I used a font named Montserrat because I like the way it looks and how the writing looks on my website. 

- You can find the font here [Montserrat](https://fonts.google.com/specimen/Montserrat?query=Montserrat)

## Images

- Clothing and acessories images were taken from pintrest and the backgrounds and hero image and videos in the home workout and diet sections were taken from pexels.


# Data Scheme

- Used DrawSQL to present my models

![data](add draw sql datamodel img here)

# Features

## Header

- I made a unique logo for the header using bootstrap.
- The navigation is very simple and contains all the categories.
- In the top right the user can acess his account and log in or out if they wish and admin can manage website
- You can also see the shopping cart icon with the total of added items.

![header](add navbar)

## Footer
![footer](add footer)
- On the left the search bar is placed, I wanted to place it at the bottom, so the user can intuitively look through the page a and see what it has to offer before searching for something.
- I have links to Facebook, Twitter, Instagram, and Youtube in the footer section.
- When you hover over the icons, you get feedback and they are totally interactive.
- To avoid diverting the user, when an icon is clicked, the page will open in a new tab.

## Hero Image
![hero](add hero img)
- I chose this as my hero image because I think it embodies everything the website is.
- On the right the user can see the white website description which works well with the dark background of the hero image.
- Added a button beside the image that takes the user straight to the all product section of the shop, so that weather they are a man or woman they can view all the items and decide after if they wish to browse either men or women section instead of taking a woman user to the mens section of the shop or vice versa.

## Diet Videos
#add here vids
- these videos I felt were really cool they are played on a loop and bring the website alive
- The videos play in the muted and in a loop slowly.

## All Products
![hero](add all products)
- Here you can see all the products in the inventory.
## Product Detail
![hero](product detail img add)
- In this section you can notice more detailed description of the item and can leave comments or ratings about products.

- This view includes rating comments and quantity select.

- You can also add to cart from this view.

## Sign Up Page
![hero](signupform)
- In this page you can see the regular sign up form

- It has validation and stops you from using bad emails or bad passwords

## Log In Page

![hero](sign in page)
### Log Out Page
![hero](logoutpage)
- Here are both the login and log out pages

## Product Management
![hero](add product management page)

- In this page you can add a new products or delete from the website, no need to go in admin page.
- Just fill up the correct fields in the form.

## Shopping Cart
![hero](shopping cart)

## Order Success
![hero](order sucess img)

- In this page , you are presented with a quick rundown of your order details that you have just placed.
## Checkout
![hero](check out)

- In the checkout view you can fill in your personal details and and press secure checkout to buy your product!

## Various Toast Messages
![hero](add toast)

![hero](addd )

![hero](addd )

![hero](add )

- There are various messages that pop up accross the website whenever we complete an action or whenever it gives us a warning.
- These ones are mostly positive and there are a couple more messages that will pop up if you do something wrong.

## 404 Page
![hero](add custom 404)

- This is our 404 page thats used to throw out errors whenever a user is attempting to access a page that doesn't work or hes not allowed to.

## Admin Page
![hero](admin panel img)

- As you can see our admin page is well structured and organized.
- It allows us to do all the CRUD actions that we require and can manage all our products.
- I can also delete a users account.

# SEO
addd this tommrow on wedsnday
## sitemap.xml
- I generated a sitemap.xml file from XML-sitemaps and downloaded it.
- I then added it to my projects root file to help search engines identifying my site properly and navigate more easily.

## Tags
![hero](media/ariatags.JPG)

- I've made sure to add lots of descriptive keywords in meta tags ands aria labels in most of my code just to improve SEO.

## robots.txt 
add robots.txt wednsday too
- I also added a file called robots.txt that instructs the search engine where to look and where not to look in our site, this also improves SEO a lot.


# STRIPE

- On this project we implemented a service called Stripe to handle payments from our customers.
- Once you set up webhooks successfully you should be able to see payments succeed in your Stripe dashboard.
- If you would like to test purchase anything on my website you can use these card details:
    - Card number: 
    - expiry: 
    - cvs: add the number after integrating stripe

### As you can see my Stripe webhooks and payments have gone through successfully.
![hero](add stripe sucess payments)



# Testing

I have conducted thorough testing of the website, as well as some close friends who I have instructed to test the site.

## Manual Testing

## User Story Testing

1. As a user I can use the recover password options so that to recover my password in case i forget

    - The 'Forgot Password' option at the bottom of the login page was used to test this. A link is then sent to the user through email, so I tested this with an already-sent email to be sure the link was received.

    - The user must wait for the password reset link to be received before using it. Once it does, they are directed to a website where they must input their old password twice in order to reset it. The user is led to a confirmation page with a bootstrap toast displaying a success message after entering the new password. An error notice alerts the user so they can try again if the passwords do not match.


2. As a user I can easily register for an account on the website so that receive benefits of a logged in user

    - This was tested by registering a couple of user accounts and:
        - making sure they worked by logging out and back in.
        - clicking the confirmation link in the email
        - scanning for verified email addresses in the admin panel.
        - using an already-existing email address to attempt to create an account


 3. As a user I can search by using a simple searchbar so that i can find exactly the product im looking for
    - I tested this by searching using the search bar in the footer and also by searching through the category links
    - The number showed matched the number of searches on each page, and it can be found on the all products page.

4. As a user I can sort products by specific category easily so that i can choose which type of product I want

    - I went to the all the product views and tested every single sorting option in the "sort by" section.
        - this included : Sort by name, sort by category and sort by price.
        - all of those options returned expected results


5. As a user I can see my order details so that i can verify the product i chose and the price
    - I selected a product put in the from the cart and clicked check out
    - After inputting my details , i clicked on secure checkout and was presented with my order details
    - I tried multiple times with various values trying to trick the form but it worked every time

6. As a user I can pay safely without having to worry about my details being stole so that i can shop with confidence
    - If the user has an account, address details can be saved and updated/removed as needed. By adding and deleting addresses from the profile page, this was put to the test. In order to verify that the address was saved on the User's Profile page after checkout, it was also inserted and saved to the profile.

    - The project makes use of Stripe to handle payments, protecting customer payment information and preventing it from being saved in their user profile.

7. As a user I can adjust the products I saved in my cart so that i can remove products.
    - I added a product to my cart and then went to the shopping cart page
    - Once on the page i was presented with the correct information as expected
    - Once I tried adjusting the Products that i added to my cart , the update went through without any issue
    - I tried multiple times to trick the system by refreshing the page etc.

8. As a user I can buy products without being logged in
    - Without being logged into an account, an order was placed. To make sure it matched what was put in the bag and afterwards checked out, it was tested by comparing the order confirmation, email confirmation, and the order within the order model. 

9. As a user I can easily view a list of products ** so that ** I can decide which one to buy
    - Once I clicked on the shop button I was presented with a well ordered list of products with the right sizes.
    - The products are displayed using bootstrap  and are very responsive due to their classes, which means the layout of the products changes with screen size.
    - All images are displayed unless theres no image, at which point the site will display a default image.

10. As a user I can click on a specific product  so that I can see relevant information about its caracteristics
    - I clicked on a product, it took me to the product details page
    - On the page it shows specific details such as size comments and ratings and of course the user can add to cart.
    - I checked different product to see if any description is the same and all of them were different

11. As a user I can sign up for the newsletter so that i can receive the latest updates
    - The user can subscribe by providing their email and clicking submit. An error warning shows below the email box if there is a problem with the email. If successful, a success message is displayed instead.

    - By subscribing with a test email and logging into Mailchimp to view the contacts, the subscription was tested. After making sure the contact was present, I scanned the page to check if they had subscribed.

12. As a user I can add payment info easily when checking out so that i dont have to spend much time before buying
    - Submitted an order while simply filling out the checkout form's mandatory information. Both Stripe and the Database successfully processed the order, which was also recorded with a success Webhook message.

    - Attempted to place an order using the wrong card information. The wrong details are confirmed by an error message that displays beneath the card details form.

    - Tried to place an order with a card that has expired. The card has expired, according to an error message that displays beneath the card details form.

    - Attempting to send a purchase order with a missing order form. All blank necessary fields notify the user that they must be filled out in order for the form to be finished and submitted.

13. As a user I can visit their facebook store page so that interact with the comunity closer
    - I scrolled down to the footer where the facebook icon is located
    - Click on the Icon and was taken directly to their facebook page
    - It opened in a new window as expected and didnt close the previous one
    - Also tested the icons in the home page and they all work

14. As a user I can add  products into my shopping cart so that I can see how much i am spending and the total cost
    - I verified to make sure the right product was added before adding an item to the cart.

    - In order to make sure the quantity in the cart matched what was added, I raised the quantity before adding it.


15. As a user I can receive a confirmation email when registering so that click the confirmation link be sure i am registered
    - By sending an order to an email address that can be verified, email confirmation was tried. The right order data and a contact email were included in an email confirmation that was sent in accordance with the template set up in the checkout app.



16. As a superuser I can edit a car products so that I can change its price, details, description
    - You can edit products in two ways, one using the admin panel and another using the edit button which appears if youre logged in as superuser.
    - I checked if that edit button appeared otherwise and it didnt if youre not a superuser.
    - Clicked the edit button and was able to edit every single field , price description etc
    - Also checked the admin panel for editing and it was the same situation everything worked without issue

18. As a superuser I can change a normal users permisions so that I can stop a user from using my website if needed
    - That can be done from the admin panel by clicking on their email and selecting the remove option.
    - This was indeed possible if you are logged into the admin panel and the user was deleted from the database.

19. As a superuser I can send emails to customers so that I can sell my products
    - When a customer signs up for emails, their information is added to the company's Mailchimp contacts list, where they can later be removed.

    - This was checked by sending an email to subscribe and then verifying that it was received by checking the Mailchimp email list. In order to make sure it was simple to remove an email from the email list, I also looked at the unsubscribe functionality.

20. As a superuser I can add different categories to products or change existing products** so that I am able to manage each product properly
    - I tested this by logging into the admin panel and clicking on the products section and then clicking what category I wanted for the list.
    - I could indeed add a product to a category and change the products category at any time


21. As a superuser I can delete Products and manage my store when products are not available anymore
    - I tested this by clicking on delete Product in admin panel.
    - If deleted the product does not show up in any category and searching for it will not cause it to show up.
    - I tested to see if you could return to an old product but got the 404 error page


## Site Features Testing
 

| Feature| Acceptance Criteria | Tests Carried out | Result |  
| --- | --- | --- | --- | 
| Admin CRUD | Admin account can create/update/delete any product | Created admin account, logged in and clicked every button for create,update or delete| Pass |
| Admin restricted access | Access to admin page is not available to normal users | Created a normal user and attempted to log into the admin page | Pass |
| Non Authenticated admin user/ product management  | Product management is not available if logged out|Logged out and refreshed the page many times, clicked on different pages of the website to check if the product management page was visible| Pass | 
| Registration/ left blank |A message appearing that says "fill out this field"| Attempted to create an account with fields left blank or adding a space and then clicking sign up| Pass | 
| Registration/ bad email| A message appearing that instructs you about email address format| Tried creating an account by using random letters and numbers, also by not finishing the address after "@"| Pass | 
| Registration/ Common Password |A message appearing that instructs you the password is too common| Added a password that was very simple and easy to guess such as "password"| Pass | 
| Registration/ Short Password |A message appearing that says your password is too short and it must contain 8 characters | Created account and added password "123"| Pass | 
| Login/ Blank Field | A message instructing you to fill out this field|Attempted to log in without filling up the username field | Pass | 
|Login/ Incorrect Username|A message that says "username or password you specified are not correct"|Tried logging in with random letters and numbers in the username field| Pass |
|Login/ Incorrect Password| A message that says "username or password you specified are not correct"|Tried logging in with random letters and numbers in the password field| Pass |
|Logged in/ billing details saved  |billing details saved from previous purchases |Created a new user and logged in, made a 
| Subscribe mailchimp |Submit button should work after you add ur email|Added email in the footer form and clicked submit, also added a invalid email and got an error | Pass | 
|Message/ login | Message appears confirming successful login |Logged in on an account| Pass |
|Logout Page |Page pops up asking the user to confirm logout| Clicked on log out button| Pass |
|Message/ logout |Message appears confirming successful logout|Clicked on the log out button and then again on log out| Pass |
|Search bar |Searchbar should return a products related to your search|Searched for the word shirt and it returned shirt in all products| Pass |
|Category dropdown menu|A menu should drop down revealing the sort options | Clicked on the drop down and the sort by options were revelead | Pass |
|Secure Checkout |Adding invalid credit card information should return an error| Added 0000 in all fields and the error message appeared| Pass |
|Forgot Password |Clicking on forgot password in the login should take you to a password reset page|Clicked on forgot password and it took me to a password reset page| Pass |
|Footer Socials|Social icons appear in the footer and on home page and open their pages in a new tab when clicked.| Clicked on the social icons on the bottom of the page and on home page| Pass |

## Validator Testing

### CSS Validator
I ran the CSS code through W3C Validator and returned no errors:
![header](add all css validation)
### HTML Validator
I ran the entire website through HTML Validator as well and returned no errors:
![header](add all html validation)
###
I also used Lighthouse on most pages and they were all good scores, Accesibility is barely not in the green because of stylistic choices
![header](add lighthouse)
### Pep8 Validator
#### I used the online pep8 validator tool to check all python code and it returned no error.


# Deployment

## 1. Get the project running locally with Django

- Go to Code Institutes Github

- On the Code Institute's "Full template", click on the "Use this Template" button.

- Open Gitpod from the template and inside Gitpod take the following steps:
- Install Gunicorn with pip3 "install Gunicorn" and also install django 
- Next you need to install the database libraries with : pip3 install dj_database_url psycopg2
- Time to create your Django project, in the terminal window type: django-admin startproject your-chosen-name
- Next start your Django app with : python3 manage.py startapp your_app_name
- Add your app to the settings.py file
- You should be good to go with django now, just type: python3 manage.py runserver


## 2. Implement Heroku and AWS

- Create a Heroku account if you dont have one

- Create a new app on heroku by clicking top right "Create new app"

- Go through the steps and select your region

- Click on the Settings tab of your new heroku tab

- Reveal Config vars and add the following configs: 

SECRET_KEY

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

EMAIL_HOST_PASS

EMAIL_HOST_USER

STRIPE_PUBLIC_KEY

STRIPE_SECRET_KEY

STRIPE_WH_SECRET

DISABLE_COLLECTSTATIC = 1

- Now go down to the Buildpack section click Add Buildpack then select python and Save Changes

- Click on the Deploy tab lower down the page

- Select Github when prompted

- Confirm you want to connect to GitHub and search for the repository then click the connect button

- Make sure you click on Enable Automatic Deploys so heroku deploys whenever you git push

- Create a Procfile "web: gunicorn your_project_name.wsgi"
- When you've finished coding your website make sure you change the DEBUG to False in settings.py
- Go back to heroku and take the following steps:
- settings > config vars delete the record for DISABLE_COLLECTSTATIC
- settings > config vars set the record for USE_AWS to True


## Technology Used

- HTML5
- CSS3
- Python
- Django
- Bootstrap
- FontAwesome
- Google Fonts
- GitPod
- GitHub
- DevTools
- Heroku
- Balsamiq
- PostgreSQL
- Allauth
- Jquery
- AWS
- Stripe


## Credits
- Pintrest for the clothing and acessories images
- Pexels for the diet video and hero image
- Boutique-ado walk through for the template
- Previous projects done by Code Institute students - Also a big source of inspiration
- Code Institute Tutor Team - They were a huge help and I couldn't have completed this project without them.
- Stack overflow for helping me fix a huge csrf token bug
