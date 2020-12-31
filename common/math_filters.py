from django.template.defaulttags import register


@register.filter
def mod(value, arg):
    '''
    Modulo Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int(value)
        arg = int(arg)
        if arg:
            return value % arg
    except:
        pass
    return ''
