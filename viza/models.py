from django.db import models

# Create your models here.



class Viza_items(models.Model):
    img =models.ImageField(upload_to = "viza" , null = True , blank = True)
    title=models.CharField(max_length=50)
    pm=models.CharField(max_length=40)
    price=models.IntegerField()
    slug=models.SlugField(null = True , blank = True)
    is_active=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False, null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class single_viza(models.Model):
    time=models.IntegerField()
    age=models.IntegerField()
    