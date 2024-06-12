Create directory for media files:
1) Go to settings.py :
    - import os
    - MEDIA_URL = "directory_name"
    - MEDIA_ROOT = os.path.join(BASE_DIR, 'directory_name') - create directory_name in project directory
2) Go to urls.py and add :
    - from django.conf.urls.static import static
    - from django.conf import settings
    2.1)
    - urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


Add views:
1) App directory
   - Create folder with name templates inside create folder with app name inside create html file
   - In views.py create class or function 
Project directory
   - In urls.py import views from app:  from app_name import views and add path in urlpatterns
2) OOP concept:
    - APP directory
      - in views.py create class
      - in urls.py create path 'views.MenuList.as_view()' - when we use class instead function use code like this where MenuList class name


Add static files:
1) App directory :
   - static directory
     - app_name directory
       - move from folder in pc to app_name directory 
   - in html file before img tags add {% load static %}
   - in html file add tag <img src="{% static 'app_name_dir/file_name' %}">


LOGIN/LOGOUT:

- SETTINGS.PY
  - LOGIN_URL = 'login'
  - LOGOUT_URL = 'logout'
1) LOGIN
   1.1) Project Directory / settings.py - add LOGIN_REDIRECT_URL = 'app_name:template_name' - it is said to system where redirect after login
   1.2) urls.py
         - from django.contrib.auth import views as auth_views
         - path('login/', auth_views.LoginView.as_view(template_name='template_name.html'), name='login')
   1.3) templates/template_name.html - add form example to this page
2) LOGOUT
   2.1) urls.py
        - from django.contrib.auth import views as auth_views
        - path('logout/', auth_views.LogoutView.as_view(template_name='template_name.html'), name='logout')
        - add form with logout button and action url connect with logout in app
   2.2) templates/template_name.html - add login form for redirect to login page after click or write text


REGISTRATION:
- in views.py define function or create class for your path
  - from django.contrib.auth.forms import UserCreationForm - a special form that makes it easy to create a new user in your application
    - render(request,'page_name.html', {'key_name': UserCreationForm()})
  - from django.contrib.auth.forms import AuthenticationForm - is used to allow a user to log in to their account in page
  - from django.contrib.auth.models import User - for creating user
  - from django.db import IntegrityError - if user try to register same in DB which register by another user before
  - from django.contrib.auth import authenticate - compare user input with data from DB


Show and update custom form:
1) Project directory
   - create path for view detail of todo
2) App directory
   - in views.py define function
     - from django.shortcuts import get_object_or_404 - find todo
     - write to conditions 
       - GET - if you only want to see form_object
       - POST - if you want to update form_object


Limitations for unregistered users work with functions:
1) Project directory
   - in settings.py create LOGIN_URL = 'add_path' - if page login required , redirect to this url
2) App directory
   - from django.contrib.auth.decorators import login_required  - in views.py
   - @login_required - before views add this code
   2.1) class base view : 
     - from django.contrib.auth.decorators import login_required
       from django.utils.decorators import method_decorator
     - @method_decorator(login_required, name='dispatch')

EMAIL SENDING WITH DJANGO:
1) Project directory
   - in settings.py configure for gmail
     - EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
     - EMAIL_HOST = 'smtp.gmail.com'
     - EMAIL_PORT = '587'
     - EMAIL_USE_TLS = True
     - EMAIL_HOST_USER = 'MAIL ACCOUNT'
     - EMAIL_HOST_PASSWORD = 'MAIL PASSWORD GENERATE WITH APP'
2) App directory
    - in views.py
      - from django.core.mail import EmailMessage
      - message_body = f'Add message body'
      - email_message = EmailMessage('Subject message', message_body, to=[email] - field in model)
      - email_message.send()


Customize admin panel object view:
1) App directory
   - create class and inherit from admin.ModelAdmin    
     - list_display = () - show columns
     - search_fields = () - search area
     - list_filter = () - filter in the right side
     - ordering = () - sorting
     - readonly_fields = ()
2) Add extra fields to user:
    - create new model for extra fields
    - connect model with built-in User model with one or many
    - make migrations and migrate


Django magic methods :
1) If you want automatically define 's' and the end of word in html (singularize and pluralize) use syntax : {{ dictionary_name_in_function.count|pluralize }}
2) If you want to change date format from html file using jinja : {{ variable_name.date|'format which you want' }}
3) If you want to truncate length of text which you want to show use: {{variable_name.description|truncatechars:chars_number }}
4) If you want to use html tags from admin panel when you write text use : {{ variable_name.description|safe }}
5) If you want to change name of model which we show in admin panel:
     - in models.py add self function and in return use which field you want to show  in admin panel
6) If you want to check which path is rendering from html page use : {% if request.path == '/your path/' %} output {% endif %}
7) If you have more than one app with same html file name 
   - add in app directory urls.py app_name = 'appName', and in html file {% url 'appName:viewFunctionName' %}
8) If you do not want to show all information in one page, or you want to sort by date: model_name.objects.order_by('-date')[:5]
9) if you have custom form tags in html page you can connect them with your function in views.py using their 'name' attribute example: 'name' = forms.cleaned_data['name']  
10) If you want to choose multiple value use 'choices', use meal_type = models.CharField(max_length=200,choices=MEAL_TYPE),  where meal tuple of tuples
11) If your model name is Post or Item anyone, django automatically create variable with same name that model but in lowercase like post or item, and you can use it in template like {{ item.name }}
12) If you want automatically add request user to model use consept inside class based create view:     def form_valid(self, form):  - built in method for form validation
                                                                                                            form.instance.user_name = self.request.user - accesses the user_name field in the data entered by the user in this form
                                                                                                            return super().form_valid(form) - including creating a new object based on data from the form and saving that object to the database.
13) if you want to customize form fields use :
    - pip install django-widget-tweaks
    - INSTALLED_APPS = ['widget_tweaks',]
    - {% load widget_tweaks %} - add before forms
    - {{ form.name|add_class:"form-control" }}  - add in template