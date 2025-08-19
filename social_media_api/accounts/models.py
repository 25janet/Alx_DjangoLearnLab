from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_followers',
        blank=True
    )

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_following',
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        """Follow another user"""
        self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        self.following.remove(user)

    def is_following(self, user):
        """Check if following another user"""
        return self.following.filter(id=user.id).exists()
