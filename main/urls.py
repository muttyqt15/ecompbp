from django.urls import path
from .views import (
    index,
    show_json,
    show_xml,
    show_json_by_id,
    show_xml_by_id,
    create_product,
    register,
    login_user,
    logout_user,
    edit_product,
    delete_product,
    ajax_get_json,
    ajax_get_xml,
    create_ajax
)

app_name = "main"
urlpatterns = [
    path("", index, name="index"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>", show_json_by_id, name="show_json_by_id"),
    path("create/", create_product, name="create_product"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("edit_product/<str:id>/", edit_product, name="edit_product"),
    path("delete_product/<str:id>/", delete_product, name="delete_product"),
    path("ajax-get-json/", ajax_get_json, name="ajax_get_json"),
    path("ajax-get-xml/", ajax_get_xml, name="ajax_get_xml"),
    path("create-ajax/", create_ajax, name="create_ajax"),
]
