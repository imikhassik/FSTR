# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Coords(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longtitude = models.FloatField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'coords'


class Images(models.Model):
    title = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField()

    class Meta:
        db_table = 'images'


class PerevalAdded(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    beautytitle = models.TextField(db_column='beautyTitle', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    other_titles = models.TextField(blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True)
    coord_id = models.ForeignKey(Coords, models.CASCADE, related_name='perevaladded_coord_id_set',
                                 blank=True, null=True)
    winter = models.TextField(blank=True, null=True)
    summer = models.TextField(blank=True, null=True)
    autumn = models.TextField(blank=True, null=True)
    spring = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'pereval_added'


class PerevalAreas(models.Model):
    id_parent = models.BigIntegerField()
    title = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'pereval_areas'


class PerevalImages(models.Model):
    pereval = models.ForeignKey(PerevalAdded, models.CASCADE)
    image = models.ForeignKey(Images, models.CASCADE)

    class Meta:
        db_table = 'pereval_images'


class SprActivitiesTypes(models.Model):
    title = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'spr_activities_types'


class Users(models.Model):
    email = models.CharField(unique=True, max_length=320, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fam = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    otc = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'users'
