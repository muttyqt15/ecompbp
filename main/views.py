from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
@login_required
def create_ajax(request):
    name = strip_tags(request.POST.get("name"))  # strip HTML tags!
    price = strip_tags(request.POST.get("price"))  # strip HTML tags!
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    stock = strip_tags(request.POST.get("stock"))
    rating = strip_tags(request.POST.get("rating"))
    user = request.user

    product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        stock=stock,
        rating=rating,
        user=user,
    )
    product.save()

    return HttpResponse(b"CREATED", status=201)


@login_required
def ajax_get_json(request):
    print(request)
    data = Product.objects.all().filter(user=request.user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


@login_required
def ajax_get_xml(request):
    data = Product.objects.all().filter(user=request.user)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def edit_product(req, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(req.POST or None, instance=product)
    if form.is_valid() and req.method == "POST":
        form.save()
        messages.success(req, "Product updated successfully!")
        return redirect("main:index")

    context = {"form": form}
    return render(req, "edit_product.html", context)


def delete_product(req, id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(req, "Product deleted successfully!")
    return redirect("main:index")


@login_required(login_url="/login/")
def index(req):
    ctx = {
        "user": {"name": req.user, "last_login": req.COOKIES.get("last_login")},
    }
    return render(req, "main.html", ctx)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:index"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("main:login")


def create_product(req):
    form = ProductForm(req.POST or None)
    if form.is_valid() and req.method == "POST":
        product = form.save(commit=False)
        product.user = req.user
        product.save()
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
