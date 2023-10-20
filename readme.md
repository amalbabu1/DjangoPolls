# start the development server

    python manage.py runserver

# the three-step guide to making model changes:

    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.

# forloop.counter indicates how many times the for tag has gone through its loop

# F() objects assigned to model fields persist after saving the model instance and will be applied on each save().

link : https://docs.djangoproject.com/en/4.2/ref/models/expressions/#avoiding-race-conditions-using-f

# generic views

https://docs.djangoproject.com/en/4.2/intro/tutorial04/

# test

CREATE function with names that begin with test
