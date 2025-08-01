from django.contrib import admin

from geohosting.admin.global_function import (
    sync_subscriptions, cancel_subscription
)
from geohosting.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Subscription admin."""

    list_display = (
        'subscription_id', 'customer_payment_id', 'payment_method',
        'current_period_start', 'current_period_end',
        'is_active'
    )
    list_filter = ('payment_method', 'is_active')
    actions = (sync_subscriptions, cancel_subscription)
    readonly_fields = (
        'payment_method', 'subscription_id', 'customer',
        'current_period_start', 'current_period_end',
        'payment_id'
    )
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'payment_method', 'subscription_id', 'customer',
                    'payment_id'
                )
            }
        ),
        (
            'Status',
            {
                'fields': (
                    'current_period_start', 'current_period_end', 'is_active'
                )
            }
        ),
    )
