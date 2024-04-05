from django import forms
from .models import Item

inputClass='form-control'
class NewItemForm(forms.ModelForm):
  class Meta:
    model=Item
    fields=('category','name','description','price','image')
    widgets={
      'category':forms.Select(attrs={
        'class':'form-select'
      }),
      'name':forms.TextInput(attrs={
        'class':inputClass
      }),
      'description':forms.Textarea(attrs={
        'class':inputClass
      }),
      'price':forms.TextInput(attrs={
        'class':inputClass
      }),
      'image':forms.FileInput(attrs={
        'class':inputClass
      })
    }

class EditItemForm(forms.ModelForm):
  class Meta:
    model=Item
    fields=('name','description','price','image','is_sold')
    widgets={
      'name':forms.TextInput(attrs={
        'class':inputClass
      }),
      'description':forms.Textarea(attrs={
        'class':inputClass
      }),
      'price':forms.TextInput(attrs={
        'class':inputClass
      }),
      'image':forms.FileInput(attrs={
        'class':inputClass
      })
    }