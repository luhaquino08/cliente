from django.shortcuts import render, redirect
from django.http import HttpResponse


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from .forms import ClienteForm
from .models import Cliente

# Create your views here.

@login_required
def novo_cliente(request):
    clientes = Cliente.objects.all() # converte em: SELECT * FROM clientes
    template_name = 'novo_cliente.html'
    context = {}
    if request.method == 'POST' :
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')
        else:
            return HttpResponse('<h1>Erro no seu formulário<h1>')

    form = ClienteForm()
    context['form'] = form
    context['clientes'] = clientes

    return render(request, template_name, context)

@login_required
def atualizar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        return HttpResponse('<h1>Cliente não encontrado')
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('novo_cliente')
        else:
            return HttpResponse('<h1>Erro na atualização de cliente</h1>')
        
    form = ClienteForm(instance=cliente)
    template_name = 'novo_cliente.html'
    clientes = Cliente.objects.all()
    context = {
        'form' : form,
        'clientes' : clientes
    }
    return render(request, template_name, context)

@login_required
def excluir_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
    except Cliente.DoesNotExist:
        return HttpResponse('<h1>Erro ao excluir cliente. Cliente não encontrado</h1>')
    return redirect('novo_cliente')

def login_usuario(request):
    template_name = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            passoword = form.cleaned_data.grt('passoword')
            usuario = authenticate(username=username, passoword=passoword)

            if usuario is not None:
                login(request, usuario)
                return redirect('novo_cliente')
            
        else:
            return HttpResponse(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    context = {'form': form}

    return render(request, template_name, context)