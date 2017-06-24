from django.shortcuts import render

from .models import Book

def index(request):
    # Book.objects.create(title="Who moved my cheed?", author="Somebody", published_date=1999/4/14, category="Scary")
    # Book.objects.create(title="To kill a mocking bird", author="Somebody", published_date=1999/1/10, category="Scary")
    # Book.objects.create(title="The Great Gatsby", author="Somebody", published_date=2000/5/11, category="Scary")
    # Book.objects.create(title="All quiet on the western front", author="Somebody", published_date=2001/6/11, category="Scary")
    # Book.objects.create(title="Java", author="Somebody", published_date=2004/6/23, category="Scary")
    book = Book.objects.all()
    print book
    for allbook in book:
        print allbook.title
        print allbook.author
        print allbook.published_date
        print allbook.category
    return render(request, 'books_app/index.html')

# Create your views here.
