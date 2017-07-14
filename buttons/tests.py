# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.test import TestCase, Client


class TestButtonPushing(TestCase):
    def setUp(self):
        self.client = Client()

    def test_button_pushing(self):
        base_url = reverse_lazy('push_button')
        url = base_url + '?color=red'
        r = self.client.get(url).json()
        self.assertEqual(r['new_count'], 1)

    def test_get_totals(self):
        url = reverse_lazy('button_totals')
        r = self.client.get(url).json()
        self.assertEqual(r['red_count'], 0)
        self.assertEqual(r['blue_count'], 0)

        # Add a red button press
        base_url = reverse_lazy('push_button')
        url = base_url + '?color=red'
        self.client.get(url)

        url = reverse_lazy('button_totals')
        r = self.client.get(url).json()
        self.assertEqual(r['red_count'], 1)
        self.assertEqual(r['blue_count'], 0)
