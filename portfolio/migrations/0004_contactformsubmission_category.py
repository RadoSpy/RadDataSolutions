# Generated by Django 3.2.25 on 2024-12-29 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20241229_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformsubmission',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='portfolio.datasolutioncategory'),
        ),
    ]
