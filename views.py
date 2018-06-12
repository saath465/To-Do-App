from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def receive(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            todo_items = List.objects.all
            messages.success(request, ('To-Do added to List'))
            return render(request, 'home.html', {'list_items': todo_items})
    else:

        todo_items = List.objects.all
        return render(request, 'home.html', {'list_items': todo_items})

def about_app(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ('To-Do Deleted from List'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.complete = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.complete = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('To-Do edited!!'))
            return redirect('home')
    else:

        items = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'items': items})