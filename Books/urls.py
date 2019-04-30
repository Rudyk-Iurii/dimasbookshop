from django.urls import path
from .views import (
    home,
    book_add,
    book_detail,
    book_edit,
    book_delete,
    payment_method,
    book_migrate,
    contact_form,
    privacy_policy,
    thanks

)

urlpatterns = [
    path('', home, name='home'),
    path('add', book_add, name='book_add'),
    path('contact_form', contact_form, name='contact_form'),
    path('privacy_policy', privacy_policy, name='privacy_policy'),
    path('thanks', thanks, name='thanks'),
    path('book_migrate', book_migrate, name='book_migrate'),
    path('payment_method', payment_method, name='payment_method'),
    path('book/<id>/', book_detail, name='book_detail'),
    path('book/<id>/edit', book_edit, name='book_edit'),
    path('book/<id>/delete', book_delete, name='book_delete'),
]
