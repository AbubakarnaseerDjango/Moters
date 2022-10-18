from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('',views.base),
    path('about',views.about),
    path('contact',views.contact),
    path('gallery',views.gallery),
    path('product',views.product),
    path('products/<int:id>',views.products_filter),
    path('services',views.services),
    path('show',views.show),
    path('sign',views.register),
    path('read',views.read),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),

    path('reset_password',auth_views.PasswordResetView.as_view(), name = "reset_password"),

    path('reset_done',auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),

    path('reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name  = "password_reset_confirm"),

    path('reset_complete',auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),

]