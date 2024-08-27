from django.db import models





class Bus(models.Model):
    bus_name=models.CharField(max_length=50)
    start=models.CharField(max_length=100)
    end=models.CharField(max_length=100)
    movetime=models.DateTimeField()
    price=models.IntegerField()
    
    
    def __str__(self):
        return self.bus_name
