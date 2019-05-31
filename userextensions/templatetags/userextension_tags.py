from django import template

# import models
from userextensions.models import UserFavorite

register = template.Library()


@register.simple_tag(name='is_favorite')
def is_favorite(request):
    try:
        user = request.user
        path = getattr(request, 'get_full_path')()
        favorite = UserFavorite.objects.get_object_or_none(url__icontains=path, user=user)
        if favorite:
            return favorite.id
        else:
            return False
    except:
        return None
