# Generated by Django 5.0.3 on 2024-03-31 11:48

import django.contrib.postgres.fields
import django.utils.timezone
import django_lifecycle.mixins
import model_utils.fields
from django.db import migrations, models
from ..models import TIMEZONES_CHOICES


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="full name"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="short name"
                    ),
                ),
                (
                    "review_days",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.PositiveSmallIntegerField(
                            choices=[
                                (0, "Lundi"),
                                (1, "Mardi"),
                                (2, "Mercredi"),
                                (3, "Jeudi"),
                                (4, "Vendredi"),
                                (5, "Samedi"),
                                (6, "Dimanche"),
                            ]
                        ),
                        size=None,
                        verbose_name="Jours de révision",
                    ),
                ),
                (
                    "review_time",
                    models.TimeField(default="18:00", verbose_name="Heure de révision"),
                ),
                (
                    "timezone",
                    models.CharField(
                        choices=TIMEZONES_CHOICES,
                        default="UTC",
                        max_length=50,
                        verbose_name="Fuseau horaire",
                    ),
                ),
                (
                    "email_notifications_enabled",
                    models.BooleanField(
                        default=True, verbose_name="Notifications par email"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]
