# Generated by Django 4.1.4 on 2023-10-25 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0005_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]