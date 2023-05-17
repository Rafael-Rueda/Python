from django.shortcuts import render


def Home(request):
    return render(request = request, template_name= 'home.html')