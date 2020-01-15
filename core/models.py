from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Sector


class UserProfile(models.Model):
    SECTOR = 1
    DISTRICT = 2
    SUPER = 3
    ROLE_CHOICES = (
        (SECTOR, 'Sector Level User'),
        (DISTRICT, 'District Level User'),
        (SUPER, 'Super Level User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_profiles')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.get_username()
