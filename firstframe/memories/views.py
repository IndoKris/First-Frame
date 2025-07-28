from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'memories/home.html')

def about_me(request):
    return render(request, 'memories/about_me.html')

def memories(request):
    return render(request, 'memories/memories.html')

def gallery(request):
    return render(request, 'memories/gallery.html')

def thank_you(request):
    return render(request, 'memories/thank_you.html')
