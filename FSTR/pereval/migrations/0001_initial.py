# Generated by Django 4.2.1 on 2023-05-26 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longtitude', models.FloatField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.TextField(blank=True, null=True)),
                ('summer', models.TextField(blank=True, null=True)),
                ('autumn', models.TextField(blank=True, null=True)),
                ('spring', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=320, null=True, unique=True)),
                ('fam', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('otc', models.CharField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='new', max_length=10)),
                ('beauty_title', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('other_titles', models.TextField(blank=True, null=True)),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.TimeField(auto_now_add=True, null=True)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.user')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('data', models.ImageField(upload_to='')),
                ('pereval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.pereval')),
            ],
        ),
    ]
