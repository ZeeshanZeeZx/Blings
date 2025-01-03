from django import template

register = template.Library()

@register.filter
def to_range(value):
    try:
        return range(int(value))
    except ValueError:
        return range(0)

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument."""
    return value * arg

@register.filter
def total_sum(cart_items):
    """Sums up the subtotal of all items in the cart."""
    return sum(item['subtotal'] for item in cart_items)