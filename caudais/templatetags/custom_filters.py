from django import template

register = template.Library()

@register.filter
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def format_count(value):
    """Format large numbers with k suffix"""
    try:
        num = int(value)
        if num >= 1000:
            return f"{num/1000:.1f}k"
        return str(num)
    except (ValueError, TypeError):
        return value