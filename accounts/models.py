from django.db import models
import uuid

#============================================
#                  User
#============================================
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    # OAUTH
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=255)
#     bio = models.TextField()
#     profile_image = models.ImageField(upload_to='profile_logo/', null=True, blank=True)
#     created_at= models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.full_name
    
# class Session(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     session_token = models.CharField(max_length=255)
#     expires_at = models.DateField()
#     created_at = models.DateField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.user} - Session"


# class LoginLogs(models.Model):
#     STATUS_CHOISES = [("success","Success"), ("failed","Failed")]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ip_address = models.GenericIPAddressField()
#     status = models.CharField(max_length=10, choices= STATUS_CHOISES)
#     timestamp = models.TimeField(auto_now_add=False)

# class SocialAccount(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     provider = models.CharField( max_length=50)
#     provider_user_id = models.CharField(max_length=50)

#     class Meta:
#         unique_together = ("provider", "provider_user_id")