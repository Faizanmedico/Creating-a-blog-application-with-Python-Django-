# Creating-a-blog-application-with-Python-Django-
This creates the main project structure:
django-blog/
├── personal_blog/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/
└── manage.py
Run the Development Server (to verify setup):
Bash

python manage.py runserver
Open your browser to http://127.0.0.1:8000/. You should see the Django success page.



8. Build Templates (HTML Structure)

Templates render the data to the user.

Create a templates directory inside your blog app:

blog/
└── templates/
    └── blog/
        ├── base.html
        ├── index.html
        ├── post_detail.html
        └── category_posts.html
blog/templates/blog/base.html (Base template for common elements):



#python manage.py runserver

