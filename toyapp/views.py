from django.shortcuts import render,redirect
from . models import Reg_tbl,Products_tbl,cart_tbl
from .forms import Regform
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def  index(request):
    return render(request,"index.html")

def  reg(request):
    if request.method=='POST':
        eml = request.POST.get('email')
        pwd = request.POST.get('password')
        rpwd = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('radiogroup1')
        obj = Reg_tbl.objects.create(email=eml,psw=pwd,rpsw=rpwd,fname=fname,lname=lname,gender=gender)
        obj.save()
        if obj:
            return redirect('/login')
        else:
            return render(request,"register.html")

    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        eml = request.POST.get('email')
        psw = request.POST.get('password')
        obj = Reg_tbl.objects.filter(email=eml,psw=psw)
        if obj:
            request.session['ema']=eml
            request.session['psa']=psw
            for i in obj:
                idno=i.id
            request.session['idl']=idno
            return render(request,"home.html")
        else:
            msg = "Invalid credentials!!"
            return render(request,"login.html",{"error":msg})
    return render(request,"login.html")

def users(request):
    obj = Reg_tbl.objects.all()
    return render(request,"users.html",{"users":obj})

def edit(request,pk):
    obj = Reg_tbl.objects.filter(id=pk)
    if request.method =="POST":
        enm = request.POST.get('nm')
        id  = request.POST.get('idl')
        pas = request.POST.get('psw')
        fna = request.POST.get('fnm')
        lna = request.POST.get('lnm')
        gen = request.POST.get('gr')
        obb = Reg_tbl.objects.filter(id=id)
        obb.update(email=enm,psw=pas,fname=fna,lname=lna,gender=gen)
        return redirect('/users')
    return render(request,"user.html",{"user":obj})

def delete(request,pk):
    obj = Reg_tbl.objects.filter(id=pk)
    obj.delete()
    return redirect('/users')

def products(request):
    if request.method=="POST":
        timg = request.FILES.get('tim')
        tnm= request.POST.get('tna')
        tprc = request.POST.get('tpr')
        tdes = request.POST.get('des')
        obj = Products_tbl.objects.create(timg=timg,tname=tnm,tprc=tprc,tdes=tdes)
        obj.save()
        if obj:
            return render(request,"products.html",{"msg":"Details added successfully!!"})
    return render(request,"products.html")

def toy(request):
    obj = Products_tbl.objects.all()
    return render(request,"toy.html",{"toy":obj})

def cart(req,idn):
    pdct = Products_tbl.objects.get(id=idn)
    cid = req.session['idl']
    customer = Reg_tbl.objects.get(id=cid)
    cartitem,created=cart_tbl.objects.get_or_create(product=pdct,customer=customer)
    if not created:
        cartitem.qty+=1
        cartitem.save()  
    messages.success(req,"Item added to cart..")
    return redirect('/toys')

def viewcart(request):
    idl=request.session['idl']
    cobj=Reg_tbl.objects.get(id=idl)
    cartuser=cart_tbl.objects.filter(customer=cobj)
    if cartuser:
        total_price = 0
        for i in cartuser:
            pro_price=i.product.tprc*i.qty
            total_price=total_price+pro_price
        return render(request,"cart.html",{"total":total_price,"cart":cartuser})
    else:
        return render(request,"cart,html",{"info":"Your cart is empty.."})

def cartdelete(request,pid):
    product = cart_tbl.objects.get(id=pid)
    product.delete()
    return redirect('/viewcart')

def email(request):
    if request.method=="POST":
        name = request.POST.get('name')
        to = request.POST.get('email')
        msg = request.POST.get('text')
        send_mail(name,msg,settings.EMAIL_HOST_USER,[to],fail_silently=False)
        return render(request,"email.html",{"success":"Mail Send Successfully"})
    return render(request,"email.html")

def formview(request):
    form = Regform()
    if request.method=="POST":
        form = Regform(request.POST)
        if form.is_valid():
            e = form.cleaned_data.get('email')
            p = form.cleaned_data.get('psw')
            obj = Reg_tbl.objects.create(email=e,psw=p)
            obj.save()
            if obj:
                msg ='Registered'
                return render(request,"forms.html",{"form":form,"success":msg})
    return render(request,"forms.html",{"form":form})