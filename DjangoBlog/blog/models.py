from django.conf import settings
from django.db import models
from django.utils import timezone

class Post_Type(models.Model):
    type = models.CharField(max_length=100, unique=True, default=None)

    def __str__(self) -> str:
        return self.type

    class Meta:
        verbose_name_plural = "Post Types"

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    total_views = models.PositiveIntegerField(default=0)
    type = models.ForeignKey(Post_Type, to_field="type", verbose_name="type", null=True, on_delete=models.CASCADE)
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
        
class Education(models.Model):
    university = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    college = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    
    def __str__(self):
        return self.university
    
class Work_Experience(models.Model):
    company_name = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=200)
    job_describe = models.TextField()
    
    def __str__(self):
        return self.company_name

class Course(models.Model):
    university = models.ForeignKey(Education, to_field="university", on_delete=models.CASCADE, default=None)
    course_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.course_name

class MyDetail(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "My Details"
        
class Gallery(models.Model):
    album_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.album_name
    
    class Meta:
        verbose_name_plural = "Gallery"
        
class Photos(models.Model):
    album_name = models.ForeignKey(Gallery, on_delete = models.CASCADE, blank=True)
    describe = models.CharField(max_length=500, blank=True)
    photo = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=30)
    compressed_photo = models.ImageField(upload_to = 'compressed_images/')
    
    def __str__(self):
        return str(self.album_name) + ': ' + self.title + '; ' + self.describe