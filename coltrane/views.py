from django.shortcuts import get_object_or_404, render_to_response
from coltrane.models import Entry, Category, Link
from django.views.generic.list import ListView

def entries_index(request): 
    return render_to_response('coltrane/entry_index.html', 
                                {'entry_list': Entry.live.all()})
                                
def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, pub_date__year=pub_date.year,
                              pub_date__month=pub_date.month,
                              pub_date__day=pub_date.day,
                              slug=slug)
    return render_to_response('coltrane/entry_detail.html',
    { 'entry': entry })
        
                                          
                                                
def category_list(request):
    return render_to_reponse('coltrane/category_list.html', 
                             {'object_list' : Category.objects.all()})
                              
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = category.live_entry_set()
    return render_to_response('coltrane/category_detail.html',
                              { 'category': category,
                                'object_list':object_list})
                                
def all_items_by_tag(request, tag):
    tagged_entries = [e for e in Entry.live.all() if tag in e.tags]
    tagged_links = [l for l in Link.objects.all() if tag in l.tags]
    return render_to_response('coltrane/tagging/items_by_tag.html',
                                {'tagged_entries': tagged_entries,
                                  'tagged_links': tagged_links,
                                  'tagname': tag})