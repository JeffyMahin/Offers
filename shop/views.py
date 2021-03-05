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
