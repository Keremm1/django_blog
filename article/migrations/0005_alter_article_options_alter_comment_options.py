# Generated by Django 4.1.3 on 2022-11-20 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_comment_comment_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
