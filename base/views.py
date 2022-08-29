from re import template
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Note
from .forms import NoteForm, BookForm

#views 
def loginPage(request):
  page = 'login'
  if request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')
   
    try:
        user = User.objects.get(username=username)
    except:
        messages.error(request,'User does not exist')
      
    user = authenticate(request,username=username, password=password)
    
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        messages.error(request,'Username or password is incorrect')
  
  context = {'page':page}
  return render(request,'base/login_register.html',context);


def logoutUser (request):
    logout(request)
    return redirect('home')

def registerPage(request):
  form = UserCreationForm
  if request.user.is_authenticated:
    return redirect('home')
    
  if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          user = form.save(commit=False)
          user.username = user.username.lower()
          user.save()
          login(request,user)
          return redirect('home')
      else:
          messages.error(request,'An error has occurred during registration')
  return render(request,'base/login_register.html',{'form':form})

@login_required(login_url='/login')
def home(request):
  q = request.GET.get('q')if request.GET.get('q')!=None else ''
  user_books = Book.objects.filter(owner = request.user)
  books = user_books.filter(
    Q(topic__icontains=q)|
    Q(name__icontains=q)
  )
  notes = Note.objects.filter(
  Q(book__topic__icontains=q)| 
  Q(book__name__icontains=q)
  ).order_by('-created')[0:5]

  context = {'books':books,'notes':notes}
  return render (request,'base/home.html',context)

@login_required(login_url='/login')
def book(request,pk):
  book = Book.objects.get(id=pk)
  book_notes = book.note_set.all()

  if book.owner != request.user:
    return redirect('home')

  else:
    context={'book':book,'book_notes':book_notes}
    return render(request,'base/book.html',context)

@login_required(login_url='/login')
def note(request,pk):
  note = Note.objects.get(id=pk)
  if note.book.owner != request.user:
    return redirect('home')
  else:
    context = {'note':note}
    return render(request,'base/note.html',context)

@login_required(login_url='/login')
def createBook(request):
  form = BookForm()
  if request.method == 'POST':
    form = BookForm(request.POST)
  if form.is_valid():
    book = form.save(commit=False)
    book.owner = request.user
    book.save()
    return redirect('home')
  context ={'form':form}
  return render(request,'base/create_book.html',context)

@login_required(login_url='/login')
def createNote(request,pk):
  book = Book.objects.get(id=pk)
  form = NoteForm()
  if request.method == 'POST':
    form = NoteForm(request.POST)
  if form.is_valid():
      note = form.save(commit=False)
      note.book = book
      note.owner = request.user
      note.save()
      return redirect('book',pk=book.id)
  context = {'form':form} 
  return render(request,'base/create_note.html',context)

@login_required(login_url='/login')
def deleteBook(request,pk):
  book = Book.objects.get(id=pk)
  if request.method == 'POST':
    book.delete()
    return redirect('home')
  return render(request,'base/delete.html',{'obj':book})

@login_required(login_url='/login')
def deleteNote(request,pk):
  note = Note.objects.get(id=pk)
  if request.method == 'POST':
    note.delete()
    return redirect('book',note.book.id)
  context = {'book':book,'note':note}
  return render(request,'base/delete.html',context)

@login_required(login_url='/login')
def updateBook(request,pk):
  book = Book.objects.get(id=pk)
  form = BookForm(instance=book)
  if request.method =='POST':
    form = BookForm(request.POST,instance=book)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form':form}
  return render(request,'base/create_book.html',context)

@login_required(login_url='/login')
def updateNote(request,pk):
  note = Note.objects.get(id=pk)
  form = NoteForm(instance=note)
  if request.method == 'POST':
    form = NoteForm(request.POST,instance=note)
    if form.is_valid():
      form.save()
      return redirect('book',note.book.id)
  context={'form':form}
  return render(request,'base/create_note.html',context)

