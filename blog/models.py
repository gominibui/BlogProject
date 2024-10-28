from django.core.validators import MinLengthValidator
from django.db import models


class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(max_length=200)
    image_field = models.ImageField(upload_to='posts', null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField( validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)

