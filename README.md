
# Author
**Timothy Mugendi**
## Description on how to use this repository
Step by Step Mpesa Integration Using Django 3.9 and Python 3.8
Django is considered as a backend python framework. It can be used to make diverse integrations. In our scenario, we are going to see our to integrate safaricom daraja Apis. This repository greatly helps demistify integration of daraja Apis thus enhancing easy integration.
## Getting Started
We shall start with integrating STK Push
### STK Push integration

- create a folder on you local machine and navigate into that folder
- Create a virtual environment by running the command: python3 -m venv virtual
- Activate the virtual environment using the name, virtual: source virtual/bin/activate
- Install django: pip install django==3.9
- Create the project: django-admin startproject mpesaApi .
- Create the application: django-admin startapp darajaApp
- Connect the application, darajaApp to the project mpesaApi by linking the app url into the project urlpatterns
- Inside the app darajaApp, create a file called: safaricom_credentials.py and urls.py
- Add the code in safaricom_credentials.py
- Add urls that are in urls.py
- Finally add lipa_na_mpesa_online and getAccessToken functions as they are in the views.py of the darajaApp application
- We first generate the token then do the stk push
- Run the local development server: python3 manage.py runserver
- Remember to use your credentials that you generate from the safaricom developers' daraja portal
- Navigate to the url: http://localhost:8000/api/v1/online/lipa/
- The stk push is thus made successfully: Try and understand the code
### C2B integration

- Add urls that are labelled C2B in urls.py
- Add functions below #start of C2B mpesa payments with csrf_exempt as they exist in the views.py of the darajaApp application
- Add the business_shortcode in the safaricom_credentials.py, c2b works with the business_shortcode
- We first generate the token and pass it for authentication
- Before running the local server, set up the ngrok for secure tunneling into the safaricom site
- Run the local development server: python3 manage.py runserver
- Remember to use your credentials that you generate from the safaricom developers' daraja portal
- Navigate to the url: http://localhost:8000/api/v1/c2b/register/
- The c2b is thus made successfully: Try and understand the code on your own





