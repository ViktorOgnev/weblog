from django import template
from coltrane.models import Entry

def do_latest_entries(parser, token):
    return LatestEntriesNode()

    
class LatestEntriesNode(template.Node):
    
    def render(self, context):
        context['latest_entries'] = Entry.live.all()[:5]
        return ''

register = template.Library()
register.tag('get_latest_entries', do_latest_entries)



    
def do_latest_content(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise template.TemplateSyntaxError(""" 'get_latest_content'
                                            tag takes exactly four arguments""")
    return LatestContentNode(bits[1], bits[2], bits[4])