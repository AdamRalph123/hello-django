from django.shortcuts import render
from .models import Item
from .forms import Itemform


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html')

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    form = Itemform()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
    