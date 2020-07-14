#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    #Determine whether dev.py exists
    try:
        from auditor.settings import dev
        settings_path = 'auditor.settings.dev'
    except ImportError:
        from auditor.settings import prod
        settings_path = 'auditor.settings.prod'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)

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
