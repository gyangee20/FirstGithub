from django.db import models
class Menu(models.Model):
    menuId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)