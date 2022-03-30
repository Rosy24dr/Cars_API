# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@&^k66n!ttc5n8+@5zgs#hx#)a5w#53+o22gm36auouoi03@45'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Zailamatthewhaziel3@',
    }
}

