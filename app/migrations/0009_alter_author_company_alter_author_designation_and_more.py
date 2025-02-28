# Generated by Django 4.2.18 on 2025-02-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_skills_jobpost_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='company',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='designation',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='expiry',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
