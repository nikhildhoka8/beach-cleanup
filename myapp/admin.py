from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TrashSubmission, GiftCard, Order, GiftCardCompany

# Register your CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Customize the display fields if needed
    list_display = ['username', 'email', 'dob', 'phoneNumber', 'city', 'points']

admin.site.register(TrashSubmission)
admin.site.register(GiftCard)
admin.site.register(Order)
admin.site.register(GiftCardCompany)