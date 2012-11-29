from django.db import models
import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown2 import markdown
    
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
    
    
    class Meta:
        
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']
    
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    
    # link it to corresp author
    
    author = models.ForeignKey(User)
    
    # create entry itself
    
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
    
    categories = models.ManyToManyField(Category)
    
    tags = TagField()
    
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)
    
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.exerpt:
            self.exerpt_html = markdown(self.exerpt)
        super(Entry, self).save(force_insert, force_update)
    
    def unicode(self):
        return self.title
        
    def get_absilute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)