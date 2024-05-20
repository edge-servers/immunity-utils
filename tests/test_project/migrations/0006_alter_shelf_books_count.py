# Generated by Django 4.2.3 on 2023-07-25 11:19

from django.db import migrations
import immunity_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("test_project", "0005_organizationradiussettings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shelf",
            name="books_count",
            field=immunity_utils.fields.FallbackPositiveIntegerField(
                blank=True, fallback=21, null=True, verbose_name="Number of books"
            ),
        ),
    ]
