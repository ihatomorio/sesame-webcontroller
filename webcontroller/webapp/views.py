from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Sesame


@login_required
def sesame_list(request):
    sesames = Sesame.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'sesame_list.html', {'sesames': sesames})