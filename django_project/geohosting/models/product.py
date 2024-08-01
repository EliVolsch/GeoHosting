# coding=utf-8
"""
GeoHosting.

.. note:: Product model.
"""

from django.db import models
from django.db.models import JSONField

from geohosting.models.cluster import Cluster
from geohosting.models.fields import SVGAndImageField


class Product(models.Model):
    """Product model."""

    name = models.CharField(
        max_length=256
    )
    order = models.PositiveIntegerField(
        default=0
    )
    upstream_id = models.CharField(
        max_length=256
    )
    description = models.TextField(
        blank=True
    )
    image = SVGAndImageField(
        upload_to='product_images/',
        null=True,
        blank=True
    )
    available = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        """Return product name."""
        return self.name


class ProductMetadata(models.Model):
    """Product metadata."""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    key = models.CharField(
        max_length=256,
        help_text='The key of metadata of product.'
    )
    value = models.TextField(
        help_text='Metadata value for the product'
    )

    class Meta:
        unique_together = ['product', 'key']


class ProductCluster(models.Model):
    """Product x cluster model."""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    cluster = models.ForeignKey(
        Cluster, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ['product', 'cluster']


class ProductMedia(models.Model):
    """Product Media model."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images')
    image = models.ImageField(
        upload_to='product_media/'
    )
    title = models.TextField(
        blank=True
    )
    description = models.TextField(
        blank=True
    )
    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        """Return image file name."""
        return self.image.name

    class Meta:
        ordering = ['product__order', 'order']


class Package(models.Model):
    """Package model for products."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='packages'
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
    name = models.CharField(
        max_length=256
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
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
    package_code = models.CharField(
        max_length=256,
        help_text='This is the package code of the product on jenkins.'
    )

    class Meta:
        ordering = ['product__order', 'order']

    def __str__(self):
        """Return package name and price."""
        return f"{self.name} - {self.price}"
