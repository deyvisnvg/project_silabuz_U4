from django.db import models

# Create your models here.


class Portafolio(models.Model):
    foto = models.TextField()
    titulo_project = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    url_github = models.TextField()

    class Meta:
        db_table = 'portafolio'
