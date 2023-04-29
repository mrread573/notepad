from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Note, Evaluation
from .forms import NoteForm, EvaluationForm


def index(request):
    evaluations = Evaluation.objects.order_by('-date_added')
    context = {'evaluations': evaluations}
    return render(request, 'notepads/index.html', context)


@login_required
def notes(request):
    _notes = Note.objects.filter(owner=request.user).order_by('-date_added')
    context = {'notes': _notes}
    return render(request, 'notepads/notes.html', context)


@login_required
def note(request, note_id):
    _note = get_object_or_404(Note, id=note_id)
    context = {'note': _note}
    return render(request, 'notepads/note.html', context)


@login_required
def new_note(request):
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)

        if form.is_valid():
            _note = form.save(commit=False)
            _note.owner = request.user
            _note.save()
            return redirect('notepads:notes')

    context = {'form': form}
    return render(request, 'notepads/new_note.html', context)


@login_required
def edit_note(request, note_id):
    _note = get_object_or_404(Note, id=note_id)
    if _note.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = NoteForm(instance=_note)
    else:
        form = NoteForm(instance=_note, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('notepads:note', note_id=note_id)

    context = {'form': form, 'note': _note}
    return render(request, 'notepads/edit_note.html', context)


@login_required
def new_evaluation(request):
    if request.method != 'POST':
        form = EvaluationForm()
    else:
        form = EvaluationForm(data=request.POST)

        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.owner = request.user
            evaluation.save()
            return redirect('notepads:index')

    context = {'form': form}
    return render(request, 'notepads/new_evaluation.html', context)
