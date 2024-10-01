from django import forms
from counsel.models import Counsel

class CounselForm(forms.ModelForm):
    class Meta:
        model = Counsel
        fields = ['category','description']
