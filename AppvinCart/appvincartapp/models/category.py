from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
# we are not getting category therefore this method is created

    def __str__(self):
        return self.name

    
    