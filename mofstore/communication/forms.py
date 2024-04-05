from django import forms
from .models import CommunicationMessage

class CommunicationMessageForm(forms.ModelForm):
  class Meta:
    model=CommunicationMessage
    fields=('content',)
    widgets={
      'content':forms.Textarea(attrs={
        'class':'form-control rounded'
      })
    }