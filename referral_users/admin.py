from django.contrib import admin
from .models import ReferralUser, FormResults


class ReferralUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'referral_code')


class FormResultsAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'tg_username', 'name', 'phone_number', 'answers')


admin.site.register(ReferralUser, ReferralUserAdmin)
admin.site.register(FormResults, FormResultsAdmin)
