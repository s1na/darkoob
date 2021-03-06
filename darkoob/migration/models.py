from django.db import models
from django.contrib.auth.models import User
from darkoob.book.models import Book

class Hop(models.Model):
    migration = models.ForeignKey('Migration')
    host = models.ForeignKey(User, related_name='host_set', db_index=True)
    received_time = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        unique_together = (("migration", "host"),)

    def __unicode__(self):
        return unicode("%s - %s" % (self.migration, self.host.username))

class Migration(models.Model):
    book = models.ForeignKey(Book, related_name='book_set')
    starter = models.ForeignKey(User, related_name='starter_set')
    starter_message = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True, db_index=True)
    private_key = models.CharField(max_length=10, unique=True)
 
    def get_user_hoped_migrations(self, user):
        '''return all migration's objects that hoped in user'''
        return [hop.migration for hop in Hop.objects.filter(host=user)]

    def get_user_host_migrations(self, user):
        '''return all migration's objects that hosted by user'''
        return [migrate for migrate in Migration.objects.filter(starter=user)]

    def get_user_related_migrations(self, user):
        '''return get_user_host_migrations() +  get_user_hoped_migrations()'''
        return self.get_user_hoped_migrations(user) + self.get_user_host_migrations(user)

    def __unicode__(self):
        return unicode("%s - %s" % (self.book.title, self.starter.username))