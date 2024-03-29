# Generated by Django 5.0.2 on 2024-02-25 21:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(choices=[('AUTO', 'Auto'), ('EASY', 'Easy'), ('HARD', 'Hard'), ('MEDIUM DEMON', 'Medium Demon'), ('NORMAL', 'Normal'), ('HARD DEMON', 'Hard Demon'), ('HARDER', 'Harder'), ('INSANE DEMON', 'Insane Demon'), ('INSANE', 'Insane'), ('EASY DEMON', 'Easy Demon'), ('EXTREME DEMON', 'Extreme Demon')], max_length=50)),
                ('pub_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('AUTO', 'Auto'), ('EASY', 'Easy'), ('HARD', 'Hard'), ('MEDIUM DEMON', 'Medium Demon'), ('NORMAL', 'Normal'), ('HARD DEMON', 'Hard Demon'), ('HARDER', 'Harder'), ('INSANE DEMON', 'Insane Demon'), ('INSANE', 'Insane'), ('EASY DEMON', 'Easy Demon'), ('EXTREME DEMON', 'Extreme Demon')], max_length=50)),
                ('text', models.TextField(max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levels.level')),
            ],
        ),
    ]
