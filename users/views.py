from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            messages.error(request, 'Você já usou este e-mail. Mude para login ou digite um novo endereço de e-mail')
            return render(request, 'signup.html')

        return render(request, 'painel.html') 

def login(request):
    return render(request, 'login.html')