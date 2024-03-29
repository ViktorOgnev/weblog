from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count 
from django.db.models import Sum

class SnippetManager(models.Manager):
    
    def top_authors(self):
        return User.objects.annotate(score=Count('snippet')).order_by('score')

    def most_bookmarked(self):  
        return self.annotate(score=Count('bookmark')).order_by('score')
        
    def get_score(self):
        return self.rating_set.aggregate(Sum('rating'))
        
        
    def top_rated(self):
        return self.annotate(score=Sum('rating')).order_by('score')
        
class LanguageManager(models.Manager):
    
    def top_languages(self):
        return self.annotate(score=Count('snippet')).order_by('score')

