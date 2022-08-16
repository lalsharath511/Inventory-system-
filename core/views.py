from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from. models import Inventory

# Create your views here.
def log(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        un=request.POST['uname']
        ps=request.POST['pwd']
        user=authenticate(request,username=un,password=ps)

        if user.is_superuser==1:
            return redirect('prolist')
        else:
            return redirect("login")


def inventory(request):
    if request.method=='GET':
        return render(request,"add_product.html")
    elif request.method=="POST":
        pro_name=request.POST['product_name']
        pro_qty=request.POST['product_qty']
        Inventory.objects.create(Product_Name=pro_name,Product_qty=pro_qty)
        return redirect(product_list)

def product_list(request):
    d=Inventory.objects.all()
    return render(request,'admin.html',{'data':d})

def del_product(request,poid):
    Inventory.objects.filter(id=poid).delete()
    return redirect('prolist')

def productedit(request,id):
    product=Inventory.objects.get(id=id)
    return render(request,'porductupdate.html',{'product':product})

def productupdate(request,id):
    if request.method=='POST':
        productqty=request.POST['Product_qty']
        form=Inventory.objects.get(id=id)
        form.Product_qty=productqty
        form.save()
        return redirect(product_list)



