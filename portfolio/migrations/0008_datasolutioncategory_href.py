# Generated by Django 3.2.25 on 2025-01-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_datasolutioncategory_desc_oneliner'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasolutioncategory',
            name='href',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
