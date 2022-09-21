
from django import forms
from curd.models import User

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
             'uemail':forms.EmailInput(attrs={'class':'form-control'}),
              'upassword':forms.TextInput(attrs={'class':'form-control'}),
             
        }
