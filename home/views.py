from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')
def contact(request):
    return render(request, 'home/contact.html') 
def about(request):
    return render(request, 'home/about.html') 
def programs(request):
    return render(request, 'home/programs.html')
def admission(request):
    return render(request, "home/admission.html")