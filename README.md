# Personal-Gallery-application
This is a personal gallery web by django where the user sees all the pictures an admin has posted  
## Built By [Um Magnific](https://github.com/Magnific7/)
## Description
This is an application that allows users to view images. Image details are stored in categories and tagged by Location. The admin is responsible for uploading, editing or deleting images.
## User Stories
These are the behaviours/features that the application implements for use by a user.
Users would like to:
* View all images submitted.
* Click on images to display more details.
* Search for images by category.
* Copy links to images to share with their friends
## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the gallery
* Create new images for showcasing
* Delete images
* Update image post details.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **/admin/** | Access Admin dashboard |
| Display all images | **the gallery** | Clickable links to open any images in a modal |
| Display single images on click | **On  click** | All details should be viewed|
| To add an image  | **Through Admin dashboard** | Add and add categories and tag location of Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through Admin dashboard ** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by category|
| To filter by Location  | **Click drop-down on navbar** | Users can view images by Location|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt
## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test 
## Technologies Used
* Python3.6
* Javascript
* Django and postgresql

## License

Copyright (c) 2019 Magnific
