#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Configuração padrão de instalação
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediaSearchAdmin.settings')

    # Configurado para a variável de ambiente apontar para o ambiente de desenvolvimento
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediaSearchAdmin.settings.development')

    # Configurado para a variável de ambiente apontar para o ambiente de teste
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediaSearchAdmin.settings.testing')

    # Configurado para a variável de ambiente apontar para o ambiente de produção
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediaSearchAdmin.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
