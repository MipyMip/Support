from django import forms

class UserForm(forms.Form):
    theme = forms.CharField(label="Тема")
    problem = forms.CharField(label="Описание проблемы", widget=forms.Textarea)
