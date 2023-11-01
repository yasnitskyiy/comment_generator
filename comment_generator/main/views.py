from django.shortcuts import render


def main_page_handler(request):
    return render(request, 'index.html')
