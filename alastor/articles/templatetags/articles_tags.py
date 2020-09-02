from django import template

register = template.Library()


# @register.inclusion_tag('articles/grid.html')
@register.simple_tag
def show_grid(articles):

    if len(articles) == 1:
        grid_type = 'full'
    elif len(articles) % 2 == 0:
        grid_type = 'double'
    else:
        grid_type = 'triple'

    return grid_type
