from django.urls import path
from . import views

app_name = 'notepads'
urlpatterns = [
    path('', views.index, name='index'),
    path('notes', views.notes, name='notes'),
    path('note/<int:note_id>', views.note, name='note'),
    path('new_note', views.new_note, name='new_note'),
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
    path('evaluation', views.new_evaluation, name='evaluation')
]
