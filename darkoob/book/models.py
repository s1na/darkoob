from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from djangoratings.fields import RatingField
from sorl.thumbnail import ImageField

def first_user():
    return User.objects.get(pk=1)

class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    publisher = models.ForeignKey('Publisher',null=True, blank=True)
    language = models.ForeignKey('Language', null=True, blank=True)
    authors = models.ManyToManyField('Author')
    tags = TaggableManager(blank=True)
    pages = models.IntegerField(blank=True, null=True)
    thumb =  models.ImageField(upload_to='books/', default='books/default.jpg')
    rating = RatingField(range=5, can_change_vote=True, allow_delete=False, allow_anonymous=False)
    creation_time = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, default=first_user)
    
    def author_names(self):
        return ', '.join([a.name for a in self.authors.all()])
    author_names.short_description = "Author Names"

    def __unicode__(self):
        return unicode(self.title)

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Language(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Translator(models.Model):
    author = models.OneToOneField(Author)

    def __unicode__(self):
        return unicode(self.author)

class Translation(models.Model):
    book = models.ForeignKey(Book)
    translator = models.ForeignKey(Translator)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return unicode(self.book)

class Review(models.Model):
    book = models.ForeignKey(Book, db_index=True)
    user = models.ForeignKey(User)
    title = models.TextField()
    text = models.TextField()
    submitted_time = models.DateTimeField(default=timezone.now(), db_index=True)
    rating = RatingField(range=5, can_change_vote=True, allow_delete=False, allow_anonymous=False)

    def __unicode__(self):
        return unicode(self.book) + unicode(self.user)

class Quote(models.Model):
    author = models.ForeignKey(Author, null=True, blank=True)
    book = models.ForeignKey(Book, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, db_index=True)
    submitted_time = models.DateTimeField(default=timezone.now(), db_index=True)
    text = models.TextField()

    @classmethod
    def get_random_quote(cls):
        try:
            quote = cls.objects.order_by('?')[0]
        except Exception, e:
            print e
            author= Author.objects.create(name='Albert Einstein')
            u = User.objects.get(pk=1)
            quote = Quote.objects.create(
                author=author,
                user=u,
                text="Two things are infinite: the universe and human stupidity\
                ; and I'm not sure about the universe."
            )

        return quote

    def __unicode__(self):
        return unicode(self.text)

