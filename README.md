# Tugas 2 PBP

### Muttaqin Muzakkir, 2306207101

### PWS

Link: http://muttaqin-muzakkir-ecommerce.pbp.cs.ui.ac.id

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Membuat sebuah proyek Django baru.

**Install Django** (jika belum terinstal):

```bash
pip install django
```

**Start Project**:
`bash
    django-admin startproject ecommerce
    cd ecommerce
    `

**Run Project**:
`bash
    python3 manage.py runserver
    `

#### Membuat aplikasi dengan nama `main` pada proyek tersebut.

Aplikasi pada Django adalah semacam _module_ pada Django yang berbasis MVT. Untuk membuat app pada Django, ada commandnya.
**Membuat Django App**:
`bash
    django-admin startapp main
    `

#### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

1. Setelah menambah apps, kita harus menambahkannya ke `INSTALLED_APPS` di `settings.py`.
2. Menginisiasi sebuah `urls.py` pada folder `/ecommerce` dan mengisikannya dengan isian `/ecommerce/views.py` yang akan nanti kita buat.
3. Menambah urls baru pada project kita dengan mengkonfigurasi `/ecommerce/urls.py` untuk _map_ ke `urls.py` utama.

```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

#### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
Buat file `models.py` di dalam folder `main` dan sesuaikan dengan aplikasi. Dalam aplikasi kami, ini adalah isi models.py kami,
```python3
from django.db import models


class Product(models.Model):
    # Atribut Wajib
    name = models.CharField(max_length=255)  # Nama item
    price = models.IntegerField()  # Harga item
    description = models.TextField()  # Deskripsi item

    # Atribut Tambahan
    stock = models.PositiveIntegerField(default=0)  # Jumlah stok
    category = models.CharField(max_length=100, blank=True, null=True)  # Kategori item
    imageSrc = models.CharField(max_length=256)  # Gambar item
    rating = models.PositiveIntegerField(default=0)  # Rating item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

```


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

## Jelaskan fungsi git dalam pengembangan perangkat lunak!

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Mengapa model pada Django disebut sebagai ORM?
