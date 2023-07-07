from django.core.exceptions import ValidationError
#from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


@deconstructible
class FileExtensionValidator:
    def __init__(self, allowed_extensions=None, message=None):
        self.allowed_extensions = allowed_extensions
        self.message = message or _('File extension "%(extension)s" is not allowed. Allowed extensions are %(allowed_extensions)s.')

    def __call__(self, value):
        if self.allowed_extensions is not None:
            extension = value.name.split('.')[-1].lower()
            if extension not in self.allowed_extensions:
                allowed_extensions = ', '.join(self.allowed_extensions)
                raise ValidationError(
                    self.message % {'extension': extension, 'allowed_extensions': allowed_extensions},
                    code='invalid_extension'
                )

def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()

    if not email:
        raise ValidationError('An email is required')
    
    if not password or len(password) < 6:
        raise ValidationError('Choose another password. Minimum 6 characters required')
    
    if not username:
        raise ValidationError('Choose another username')
    
    return data

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('An email is needed')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('Choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('A password is needed')
    return True