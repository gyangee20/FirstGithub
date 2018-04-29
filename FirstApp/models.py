from django.db import models
class Menu(models.Model):
    menuId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
class Item(models.Model):
    itemId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE)