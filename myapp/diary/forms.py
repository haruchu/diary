from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    title=forms.CharField(max_length=15)
    text = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '40', 'rows': '5','wrap':"soft", 'max_length': '250'}))

    class Meta:
        model = Diary
        fields = ("user","title","text")

