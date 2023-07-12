from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):  

    class Meta:
        model = Comment
        fields = ('text', 'rating',)
        labels = {
            'text': 'Текст комментария',
            'rating': 'Оценка (0-10)',
        }