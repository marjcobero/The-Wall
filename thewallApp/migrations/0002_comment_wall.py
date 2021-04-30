# Generated by Django 2.2 on 2021-03-25 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thewallApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='thewallApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='thewallApp.User')),
                ('wall_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='thewallApp.Wall')),
            ],
        ),
    ]