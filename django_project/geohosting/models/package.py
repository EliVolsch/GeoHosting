# coding=utf-8
"""
GeoHosting.

.. note:: Package model.
"""
import json

from django.db import models
from django.db.models import JSONField
from django.utils import timezone

from geohosting.models.product import Product
from geohosting.utils.functions import (
    parse_k8s_size, format_bytes, parse_k8s_cpu
)
from geohosting.utils.github import DevopsGithubClient
from geohosting.utils.paystack import create_paystack_price
from geohosting.utils.stripe import create_stripe_price


class PackageGroup(models.Model):
    """Package model for products."""

    name = models.CharField()
    package_code = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        help_text='This is the package code of the product on jenkins.'
    )
    specification = models.JSONField(
        blank=True,
        null=True,
        help_text='Specification of the package.'
    )
    conf_github_path = models.CharField(
        max_length=256,
        blank=True
    )

    def __str__(self):
        """Return package group name."""
        return self.name

    def sync_specification(self):
        """Sync specification from github."""
        if self.conf_github_path:
            client = DevopsGithubClient()
            content = client.get_content(
                'argocd/templates/' + self.conf_github_path
            )
            content = json.loads(content)
            specification = {}

            # Check every app
            for key, value in content.items():
                if isinstance(value, dict):
                    app_specification = {}
                    # Add the cpu
                    if 'cpu' in value:
                        app_specification['cpu'] = parse_k8s_cpu(value['cpu'])
                    # Add the memory
                    if 'memory' in value:
                        app_specification['memory'] = format_bytes(
                            parse_k8s_size(
                                value['memory']
                            )
                        )

                    # Add the volume
                    storage = 0
                    for k, v in value.items():
                        if 'volume' in k:
                            storage += parse_k8s_size(v)
                    if storage:
                        app_specification['storage'] = format_bytes(storage)
                    specification[key] = app_specification

            self.specification = specification
            self.save()
            return

        self.specification = None
        self.save()


class Package(models.Model):
    """Package model for products."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='packages'
    )
    name = models.CharField(
        max_length=256
    )
    erpnext_code = models.CharField(
        default='',
        blank=True
    )
    erpnext_item_code = models.CharField(
        default='',
        blank=True
    )
    currency = models.CharField(
        default='',
        blank=True
    )
    price_list = models.CharField(
        default='',
        blank=True,
        help_text='Selling price list of the package.'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    periodicity = models.CharField(
        max_length=256,
        default='monthly'
    )
    feature_list = JSONField(
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    stripe_id = models.CharField(
        blank=True,
        null=True,
        help_text='Price id on the stripe.'
    )
    paystack_id = models.CharField(
        blank=True,
        null=True,
        help_text='Price id on the paystack.'
    )

    # Package group that basically grouping by the variant
    package_group = models.ForeignKey(
        PackageGroup,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    # Is package enable
    enabled = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['product__order', 'order']

    def __str__(self):
        """Return package name and price."""
        return f"{self.name} - {self.price}  [{self.price_list}]"

    # ----------------------------------------------------
    # STRIPE
    # ----------------------------------------------------
    def _create_stripe_price_id(self):
        """Create price id on stripe."""
        features = []
        try:
            features = self.feature_list['spec']
        except KeyError:
            pass
        if self.price and not self.stripe_id:
            self.stripe_id = create_stripe_price(
                self.name, self.currency, self.price,
                self.periodicity.replace('ly', ''),
                features
            )
            self.save()

    def get_stripe_price_id(self):
        """Return price id on stripe."""
        if not self.stripe_id:
            self._create_stripe_price_id()
        return self.stripe_id

    # ----------------------------------------------------
    # PAYSTACK
    # ----------------------------------------------------
    def _create_paystack_price_id(self, email):
        """Create price id on paystack."""
        features = []
        try:
            features = self.feature_list['spec']
        except KeyError:
            pass
        # TODO: Always create new plan
        # if self.price and not self.paystack_id:
        if self.price:
            now = int(timezone.now().timestamp())
            self.paystack_id = create_paystack_price(
                f'{self.name} - {email} - {now}', self.currency, self.price,
                self.periodicity,
                features
            )
            self.save()
        return self.paystack_id

    def get_paystack_price_id(self, email):
        """Return price id on paystack."""
        # TODO: Paystack price plan is created everytime
        #  As it does not able to have multiple subscription with one plan
        # if not self.paystack_id:
        #     self._create_paystack_price_id()
        # return self.paystack_id
        return self._create_paystack_price_id(email)
