from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Sesame
from .forms import SesameForm


@login_required
def sesame_list(request):
    sesames = Sesame.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'sesame_list.html', {'sesames': sesames})


@login_required
def sesame_new(request):
    if request.method == "POST":
        forms = SesameForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data

            Sesame.objects.create(
                owner = request.user,
                name = cd['name'],
                auth_token = cd['auth_token'],
            )

            return redirect('/')
    else:
        forms = SesameForm()
    return render(request, 'sesame_new.html', {'forms': forms})