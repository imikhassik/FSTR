# Generated by Django 4.2.1 on 2023-05-25 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0011_rename_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pereval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pereval.perevaladded'),
        ),
    ]
