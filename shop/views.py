from django.shortcuts import render, redirect
from .forms import ShopDetailForm
from .models import ShopDetail
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def add(request):
    shop_data = ShopDetailForm(request.POST or None)

    if shop_data.is_valid():
        shop_data.save()
        return redirect('shop_index')

    context = {
        'shop_data': shop_data
    }
    return render(request, 'shop/add.html', context)


@login_required(login_url='login')
def index(request):
    shop_data = ShopDetail.objects.all()

    context = {
        'shop_data': shop_data
    }
    return render(request, 'shop/index.html', context)


def edit(request, id):
    current_user = request.user

    edit_shop = ShopDetailForm(request.POST)

    if edit_shop.is_valid():
        edit_shop.save()
        return redirect('shop_index')

    context = {
        'edit_shop': edit_shop,
        'current_user': current_user
    }

    return render(request, 'shop/edit.html', context)


def delete(request, id):
    print(id)

    delete_shop = ShopDetail.objects.get(id=id)
    print(delete_shop)

    delete_shop.delete()
    return redirect('shop_index')
