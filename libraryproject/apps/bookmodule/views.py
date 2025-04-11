from django.shortcuts import render
from apps.bookmodule.models import Book
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.urls import reverse
from .forms import BookForm


def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return HttpResponseRedirect(reverse('lab9_part1.listbooks'))
    return render(request, 'bookmodule/add_book.html')

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return HttpResponseRedirect(reverse('lab9_part1.listbooks'))
    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('lab9_part1.listbooks'))



def list_books_with_forms(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})

def add_book_with_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab9_part2.listbooks'))
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book.html', {'form': form})

def edit_book_with_form(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lab9_part2.listbooks'))
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_book.html', {'form': form})

def delete_book_with_form(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('lab9_part2.listbooks'))


def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_page(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_page(request):
    return render(request, 'bookmodule/text_formatting.html')


def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search_books(request):
    
    if request.method == "POST":
            string = request.POST.get('keyword').lower()
            isTitle = request.POST.get('option1')
            isAuthor = request.POST.get('option2')
            # now filter
            books = __getBooksList()
            newBooks = []
            for item in books:
                contained = False
                if isTitle and string in item['title'].lower(): contained = True
                if not contained and isAuthor and string in item['author'].lower():contained = True
                
                if contained: newBooks.append(item)
            return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    
    return render(request, 'bookmodule/search.html')


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='jux') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks=Book.objects.filter(author__isnull = False).filter(title__icontains='j').filter(edition__gte = 2).exclude(price__lte = 100)
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})


def task3(request):
    books = Book.objects.exclude(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})



def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/stats.html', {'stats': stats})
