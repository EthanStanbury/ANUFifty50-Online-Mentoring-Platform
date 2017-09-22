# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Feedback_contact

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name", "get_user", "message"]
    list_filter = ['first_name', "last_name", 'user__role']

    def get_user(self, obj):
        return obj.user.role

    get_user.admin_order_field = 'Role'  # Allows column order sorting
    get_user.short_description = 'Profile Role'  # Renames column head


admin.site.register(Feedback_contact, FeedbackAdmin)