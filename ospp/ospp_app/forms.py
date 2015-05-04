from django import forms
from django.contrib.auth.models import User
from ospp_app.models import Project, Comment


class CreateUserForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        max_length=20, 
        error_messages={'required': 'Введите ваш логин!'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Логин'
            }
        )
    )
    email = forms.EmailField(
        error_messages={'required': 'Введите email!'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'E-mail'
            }
        )
    )
    password = forms.CharField(
        max_length=20, 
        error_messages={'required': 'Введите пароль!'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Пароль'
            }
        )
    )

    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()  # individual field's clean methods have already been called
        password = cleaned_data.get("password")
        return cleaned_data

    class Meta:
        model = User



class EditUserForm(forms.Form):
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'E-mail'
            }
        )
    )
    first_name = forms.CharField(
        required=False,
        label='First name',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Имя',
            }
        )
    )
    last_name = forms.CharField(
        required=False,
        label='Last name',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Фамилия'
            }
        )
    )

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()

    class Meta:
        model = User