# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ButtonCounter(models.Model):
    red_count = models.IntegerField(default=0)
    blue_count = models.IntegerField(default=0)

    def push_red(self):
        self.red_count += 1
        self.save(update_fields=['red_count'])
        return self.red_count

    def push_blue(self):
        self.blue_count += 1
        self.save(update_fields=['blue_count'])
        return self.blue_count
