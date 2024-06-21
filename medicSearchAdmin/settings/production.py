from .settings import*

DEBUG = True

# Secret key para o ambiente de desenvolvimento
SECRET_KEY = 'rq(%>JL"F@,$\dLAWrmv)e>4JX'

# Alterar para o Ip do ambiente de produção quando houver
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}