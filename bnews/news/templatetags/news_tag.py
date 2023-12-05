from django import template



from news.models import Catigories, News

register = template.Library()

@register.simple_tag()
def get_cat():
    return Catigories.objects.all()


