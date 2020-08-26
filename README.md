Customers API
============

This is a Customers API built using Docker and Django with CSV/DB data management. 



To set this project up, run this commands on your console:
    
    #Setup the database and the web service
    docker-compose up -d db
    docker-compose up -d web
    
    #Creates and setup the migrations for the model
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    
    #Creates the super user
    docker-compose run web python manage.py createsuperuser
    
    #Runs the script for filling the Customer table
    docker-compose run web python manage.py runscript parse_csv
    
    #Runs the database and the web service
    docker-compose up


Urls
----

For accessing to the project, you just have to access to the different urls:
    
    http://0.0.0.0:8000 # For accessing to the swagger interface
    http://0.0.0.0:8000/admin/ # For accesing to the admin interface