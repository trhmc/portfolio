# portfolio
My own portfolio

### Create project
Installation scripts for React and Django
1. cd into projcet (cd myprojectpath)
2. create React front-end template
```npx create-react-app my-project-front-end
cd my-project
npm start
```
3. Installing django using pipenv
```pipenv shell
pipenv install django
```

4. create back-end template within that virtual environment
```django-admin startproject my-project-back-end```

### Create different model for different pages
Creating new app
```python manage.py startapp myapp```
Creating class in models.py to store obj
Adding changes to database (each time modify models.py)
```python manage.py makemigrations myapp```
### Create entries in database
```
python manage.py shell
>>> from projects.models import Project
>>> p1 = Project(
...     title='My First Project',
...     description='A web development project',
...     technology='Django',
...     image='img/project1.png'
... )
>>> p1.save()
```


## Resource
https://realpython.com/get-started-with-django-1/
https://create-react-app.dev/docs/updating-to-new-releases