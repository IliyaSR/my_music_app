from django.core.validators import MinLengthValidator
from django.db import models
from my_music_app.account.validators import validate_username, age_validate


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=(MinLengthValidator(2), validate_username))
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True, validators=(age_validate,))

    def __str__(self):
        return self.username
