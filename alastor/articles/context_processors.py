# -*- coding: utf-8 -*-
from .models import Section


def extra_context(request):

    return {
        'nav_sections': Section.objects.all(),
    }
