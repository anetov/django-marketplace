# Generated by Django 4.2.5 on 2023-10-04 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("sales", models.IntegerField()),
                ("purchases", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="seller",
            name="user",
        ),
        migrations.RemoveField(
            model_name="basket",
            name="buyer",
        ),
        migrations.RemoveField(
            model_name="product",
            name="seller",
        ),
        migrations.DeleteModel(
            name="Buyer",
        ),
        migrations.DeleteModel(
            name="Seller",
        ),
        migrations.AddField(
            model_name="basket",
            name="client",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.client",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="client",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="products.client",
            ),
            preserve_default=False,
        ),
    ]
