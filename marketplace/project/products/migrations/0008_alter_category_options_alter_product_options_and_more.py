# Generated by Django 4.1.4 on 2023-11-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_alter_product_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ("name_cat",), "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name_plural": "Товары"},
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(),
        ),
    ]
