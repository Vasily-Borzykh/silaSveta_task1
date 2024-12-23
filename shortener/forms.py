from django import forms
from .models import ShortenedURL

class URLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите URL для сокращения',
            }),
        }
