from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=40)
    amount = models.IntegerField()
    article_number = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=30)
    warehouse_number = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='inWarehouse')


class Shelf(models.Model):
    shelf_number = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='inShelf')


class StorageUnit(models.Model):
    storageunit = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='inStorageUnit')
