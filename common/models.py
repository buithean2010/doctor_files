from django.db import models

# Create your models here.


class MainCategories(models.Model):
    name_vn = models.CharField(max_length=512)
    name_kanji = models.CharField(max_length=512)
    name_kana = models.CharField(max_length=512)
    name_en = models.CharField(max_length=512)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_categories'


class SubCategories1(models.Model):
    main_cat = models.ForeignKey(MainCategories, models.DO_NOTHING)
    name_vn = models.CharField(max_length=512)
    name_kanji = models.CharField(max_length=512)
    name_kana = models.CharField(max_length=512)
    name_en = models.CharField(max_length=512)
    img_url = models.TextField()
    sort_no = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sub_categories_1'
