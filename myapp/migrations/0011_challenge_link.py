# Generated by Django 4.0.5 on 2022-08-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_answer_sno'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='link',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]