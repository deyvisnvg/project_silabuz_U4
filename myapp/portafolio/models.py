from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Portafolio(models.Model):
    foto = models.TextField()
    titulo_project = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    url_github = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'portafolio'
