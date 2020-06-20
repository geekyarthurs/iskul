from django import forms
from .models import Content


class ContentCreateForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('topic', 'content_image', 'content_video',
                  'content_paragraph')
