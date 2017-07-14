# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import View

from models import ButtonCounter


def get_counter():
    counter, _ = ButtonCounter.objects.get_or_create(pk=1)
    return counter


class PushButtonView(View):
    def get(self, request, *args, **kwargs):
        counter = get_counter()
        try:
            color = request.GET['color']
            if color == 'red':
                new_count = counter.push_red()
            elif color == 'blue':
                new_count = counter.push_blue()
            else:
                color = 'No color provided'
                new_count = 0
            return JsonResponse({
                'color': color,
                'new_count': new_count,
            })
        except KeyError:
            return JsonResponse({
                'success': False,
                'reason': 'Provide a color',
            })


class ButtonTotalsView(View):
    def get(self, request, *args, **kwargs):
        counter = get_counter()
        return JsonResponse({
            'red_count': counter.red_count,
            'blue_count': counter.blue_count,
        })
