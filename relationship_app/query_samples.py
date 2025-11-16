# relationship_app/query_samples.py
import os
import sys
import django

# --- FIX 1: Add project root to Python path ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.insert(0, PROJECT_ROOT)

# --- FIX 2: Correct settings module ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')

django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author named {author_name}")
        return
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for b in books:
        print(f"- {b.title}")


def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named {library_name}")
        return
    print(f"Books in {library.name}:")
    for b in library.books.all():
        print(f"- {b.title} by {b.author.name}")


def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named {library_name}")
        return
    if hasattr(library, 'librarian'):
        print(f"Librarian for {library.name}: {library.librarian.name}")
    else:
        print(f"No librarian assigned for {library.name}")


if __name__ == '__main__':
    query_books_by_author("Jane Austen")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
