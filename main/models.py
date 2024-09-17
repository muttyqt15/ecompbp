from django.db import models


class Product(models.Model):
    # Atribut Wajib
    name = models.CharField(max_length=255)  # Nama item
    price = models.IntegerField()  # Harga item
    description = models.TextField()  # Deskripsi item

    # Atribut Tambahan
    stock = models.PositiveIntegerField(default=0)  # Jumlah stok
    category = models.CharField(max_length=100, blank=True, null=True)  # Kategori item
    image = models.CharField(
        max_length=256, default="https://loremflickr.com/200/200?random=7"
    )  # Gambar item
    rating = models.PositiveIntegerField(default=0)  # Rating item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Person(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    isHappy = models.BooleanField(default=True)
