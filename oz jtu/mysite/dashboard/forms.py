from django import forms
from univer.models import *


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu()
        fields = "__all__"


class Basic_menuForm(forms.ModelForm):
    class Meta:
        model = Basic_menu()
        fields = "__all__"


