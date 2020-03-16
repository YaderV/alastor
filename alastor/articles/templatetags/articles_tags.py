from django import template

register = template.Library()


@register.inclusion_tag('articles/grid.html')
def show_grid(articles):

    if articles.count() == 1:
        grid_type = 'full'
    elif articles.count() % 2 == 0:
        grid_type = 'double'
    else:
        grid_type = 'triple'

    return {
        'articles': articles,
        'type': grid_type
    }
