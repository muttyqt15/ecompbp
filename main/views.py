from django.shortcuts import render


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
