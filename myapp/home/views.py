from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from diary.forms import DiaryForm
from diary.models import Diary


@login_required
def home(request):
    context = {
        "user": request.user,
        "diarys": Diary.objects.filter(user=request.user).order_by('-created_date').all(),
    }
    return render(request, 'home.html', context)
