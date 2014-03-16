from django import template

register = template.Library()

@register.filter
def classname(obj, arg=None):
    classname = obj.__class__.__name__
    if arg:
        if arg == classname:
            return True
        else:
            return False
    else:
        return classname
