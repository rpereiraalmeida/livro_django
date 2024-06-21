from .settings import*

DEBUG = True

# Secret key para o ambiente de desenvolvimento
SECRET_KEY = 'rq(%>JL"F@,$\dLAWrmv)e>4JX'

# Você pode deixar em branco com colchetes vazios []
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}