from django.forms import ModelForm
from .models import Note, Book

#forms
class NoteForm(ModelForm):
  class Meta:
    model = Note
    fields = '__all__'
    exclude = ['book','user']

class BookForm(ModelForm):
  class Meta:
    model = Book  
    fields = '__all__'
    exclude = ['owner']