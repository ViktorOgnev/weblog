from django.db import models
from pygments import formatters, highlight, lexers
from tagging.fields import TagField
from django.contrib.auth.models import User
from markdown import markdown
import datetime
from cab import managers


class Language(models.Model):

    objects = managers.LanguageManager()
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    language_code = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)
    
    
    class Meta:
        ordering = ['name']
        
    
    def __unicode__(self):
        return self.name
        
    @models.permalink    
    def get_absolute_url(self):
        return('cab_language_detail', (), {'slug': self.slug})
    
    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)

class Snippet(models.Model):  
    
    objects = managers.SnippetManager()
    
    title = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    code = models.TextField()
    highlighted_code = models.TextField(editable=False)
    tags = TagField()
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    
    
    class Meta:
        ordering = ['-pub_date']
    
    
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.description_html = markdown(self.description)
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(force_insert, force_update, *args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('cab_snippet_detail', (), {'pk': self.id})
        
    def highlight(self):    
        return highlight(self.code,
                         self.language.get_lexer(),
                         formatters.HtmlFormatter(linenos=True))
                         
    
        
        
        
class Bookmark(models.Model):
    snippet = models.ForeignKey(Snippet)
    user = models.ForeignKey(User, related_name='cab_bookmarks')
    date = models.DateTimeField()
    
    class Meta:
        ordering = ['-date']
        
    def __unicode__(self):
        return " %s bookmarked by %s" % (self.snippet, self.user)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Bookmark, self).save(*args, **kwargs)
        
    
class Rating(models.Model):
        RATING_UP = 1
        RATING_DOWN = -1
        RATING_CHOICES = ((RATING_UP, 'useful'), (RATING_DOWN, 'not useful'))
        
        snippet = models.ForeignKey(Snippet)
        user = models.ForeignKey(User, related_name='cab_rating')
        rating = models.IntegerField(choices=RATING_CHOICES)
        date = models.DateTimeField()
        
        def __unicode__(self):
            return "%s rating %s (%s)" % (self.user, self.snippet,
                                          self.get_rating_display())
        
        def save(self,  *args, **kwargs):
            if not self.id:
                self.date = datetime.datetime.now()
            super(Rating, self).save(*args, **kwargs)
        
        
        
        
        
    
    
    
        
    