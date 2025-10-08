from django.db import models
from cloudinary.models import CloudinaryField

class SingletonModel(models.Model):
    """
    Abstract base model for creating singleton models.
    Only one instance can exist.
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1  # Always set the primary key to 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ContactInfo(SingletonModel):
    email = models.EmailField()
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.email


class Profile(SingletonModel):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = CloudinaryField('image', blank=True, null=True)
    # profile_image = models.ImageField(upload_to='profile_images/')
    cv = CloudinaryField('raw', folder='cv', blank=True, null=True)
    # cv = models.FileField(upload_to='cv/')
    # contact = models.OneToOneField(ContactInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class About(SingletonModel):
    moto = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='about_images/')
    location = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    interests = models.TextField()
    # contact = models.OneToOneField(ContactInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.moto

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['-end_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

    @property
    def duration(self):
        start = self.start_date.strftime("%b %Y") if self.start_date else ""
        end = self.end_date.strftime("%b %Y") if self.end_date else "Present"
        return f"{start} - {end}"

class TechStack(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    tech_stacks = models.ManyToManyField(TechStack, blank=True)  # new
    description = models.TextField()
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    university = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    year_of_completion = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return f'{self.course} - {self.university}'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
