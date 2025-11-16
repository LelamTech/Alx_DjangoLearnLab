# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    class Meta:
        # custom permissions placeholder for Task 4
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} ({self.library.name})"

# Optional: extend User via profile (Task 3 will use this).
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
