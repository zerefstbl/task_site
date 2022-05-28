from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import RegisterTask
from .models import Tarefas
from django.contrib import messages


def lista(request):

    search = request.GET.get('search')

    if search:
        tasks = Tarefas.objects.filter(tarefa__icontains=search)

    else:

        tasks = Tarefas.objects.all()

        form = RegisterTask()

    form = RegisterTask()

    return render(request, 'index.html', {'form': form, 'tasks': tasks})


def delete_task(request, id):
    task = get_object_or_404(Tarefas, pk=id)
    task.delete()
    messages.success(
        request,
        'Tarefa Apagada com Sucesso'
    )

    return redirect('/')


def save_task(request):
    if request.method == 'POST':
        form = RegisterTask(request.POST)
        categoria = form.data['categoria']
        print(categoria)
        form.save()

        return redirect('/')
    return HttpResponse('teste')


def details_task(request, id):
    task = get_object_or_404(Tarefas, pk=id)

    return render(request, 'detalhes.html', {'task': task})


def edit_task(request, id):
    task = get_object_or_404(Tarefas, pk=id)
    print(task)
    form = RegisterTask(instance=task)

    if request.method == "POST":
        form = RegisterTask(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return HttpResponse('TESTE')
    else:
        return render(request, 'edit.html', {'form': form, 'task': task})

    return render(request, 'edit.html', {'form': form, 'task': task})
