from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import DiaryForm
from .models import Diary
from .helpers import get_current_user


@login_required
def new_diary(request):
    current_user = get_current_user(request)
    initial_dict = {'user': request.user}
    form = DiaryForm(request.POST or None, initial=initial_dict)
    context = {
        "user": request.user,
        "current_user": current_user,
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
