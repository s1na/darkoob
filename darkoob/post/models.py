from django.db import models
from darkoob.social.models import User
from darkoob.group.models import Group
from django.utils import timezone  
from djangoratings.fields import RatingField

from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):
    user = models.ForeignKey(User, related_name='post_set', db_index=True)
    text = models.TextField()
    submitted_time = models.DateTimeField(default=timezone.now(), db_index=True)
    noks = RatingField(range=1, can_change_vote=True, allow_delete=True, allow_anonymous=False)

    def __unicode__(self):
        return unicode("user %s"% self.user_id)

class Comment(MPTTModel):
    """ Threaded comments for blog posts """
    post = models.ForeignKey(Post, related_name='comment_set')
    author = models.CharField(max_length=60, db_index=True)
    comment = models.TextField()
    added  = models.DateTimeField(default=timezone.now())
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['added']
