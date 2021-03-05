from django.shortcuts import render, redirect


def home(request):
    return redirect('offer_index')
    # return render(request, 'home/home.html')
