from django.shortcuts import render
from testapp.models import Book
from testapp.forms import Bookform
# Create your views here.


def index_view(request):
    return render(request,'testapp/index.html')

def Book_View(request):
    form=Bookform()
    if request.method=="POST":
        form=Bookform(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/addbook.html',{'form':form})

def list_book_view(request):
    books_list=Book.objects.all().order_by()
    return render(request,'testapp/listbook.html',{'books_list':books_list})
            
            
