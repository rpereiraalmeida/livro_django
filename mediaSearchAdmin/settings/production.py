from .settings import*

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'Dw#.LY6%89K(SCj0'

# Configuração do IP de acesso para o app // pode ser vazio []
# Alterar para o ambiente de produção quando houver
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}