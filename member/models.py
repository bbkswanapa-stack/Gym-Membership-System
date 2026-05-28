from django.db import models

# Create your models here.

class GenderChoice(models.TextChoices):
    Male = 'M'  
    Female = 'F'    
    Other = 'O'

class BloodGroupChoice(models.TextChoices):
    A_Positive = 'A+'  
    A_Negative = 'A-'  
    B_Positive = 'B+'  
    B_Negative = 'B-'  
    AB_Positive = 'AB+'  
    AB_Negative = 'AB-'  
    O_Positive = 'O+'  
    O_Negative = 'O-'

class Member(models.Model):
    # Identity
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderChoice.choices, blank=True)
    blood_group = models.CharField(max_length=5, choices=BloodGroupChoice.choices, blank=True)
    
    #Contact
    phone = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone= models.PositiveBigIntegerField(default=0)

    
    joined_at = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    medical_conditions = models.TextField(null=True, blank=True)
    

    height_cm = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    weight_kg = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"