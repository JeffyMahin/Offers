from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def registration(request):
    current_user = request.user
    # print(groups.filter(user__name = 'current_user'))

    groups = Group.objects.all()
    add_user = UserForm(request.POST or None)
    # import pdb; pdb.set_trace()

    if add_user.is_valid():
        user = User.objects.create(
            username=add_user.cleaned_data.get('username'),
            email=add_user.cleaned_data.get('email'),
            is_staff=add_user.cleaned_data.get('is_staff'),
        )
        user.set_password(add_user.cleaned_data['password'])
        user.save()
        my_group = Group.objects.get(name=add_user.cleaned_data['groups'].first().name)
        my_group.user_set.add(user)
        # print(add_user)
        group_name = add_user.cleaned_data['groups'].first().name
        if add_user.cleaned_data['groups'].first().name == 'Admin':
            return redirect('admin_user_index')
        else:
            return redirect('offer_index')

    context = {
        'add_user': add_user,
        'groups': groups,
        'current_user': current_user
    }

    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
def admin_user_index(request):
    current_user = request.user

    admin_user_index = User.objects.filter(groups__name='Admin')

    context = {
        'admin_user_index': admin_user_index,
        'current_user': current_user

    }

    return render(request, 'registration/admin_user_index.html', context)


#
# def delete_admin(request, id):
#     delete_admin = User.objects.get(id = id)
#
#     print(delete_admin)
#     # delete_admin.delete()
#     return redirect('admin_user_index')


@login_required(login_url='login')
def shopkeeper_user_index(request):
    current_user = request.user

    shopkeeper_user_index = User.objects.filter(groups__name='Shop Keeper')

    context = {
        'shopkeeper_user_index': shopkeeper_user_index,
        'current_user': current_user

    }

    return render(request, 'registration/shopkeeper_user_index.html', context)


def delete_admin(request, id):
    delete_admin = User.objects.get(id=id)

    # print(delete_admin)
    delete_admin.delete()
    return redirect('admin_user_index')
