# DJANGO-REACT APP TEMPLATE

This repo contains a template for building a React application connected to a Django backend API. 

This project uses Pipenv for managing the backend virtual environment. If you do not have Pipenv installed, you can find information on installing it [here](https://docs.pipenv.org/en/latest/).

## Setup Instructions

To start a new application using this template follow these steps:
### Backend Setup
1. Make a local clone of this repo with `git clone https://github.com/thehomebrewnerd/django-react-app-template.git <appname>` where `<appname>` is the name you would like to use for your application.
2. Navigate into the directory created by the clone operation
3. Navigate into the `backend` subdirectory and start a new virtual environement using Python 3.7 by running `pipenv install --python 3.7`.
5. Start the virtual environment with `pipenv shell`.
6. Install the packages required for development by running `pipenv install --dev`
7. Run the initial Django database migrations by executing `python manage.py migrate`
8. Create a new Django superuser by running `python manage.py createsuperuser` and filling in the information requested at the prompts.
9. Test the installation by starting the develompent server with `python manage.py runserver`. Once the server is started, open your browser and navigate to [http://localhost:8000/admin](http://localhost:8000/admin) and login with the superuser credentials entered in the previous step. If you see the Django admin page, your setup was successful.

### Frontend Setup
1. COMING SOON!