from django.db import models

class Great(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('company', 'Company'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    # Common fields
    full_name = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True,unique=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    # Student fields
    skills = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    internship_location = models.CharField(max_length=100, blank=True, null=True)

    # Company fields
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    number_of_interns_required = models.IntegerField(default=0, blank=True, null=True)
    
    # (Optional) for OTP verification
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        if self.role == 'company':
            return f"{self.company_name} ({self.email})"
        else:
            return f"{self.full_name} ({self.email})"
    # AI Matching Models
class Candidate(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    skills = models.TextField()
    internship_location = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    past_participation = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Internship(models.Model):
    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    skills_required = models.TextField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} at {self.company_name}"
