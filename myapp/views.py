from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'bases.html')

def view(request):
    return render(request, 'view.html')