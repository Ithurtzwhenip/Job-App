from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name':_('Enter First Name'),
            'last_name':_('Enter Last Name'),
            'email':_('Enter Email')
        }
        help_texts = {'first_name':_("Enter characters only")}
        error_messages = {
            'first_name':{
                'required':_('You must enter a first name')
            }
        }

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid Name")
#     return value
#
#
# class SubscribeForm(forms.ModelForm):
#     class Meta:
#
#
#     # first_name = forms.CharField(max_length=100, required=False, label="Enter first name",
#     #                              )
#     # last_name = forms.CharField(max_length=100, disabled=False, validators=[validate_comma])
#     # email = forms.EmailField(max_length=100)
