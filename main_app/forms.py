from django import forms
from .models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'notes', 'mood', 'chapter', 'page']
        
class JournalAllForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'notes', 'mood', 'chapter', 'page', 'book']