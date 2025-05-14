from django import template

register = template.Library()

@register.simple_tag
def get_scale(temp):
    return f'{round((float(temp)-273.15), 1)} °C'

# @register.simple_tag
# def get_scale(temp):
#     return [f'{round((float(temp)-273.15), 1)} °C',f'{round(temp, 1)} °K', f'{round(1.8 * (float(temp)-273) - 32, 1)} °F']
