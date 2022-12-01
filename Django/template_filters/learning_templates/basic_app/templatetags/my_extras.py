from django import template

register = template.Library()

#custome template filter
@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut)
