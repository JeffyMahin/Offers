from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from feedback.models import Feedback
from .forms import OfferDetailForm
from .models import OfferDetail
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def add(request):
    current_user = request.user

    offer_data = OfferDetailForm(request.POST, request.FILES)
    # import pdb;pdb.set_trace()

    if offer_data.is_valid():
        print('Mahin')
        offer_data.save()
        return redirect('offer_pending')

    context = {
        'offer_data': offer_data,
        'current_user': current_user
    }

    return render(request, 'offer/add.html', context)


@login_required(login_url='login')
def offer_pending(request):
    current_user = request.user

    pending_offer_index = OfferDetail.objects.filter(status=0).all()

    context = {
        'pending_offer_index': pending_offer_index,
        'current_user': current_user
    }

    return render(request, 'offer/pending_offers.html', context)


def index(request):
    offer_index = OfferDetail.objects.filter(status=1).all()

    context = {
        'offer_index': offer_index
    }

    return render(request, 'offer/index.html', context)


def offer_detail_view(request, id):
    current_user = request.user
    offer_detail = OfferDetail.objects.get(id=id)

    if request.method == 'POST':
        feedback_data = request.POST.get('feedback_val')
        Feedback.objects.create(
            offer_id_id=id,
            feedback=feedback_data
        )

    context = {
        'offer_detail': offer_detail,
        'current_user': current_user
    }

    return render(request, 'offer/offer_detail.html', context)


def edit_offer(request, id):
    current_user = request.user
    edit_offer = OfferDetailForm(request.POST)

    if edit_offer.is_valid():
        edit_offer.save()
        return redirect('offer_index')

    context = {
        'edit_offer': edit_offer,
        'current_user': current_user
    }

    return render(request, 'offer/edit.html', context)


@login_required(login_url='login')
def accept_offer(request, offer_id):
    offer_detail = OfferDetail.objects.get(id=offer_id)
    offer_detail.status = 1
    offer_detail.save()
    return redirect('offer_index')


@login_required(login_url='login')
def delete_offer(request, offer_id):
    offer_detail = OfferDetail.objects.get(id=offer_id)
    offer_detail.delete()
    return redirect('offer_pending')


def delete_detail_offer(request, id):
    # current_user = request.user
    # print(current_user)
    # print(current_user.cleaned_data['groups'].first().name)
    # delete_offer = OfferDetail.objects.get(id = id)
    # # delete_offer.delete()

    # return HttpResponseNotFound("Deleting offer provision is not allowed")
    # messages.info(request, "You can't delete here")
    return redirect('offer_index')
