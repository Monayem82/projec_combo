from django import forms

class makePost(forms.Form):
    title=forms.CharField()
    name=forms.CharField()
    describ=forms.CharField()

class studentDetails(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    dep=forms.CharField(initial="CSE",disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    file=forms.CharField(widget=forms.FileInput)
