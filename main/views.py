from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect


# Create your views here.
def index(req):
    ctx = [
        {
            "name": "Classic Leather Jacket",
            "price": 150,
            "description": "A timeless piece of fashion. Crafted from premium leather with a stylish design.",
            "category": "Clothing",
            "stock": 25,
            "image": "https://loremflickr.com/200/200?random=7",
        },
        {
            "name": "Wireless Bluetooth Headphones",
            "price": 80,
            "description": "Experience high-quality sound with these noise-cancelling Bluetooth headphones.",
            "category": "Electronics",
            "stock": 50,
            "image": "https://loremflickr.com/200/200?random=4",
        },
        {
            "name": "Portable Blender",
            "price": 45,
            "description": "Blend your favorite smoothies on the go with this compact and powerful blender.",
            "category": "Appliances",
            "stock": 30,
            "image": "https://loremflickr.com/200/200?random=2",
        },
        {
            "name": "Fitness Tracker Watch",
            "price": 60,
            "description": "Track your workouts and monitor your health with this sleek fitness tracker.",
            "category": "Accessories",
            "stock": 40,
            "image": "https://loremflickr.com/200/200?random=1",
        },
        {
            "name": "Ceramic Coffee Mug",
            "price": 15,
            "description": "Enjoy your coffee with this stylish ceramic mug. Perfect for your morning routine.",
            "category": "Kitchenware",
            "stock": 100,
            "image": "https://loremflickr.com/200/200?random=3",
        },
    ]

    return render(req, "main.html", {"products": ctx})


def show_products(req):
    data = Product.objects.all()

    context = {
        "name": "Muttaqin Muzakkir",
        "class": "PBP A",
        "npm": "2306207101",
        "products": data,
    }

    return render(req, "products.html", context)


def create_product(req):
    form = ProductForm(req.POST or None)

    if form.is_valid() and req.method == "POST":
        form.save()
        return redirect("main:show_products")  # Menggunakan nama di urls.py

    context = {"form": form}
    return render(req, "create_product.html", context)


def show_xml(req):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(req):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id(req, id):
    data = Product.objects.filter(pk=id)  # Primary key
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id(req, id):
    data = Product.objects.filter(pk=id)  # Primary key
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )
