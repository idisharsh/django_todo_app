from django.shortcuts import render, redirect
from .models import ToDo
from django.http import HttpResponse

def home_page(request):
    todotasks = ToDo.objects.all()
    if request.method == 'POST':
        todo_front_data = request.POST
        description = todo_front_data.get('description')
        ToDo.objects.create(description=description)
        return redirect('home_page')

    context = {'todotasks': todotasks}
    return render(request, 'home_page.html', context)

def mark_complete(request, id):
    todo_backend = ToDo.objects.get(id=id)
    if todo_backend.completed :
        todo_backend.completed = False
    else:
        todo_backend.completed = True
    todo_backend.save()
    return redirect('home_page')