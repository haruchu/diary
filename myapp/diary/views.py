from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import DiaryForm
from .models import Diary
from django.utils import timezone
import datetime
from .helpers import get_current_user


@login_required
def new_diary(request):
    current_user = get_current_user(request)
    initial_dict = {'user': request.user,'month':datetime.datetime.now().month}
    form = DiaryForm(request.POST or None, initial=initial_dict)
    context = {
        "user": request.user,
        "form": form,
        "diarys": Diary.objects.order_by('-created_date').all(),
    }
    return render(request, 'new_diary.html', context)

@login_required
def create_diary(request):
    form = DiaryForm(request.POST)
    if form.is_valid():
        form = DiaryForm(request.POST)
        diary = form.save(commit=False)
        diary.user = request.user
        diary = form.save()
        return redirect('/home')
    return render(request, 'home.html', {'form': form})


@login_required
def delete(request, diary_id):
    diary = Diary.objects.get(pk=diary_id)
    diary.delete()
    return redirect('/home')


@login_required
def diary(request, diary_id):
    context ={
        'diary': Diary.objects.get(pk=diary_id),
    }
    return render(request, 'diary.html', context)

@login_required
def diary_month(request, month):
    context ={
        'diarys': Diary.objects.filter(month=month).order_by('created_date'),
        'month':month,
    }
    return render(request, 'diary_month.html', context)

