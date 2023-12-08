from django import template
from . import bag_tools

register = template.Library()

register.filter(name='calc_subtotal')(bag_tools.calc_subtotal)