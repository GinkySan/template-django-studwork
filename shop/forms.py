from django import forms
from .models import CustomUser, Product


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'role', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'article', 'description', 'price', 'image']
