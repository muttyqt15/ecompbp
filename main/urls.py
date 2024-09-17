from django.urls import path
from .views import (
    index,
    show_json,
    show_xml,
    show_json_by_id,
    show_xml_by_id,
    create_product,
    show_products,
)

app_name = "main"
urlpatterns = [
    path("", index, name="index"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>", show_json_by_id, name="show_json_by_id"),
    path("create/", create_product, name="create_product"),
    path("products/", show_products, name="show_products"),
]
