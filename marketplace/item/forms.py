from django import forms

from .models import Items

INPUT_CLASS = "w-full py-4 px-6 rounded-xl border"


class Additem(forms.ModelForm):
    class Meta:
        model = Items
        fields =('category','name','description','price','image',)

        # category = forms.ChoiceField(widget=forms.ChoiceWidget
        widgets = {
            'category': forms.Select(attrs={
                "class": INPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                "class": INPUT_CLASS
            }),
            'description' : forms.TextInput(attrs={
                "class": INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                "class": INPUT_CLASS
            }),
            "image":forms.FileInput(attrs={
                "class": INPUT_CLASS
            }),

        }


class edititem(forms.ModelForm):
    class Meta:
        model = Items
        fields =('name','description','price','image','is_sold')

        # category = forms.ChoiceField(widget=forms.ChoiceWidget
        widgets = {
            'name': forms.TextInput(attrs={
                "class": INPUT_CLASS
            }),
            'description' : forms.TextInput(attrs={
                "class": INPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                "class": INPUT_CLASS
            }),
            "image":forms.FileInput(attrs={
                "class": INPUT_CLASS
            }),

        }