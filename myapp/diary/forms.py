from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '40', 'rows': '5','wrap':"soft", 'max_length': '200'}))

    class Meta:
        model = Diary
        fields = ("user","title","text")

