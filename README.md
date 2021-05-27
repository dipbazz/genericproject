# How and when to use GenericForeignKey in Django
---
## About

A Django web application that uses `GenericForeignKey` to reduce the dependence on multiple `ForeignKey` in single model. 
The repository is reference to my blog article [How and when to use GenericForeignKey in Django](https://dipbazz.medium.com/how-and-when-to-use-genericforeignkey-in-django-ad88202be0f)

## Getting the app in the local machine.

### Installation instructions

- Clone the repo and navigate to the directory
- Create virtual environment how you like but I use [virtualenv](https://virtualenv.pypa.io/en/latest/). If you are using the same thing as I do then,
    ```
    // for linux user
    virtualenv venv -p python3
    ```
- Activate the virtual environment.
    ```
    source venv/bin/activate
    ```
- Migrate the migrations file.
    ```
    python manage.py migrate
    ```
- If you would like to create super user and start adding information in database go ahead.
    ```
    python manage.py createsuperuser
    ```
- Run the server.
    ```
    python manage.py runserver
    ```
- Open your browser at [localhost](http://localhost:8000/). You will see a nice Django default web page.


## Built With

- Python (v3.8.5)
- Django (v3.2)


## Authors

👤 **Dipesh Bajgain**

- GitHub: [@dipbazz](https://github.com/dipbazz)
- Twitter: [@dipbazz](https://twitter.com/dipbazz)
- LinkedIn: [Dipesh Bajgain](https://www.linkedin.com/in/dipbazz/)


## Acknowledgments
- I have followed the article [How to Use Django's Generic Relations](https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html) from [simple is better than complex](https://simpleisbetterthancomplex.com/)
- The official Django documentation is really great for understanding the concept of [contenttypes framework and Generic Relation](https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/)

## 📝 License

This project is [CC0](./LICENSE) licensed.
