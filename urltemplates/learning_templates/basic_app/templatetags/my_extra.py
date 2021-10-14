from django import template

register = template.Library()


def cut(value, arg):
    """
    This cuts out thr 'arg' from value
    """
    return value.replace(arg, '')


register.filter('cut', cut)
