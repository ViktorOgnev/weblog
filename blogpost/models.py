from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.username
        
class Post(models.Model):
    user = models.ForeignKey(User)
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    post_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)
        
    def __unicode__(self):
        return self.post_title
    