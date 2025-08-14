from django.db import models


# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_influencer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Follower(models.Model):
    influencer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('influencer', 'follower')

    def __str__(self):
        return f"{self.follower.username} follows {self.influencer.username}"
