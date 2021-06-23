from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self,email, password, **extra_fields):
		if not email:
			raise ValueError("The Email must be set")
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password, **extra_fields):
        # """
        # Create and save a Superuser with the given email and password.
        # """
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)
		extra_fields.setdefault('is_admin', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError("Superuser must have is_staff = True")
		if extra_fields.get('is_superuser') is not True:
			raise ValueError("Superuser must have is_superuser = True")
		return self.create_user(email, password, **extra_fields)
	
       


class Account(AbstractBaseUser):
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
   
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    first_name              = models.CharField(max_length=30,null=True)
    last_name               = models.CharField(max_length=30,null=True)
    
    


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    def __str__(self):
        return self.email
		

    


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
		

		
class profile_verify(models.Model):
    user1 = models.OneToOneField(Account, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user1.email
	
	
	
	
	
	
	
    
    
	
	


	

	

	
	# For checking permissions. to keep it simple all admin have ALL permissons
	

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    

