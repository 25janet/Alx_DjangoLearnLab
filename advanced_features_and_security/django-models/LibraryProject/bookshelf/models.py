from django.db import models
from django.contrib.auth.models import  AbstractUser,BaseUserManager
from django.contrib.auth.models import Groups,Permission
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError("The email field is required")
        email = self.normalize_email(email)
        user = self.model.(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

class CustomUser(AbstractUser):
    date_of_birth = models.DateTimeField(blank = True)
    profile_picture = models.ImageField(null = True, blank = True,upload_to = "profiles/")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 
    class meta:
        permissions = [
            ("can_view", "Can View"),
            ("can_edit", "Can Edit"),
            ("can_delete", "Can delete"),
            ("can_post", "Can Post"),
            ("can_create", "Can create")

        ]
    def __str__(self):
        return self.email
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view post"),
            ("can_create", "Can create post"),
            ("can_edit", "Can edit post"),
            ("can_delete", "Can delete post"),
        ]

    def __str__(self):
        return self.title

#create groups
viewers_group, _ = Group.objects.get_or_create(name="Viewers")
editors_group, _ = Group.objects.get_or_create(name="Editors")
admins_group, _ = Group.objects.get_or_create(name="Admins")
#fetch permissions
can_view = Permission.objects.get(codename="can_view")
can_edit = Permission.objects.get(codename="can_edit")
can_post = Permission.objects.get(codename="can_post")
can_delete = Permission.objects.get(codename="can_delete")
can_create = Permission.objects.get(codename="can_create")
#assign
viewers_group.permissions.add("can_view")
editors_group.permissions.add("can_view", "can_edit","can_create","can_post")
admins_group.permissions.add("can_view","can_edit","can_create","can_post","can_delete")
