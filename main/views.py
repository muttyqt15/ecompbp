from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect


# Create your views here.
def index(req):
    data = Product.objects.all()
    return render(req, "main.html", {"products": data})


def create_product(req):
    form = ProductForm(req.POST or None)
    if form.is_valid() and req.method == "POST":
        form.save()
        return redirect("main:index")  # Menggunakan nama di urls.py

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
