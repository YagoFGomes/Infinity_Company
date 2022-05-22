from django.shortcuts import render

# Create your views here.

def HomePage(request):

    context = {}
    return render(request, 'home_page.html', context)