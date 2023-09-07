from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Items
from .forms import Additem,edititem

# Create your views here.


# from .tasks import add
# result = add.apply_async((2, 3), countdown=5) 
# print ("result",result)


def  detail(request,pk):
    item = get_object_or_404(Items,pk=pk)
    remaining_items = Items.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)
    print("remaining items",remaining_items)
    return render(request,'item/detail.html',{
        'item':item,
        'remaining_items':remaining_items,
        })



@login_required
def NewItem(request):
    if request.method == "POST":
        form = Additem(request.POST,request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail",pk=item.id)
        
    else:
        form =Additem()


    return render(request,"item/form.html",{
        'form':form,
        'title':"New Item",
    })

@login_required
def delete(request,pk):

    item = get_object_or_404(Items, pk=pk,created_by=request.user)
    item.delete()

    return redirect("dashboard:index")

@login_required
def EditItem(request,pk):
    item = get_object_or_404(Items, pk=pk,created_by=request.user)

    if request.method == "POST":
        print("in if")
        form = edititem(request.POST,request.FILES,instance=item)

        if form.is_valid():

            form.save()

            return redirect("item:detail",pk=item.id)
        
    else:
        print("in else")
        form =edititem(instance=item)


    return render(request,"item/form.html",{
        'form':form,
        'title':"Edit Item",
    })

