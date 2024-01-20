from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): 
    dob = models.DateField(null=True, blank=True)
    profilePicture = models.ImageField(upload_to='./static/images/profile_pictures/', null=True, blank=True)
    phoneNumber = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField(default=0)

    # Add related_name to avoid clashes with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
 
    def __str__(self):
        return self.get_full_name() or self.username

class TrashSubmission(models.Model):
        image = models.ImageField(upload_to='trash_images/')
        customerID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        mapsURL = models.CharField(max_length=255)
        created_at = models.DateField(auto_now_add=True)
        validity = models.BooleanField(default=False)


class GiftCardCompany(models.Model):
    companyName = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.companyName
    
class GiftCard(models.Model):
    company = models.ForeignKey(GiftCardCompany, on_delete=models.CASCADE)
    amount = models.FloatField()


class Order(models.Model):
    giftCardID = models.ForeignKey(GiftCard, on_delete=models.CASCADE)
    customerID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    orderDate = models.DateField(auto_now_add=True)


