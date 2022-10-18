import imp
from django.shortcuts import render,redirect
from . models import Contact, Product,CustomerServices,Catagry
from . forms import ContactModelForm,CreatUserForm,UserUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def base(request):
    return render(request,'index.html') 

def about(request):
    return render(request,'about.html') 

def contact(request):
    if request.method == "POST":
        frm = ContactModelForm(request.POST)
        if frm.is_valid():
            frm.save()
            frm = ContactModelForm()
    else :
        frm = ContactModelForm()
        data = Contact.objects.all()
    return render(request,'contact.html',{'form' : frm}) 

def gallery(request):
    return render(request,'gallery.html') 

def product(request):
    cata=Catagry.objects.all()
    read = Product.objects.all()
    return render(request,'products.html',{"data" : read,"cata":cata})
# def products(request,id):
    
#     # file = Product.objects.filter(catagry= id) 
#     return render(request,'products.html',{ "cata":cata}) 

def services(request):

    read = Product.objects.all()
    find = CustomerServices.objects.all()
    return render(request,'services.html',{"data" : read , "kam" : find}) 

def show (request):
    return render(request , 'show.html')

def register (request):
    frm = CreatUserForm()

    if request.method == 'POST':
        frm = CreatUserForm(request.POST)
        if frm.is_valid():
            frm.save()
            user = frm.cleaned_data.get('username')
            messages.success(request,'Account is created for '+ user)
            return redirect('/about')

    return render (request , 'signUp.html',{'form':frm})

def read (request):
    read = User.objects.all()
    return render(request,'read.html',{'data':read})

def update(request,id):
    var = User.objects.get(id = id)
    frm = UserUpdateForm(request.POST or None, instance = var)
    if frm.is_valid():
        frm.save()
        return redirect('/read')
    data = User.objects.all()
    return render (request, 'update.html' , {"form" : frm  , "data" : data})

def delete(request,id):
    var = User.objects.get(id = id)
    frm = CreatUserForm(request.POST or None, instance = var)
    if frm.is_valid():
       var.delete()
       return redirect ('/read')
    data = User.objects.all()
    return render(request, 'delete.html' , {"form" : frm , "data" : data}) 

def products_filter(request,id):
    # catagry = request.GET.get('catagry')
    file = Product.objects.filter(catagry= id) 
    return render(request,'show.html',{ "kam" : file}) 