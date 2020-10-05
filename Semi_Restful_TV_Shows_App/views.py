from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def redirectreq(request):
    return redirect('/shows')

    
def index(request):
    #return render(request, "shows.html",{"shows": Show.objects.all()})
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)
    

def new_show(request):
    return render(request,'new.html')


def create_show(request):
    
    errors = Show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
        )
    return redirect('/shows')

def display_show(request, show_id):

    context = {
    'one_show':  Show.objects.get(id=show_id)
    }
    return render(request,'show.html',context)
    

def edit(request, show_id):

    context = {
    'show':  Show.objects.get(id=show_id)
    }
    return render(request,'edit.html',context)

def update(request, show_id):
    # update show!
    to_update = Show.objects.get(id=show_id)
    # updates each field
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['releasedate']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/shows/')


def delete(request, show_id):
    print(request.POST)
    print(show_id)
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')



         
    