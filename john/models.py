from django.db import models

# Create your models here.
class Jade(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.TextField()
    image=models.ImageField(upload_to='jades')
    link=models.URLField(null=True,blank=True)
    fecha=models.DateField()
