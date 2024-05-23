from django.shortcuts import render

def about(request):
    return render(request, 'filter_app/about.html')

def contact(request):
    return render(request, 'filter_app/contact.html')

def methods(request):
    return render(request, 'filter_app/methods.html')