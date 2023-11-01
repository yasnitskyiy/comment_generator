from django.contrib import admin
from django.urls import path, include
from main import views as main
from custom_auth import views as custom_auth
# from custom_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.main_page_handler),
    path('login/', custom_auth.custom_login_page_handler),
    path('register/', custom_auth.custom_register_page_handler),
]
