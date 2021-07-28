from django import forms
from .models import Users

#create a ModelForm
class UsersForm(forms.ModelForm):
    # specify the name of the model to use
    class Meta:
        model = Users
        # specify model fields to be included in the form. This indicates all of them
        fields = "__all__"