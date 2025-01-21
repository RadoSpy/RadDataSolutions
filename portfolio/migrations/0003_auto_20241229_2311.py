# Generated by Django 3.2.25 on 2024-12-29 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_contactformsubmission_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSolutionCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('DM', 'Data Management'), ('DE', 'Data Integration & ETL'), ('DA', 'Analytics & BI'), ('DS', 'Machine Learning & Data Science'), ('SP', 'Data Security & Privacy'), ('CD', 'Cloud Data Solutions'), ('OT', 'Other')], default='OT', max_length=2)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Data Solution Category',
                'verbose_name_plural': 'Data Solution Categories',
            },
        ),
        migrations.AddField(
            model_name='contactformsubmission',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
