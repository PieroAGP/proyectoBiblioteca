from django.shortcuts import render,redirect, get_object_or_404
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

class DetailBook(View):
    def get(self, request, pk):
        book = get_object_or_404(Book,pk=pk)
        return render(request,'book/detailBook.html',{'book':book})
    
class EditBook(View):
    def get(self,request,pk):
        book= get_object_or_404(Book, pk=pk)
        form=BookForm(instance=book)
        return render(request,'book/editBook.html',{'book':book, 'form':form})
    
    def post(self,request,pk):
        book= get_object_or_404(Book, pk=pk)
        form=BookForm(request.POST, instance=book)
        if form.is_valid():
            book=form.save(commit=False)
            form.save()
            return redirect('detailBook', pk=pk)
        return render(request,'book/editBook.html',{'book':book, 'form':form})
