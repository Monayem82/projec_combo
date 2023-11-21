from django import forms

class contactUs(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    father_name=forms.CharField(initial='Father',disabled=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    topic=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    department=forms.CharField(max_length=3,initial='CSE',widget=forms.TextInput(attrs={'class':'form-control'}))
    describe=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    