from django.db import models
import datetime
form django.contrib.auth.models import User
    
class Category(models.Model):
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
        
    
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True, help_text=""" Suggested value automatically 
                                        generated from title. Must be unique.""")
    description = models.TextField()
    
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

    def __unicode__(self):
        return self.title

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3

    author = models.ForeignKey(User)
    
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)