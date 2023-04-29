from django import forms
from .models import Note, Evaluation


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        labels = {'title': 'Title:', 'text': 'Text:'}


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['text']
        labels = {'text': 'Text:'}
