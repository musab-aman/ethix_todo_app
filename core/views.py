from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo, User

def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            default_user = User.objects.first() 
            Todo.objects.create(title=title, user=default_user)
        return redirect('core:get_todos')
    return render(request, "index.html")

def get_todos(request):
    todos = Todo.objects.all()
    newtodos = []
    for todo in todos:
        newtodos.append(
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "user": todo.user.username,
            }
        )
    print(newtodos)
    return render(request, "index.html", {"todo_lists": newtodos})


def get_todo_by_id(request, todo_id):
    find_todo = Todo.objects.get(pk=todo_id)
    if not find_todo:
        return HttpResponse("Todo not found", status=404)
    return render(request, "detail.html", {"todo": find_todo})


def update_todo(request):
    return HttpResponse("Update a todo")


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id) 
    todo.delete()
    return redirect('core:get_todos') 