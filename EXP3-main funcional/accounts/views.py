from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Reemplaza 'index' con el nombre de tu vista de inicio
        else:
            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
    else:
        error_message = None
    return render(request, 'core/login.html', {'error_message': error_message})

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('index')