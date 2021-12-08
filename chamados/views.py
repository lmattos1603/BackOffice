from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ChamadoForm, SetorForm
from .models import Chamado, Setor

# CHAMADOS *****************************************************************************

@login_required(login_url='/users/login')
def list_chamados(request):
    chamados = Chamado.objects.all()
    return render(request, 'chamados.html', {'chamados': chamados})

@login_required(login_url='/users/login')
def create_chamados(request):
   users = User.objects.all()
   setores = Setor.objects.all()
   form = ChamadoForm(request.POST or None, request.FILES)

   if form.is_valid():

    form.save()
    return redirect('list_chamados')

   return render(request, 'chamados-form.html', {'form': form, 'users': users, 'setores': setores})

@login_required(login_url='/users/login')
def update_chamados(request, id):
    chamado = Chamado.objects.get(id=id)
    users = User.objects.all()
    setores = Setor.objects.all()
    form = ChamadoForm(request.POST or None, request.FILES, instance=chamado)

    if form.is_valid():
        form.save()
        return redirect('list_chamados')

    return render(request, 'chamados-form.html', {'form': form, 'chamado': chamado, 'users': users, 'setores': setores})

@login_required(login_url='/users/login')
def delete_chamados(request, id):
    chamado = Chamado.objects.get(id=id)

    if request.method == 'POST':
        chamado.delete()
        return redirect('list_chamados')

    return render(request, 'delete-confirm.html', {'chamado': chamado})


# SETORES *****************************************************************************

@login_required(login_url='/users/login')
def list_setores(request):
    setores = Setor.objects.all()
    return render(request, 'setores.html', {'setores': setores})

@login_required(login_url='/users/login')
def create_setor(request):
    form = SetorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_setores')

    return render(request, 'setor-form.html', {'form': form})

@login_required(login_url='/users/login')
def update_setor(request, id):
    setor = Setor.objects.get(id=id)
    form = SetorForm(request.POST or None, instance=setor)

    if form.is_valid():
        form.save()
        return redirect('list_setores')

    return render(request, 'setor-form.html', {'form': form, 'setor': setor})

@login_required(login_url='/users/login')
def delete_setor(request, id):
    setor = Setor.objects.get(id=id)

    if request.method == 'POST':
        setor.delete()
        return redirect('list_setores')

    return render(request, 'delete-setor-confirm.html', {'setor': setor})

# USUÁRIOS *****************************************************************************

def login_user(request):
    return render(request, 'login.html')

def submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/list')
        else:
            messages.error(request, 'Erro! Usuário ou senha inválidos.')
    return redirect('/users/login')

@login_required(login_url='/users/login')
def logout_user(request):
    logout(request)
    return redirect('/users/login')

@login_required(login_url='/users/login')
def alterar_senha(request, id):
    if request.method == 'POST':
        novasenha = request.POST.get('newpass')

        user = User.objects.get(id=id)
        user.set_password(novasenha)
        user.save()
        messages.success(request,'Senha alterada com sucesso!')

    else:
        return render(request, 'password-form.html')

    return redirect('/users/logout')
