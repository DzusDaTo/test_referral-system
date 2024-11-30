import random
import string
from django.db import models


def generate_invite_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, unique=True, default=generate_invite_code)
    activated_invite = models.CharField(max_length=6, null=True, blank=True)
    invited_users = models.ManyToManyField('self', symmetrical=False, related_name='invited_by')

    def __str__(self):
        return self.phone_number

