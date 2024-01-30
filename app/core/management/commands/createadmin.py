from django.core.management import CommandError
from django.utils.translation import gettext as _
from django.contrib.auth.management.commands.createsuperuser import Command as SuperUserCommand

import getpass

class Command(SuperUserCommand):
    """Create a superuser with name, username, email, and password"""

    def get_input_data(self, field_name, message=None, default=None):
        """
        Prompts the user for input and returns the entered value.
        If the user enters an empty value and a default is provided, the default value is returned.
        If the user enters an empty value and no default is provided, the function will keep prompting until a non-empty value is entered.
        """
        while True:
            if default:
                prompt = f'{field_name.capitalize()} [{default}]: '
            else:
                prompt = f'{field_name.capitalize()}: '
            value = input(message or prompt).strip() or default
            if value:
                return value

    def handle(self, *args, **options):
        email = self.get_input_data('email', message='Email address: ')
        name = self.get_input_data('name', default='', message='Name (leave blank for none): ')
        username = self.get_input_data('username', default='', message='Username (leave blank for none): ')
        password = None
        password_confirm = None
        while not password:
            password = getpass.getpass('Password: ')
            if not password:
                print(_('Error: Blank passwords are not allowed.'))
        while not password_confirm:
            password_confirm = getpass.getpass('Password (again): ')
            if password_confirm != password:
                print(_('Error: Passwords do not match.'))

        user_data = {
            'email': email,
            'password': password,
        }

        if name:
            user_data['name'] = name

        if username:
            user_data['username'] = username

        self.UserModel._default_manager.db_manager().create_superuser(**user_data)
