# Generated by Django 4.0.5 on 2022-07-17 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0008_challenge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Ans', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('ques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
