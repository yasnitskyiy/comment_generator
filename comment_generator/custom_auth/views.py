from django.shortcuts import render


def custom_login_page_handler(request):
    return render(request, 'login.html')


def custom_register_page_handler(request):
    return render(request, 'register.html')
