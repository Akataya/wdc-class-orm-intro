from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    country_id = models.IntegerField()

    def __str__(self):
        return self.name

    def get_country(self):
        return Country.objects.get(id=self.country_id)

    def get_books(self):
        return Book.objects.filter(author_id=self.id)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_id = models.IntegerField()
    isbn = models.CharField(max_length=255)
    popularity = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return "{}({})".format(self.title, self.popularity)

    def get_author(self):
        return Author.objects.get(id=self.author_id)
