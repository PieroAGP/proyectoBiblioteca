from django.shortcuts import render,redirect
from .models import Book
from django.views import View
from .forms import BookForm
# Create your views here.


class BookList(View):
    books= Book.objects.all()
    template_name='book/bookList.html'

    def actualizaTask(self):
        self.books = Book.objects.all()
        return self.books

    def get(self,request):
        return render(request,self.template_name,{'books': self.actualizaTask()})

class NewBook(View):
    books= Book.objects.all()
    template_name='book/newBook.html'

    def actualizaTask(self):
        self.books = Book.objects.all()
        return self.books

    def get(self,request):
        form = BookForm()
        return render(request,self.template_name,{'books':self.actualizaTask(),'form':form})
    
    def post(self,request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listBook')
        return render(request,self.template_name,{'books': self.actualizaTask(),'form':form})

    
