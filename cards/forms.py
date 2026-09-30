# from django import forms
# from .models import ECard


# class ECardForm(forms.ModelForm):

#     class Meta:
#         model = ECard

#         fields = [
#             'title',
#             'category',
#             'description',
#             'image',
#             'price',
#         ]

#         widgets = {

#             'title': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Enter card title'
#                 }
#             ),

#             'description': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Enter card description'
#                 }
#             ),

#             'price': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Enter price'
#                 }
#             ),
#         }


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import ECard


class ECardForm(forms.ModelForm):

    class Meta:
        model = ECard

        fields = [
            'title',
            'category',
            'description',
            'image',
            'price'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter card title'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter card description'
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter price'
                }
            ),
        }


class SignupForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }
        )
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]