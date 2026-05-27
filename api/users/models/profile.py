from django.db import models

from api.users.models import User


class Profile(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profiles'
    )
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=65)
    street = models.CharField(max_length=128)
    house_number = models.CharField(max_length=16, blank=True, null=True)
    postal_code = models.CharField(max_length=19, blank=True, null=True)
    headline = models.CharField(max_length=100, verbose_name="Slogan / Titel")
    description = models.TextField(verbose_name="Beschreibung (Über mich)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile'
        ordering = ['-created_at']
        app_label = 'users'
        constraints = [
            models.UniqueConstraint(fields=[
                'country',
                'city',
                'street',
                'headline',
                'description'
            ],
                name='unique_profile_with_description')
        ]

    def __str__(self):
        parts = [self.country, self.city, self.headline]
        if self.owner:
            parts = [self.owner.first_name, self.owner.last_name, self.city]
            return ', '.join(filter(None, parts))
        return ', '.join(filter(None, parts))