from django import template
from post.models import *


register=template.Library()
@register.simple_tag(name='category_list')
def show_category():
    return  Category.objects.all()

