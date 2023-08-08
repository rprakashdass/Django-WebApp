from django import forms
from .models import userr

class fromform(forms.ModelForm):
    class Meta:
        model = userr
        fields = ['username','password','email','phoneNo']