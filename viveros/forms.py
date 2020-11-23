from django.forms import ModelForm
from viveros.models import Productor


# Create the form class.
class ProductorForm(ModelForm):
    class Meta:
        model = Productor
        fields = '__all__'

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    surname = forms.CharField(max_length=20)

    class Meta:
        fields = ('username','email','surname','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['surname'].label = 'Surname'
        self.fields['email'].label = 'Email Address'


