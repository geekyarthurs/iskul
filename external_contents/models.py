from django.db import models
from tinymce import HTMLField
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    active = (
        ("T" , "True"),
        ("F", "False"),
    )
    name = models.CharField(max_length=50)
    is_active = models.CharField(choices=active, max_length=10)

    def __str__(self):
        return self.name
    

class Content(models.Model):
    name = models.CharField( max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = HTMLField()
    posted_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug =   str(slugify(self.name) ) +"-" + str(slugify(self.category))
        super(Content, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class file(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    file = models.FileField( upload_to="files", max_length=100)

    def __str__(self):
        return self.content.name
    
