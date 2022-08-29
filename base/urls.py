from django.urls import path
from . import views

urlpatterns= [
  path('',views.home,name="home"),
  path('login/',views.loginPage,name="login"),
  path('register/',views.registerPage,name="register"),
  path('logout/',views.logoutUser,name="logout"),
  path('book/<str:pk>/',views.book,name="book"),
  path('note<str:pk>/',views.note,name="note"),
  path('create_book/',views.createBook,name="create_book"),
  path('create_note/<str:pk>',views.createNote,name="create_note"),
  
  path('update_book/<str:pk>',views.updateBook,name="update_book"),
  path('update_note/<str:pk>',views.updateNote,name="update_note"),
  path('delete/<str:pk>',views.deleteBook,name="delete_book"),
  path('delete_note/<str:pk>',views.deleteNote,name="delete_note")
]