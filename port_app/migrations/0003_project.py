# Generated by Django 4.2.6 on 2023-10-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_app', '0002_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies_used', models.CharField(max_length=200)),
                ('github_link', models.URLField(blank=True)),
                ('live_demo_link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('date_completed', models.DateField()),
            ],
        ),
    ]