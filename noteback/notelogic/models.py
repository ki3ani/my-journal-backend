from django.db import models



# Create your models here.

# This is the model for the notes
class Note(models.Model): 
    title = models.CharField(max_length=100, null=True, blank=True)
    cover_image = models.ImageField(upload_to='images', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



# This is the string representation of the object
    def __str__(self):
        return self.title
    


