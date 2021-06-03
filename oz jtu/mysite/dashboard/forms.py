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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact()
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = "__all__"


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher()
        fields = "__all__"
