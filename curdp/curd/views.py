
from django.shortcuts import render,redirect
from curd.fome import Userform
from django.http import HttpResponse
from curd.models import User

def insert(request):
    if request.method=="POST":
        form=Userform(request.POST)
        if form.is_valid:
            try:
                form.save()
                return HttpResponse("<h1>data sent to database</h1>")
            except:
               pass
    form=Userform()
    return render(request,'index.html',{'form':form})

def show(request):
    users=User.objects.all()
    return render(request,'show.html',{'users':users})    

    
def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    user=User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})

def update(request,id):
    user=User.objects.get(id=id)
    form=Userform(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'user':user})    

