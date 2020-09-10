# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CarLogo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    founded = models.CharField(max_length=255, blank=True, null=True)
    legal_person = models.CharField(max_length=255, blank=True, null=True)
    car_model = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_logo'


class EngStu(models.Model):
    word = models.CharField(max_length=255, blank=True, null=True)
    fayin = models.CharField(max_length=255, blank=True, null=True)
    cigen = models.CharField(max_length=255, blank=True, null=True)
    yisi = models.CharField(max_length=255, blank=True, null=True)
    pl = models.CharField(db_column='pL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eng_stu'


class Idiom(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    spenak = models.CharField(max_length=255, blank=True, null=True)
    meaning = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    example = models.CharField(max_length=255, blank=True, null=True)
    hot = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idiom'




class Englishword(models.Model):
    word = models.CharField(max_length=32, blank=True, null=True)
    word_chinese = models.CharField(max_length=255, blank=True, null=True)
    cixing = models.CharField(max_length=10)
    study_time = models.DateField(auto_now_add=True)
    count = models.IntegerField()



class Rank(models.Model):
    name = models.CharField(max_length=50)
    round_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rank'
