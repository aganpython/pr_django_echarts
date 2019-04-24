from django.db import models


# Create your models here.

# class Salesproduct(models.Model):
#     category = models.CharField(max_length=200, verbose_name="商品类别")
#     salesnum = models.IntegerField(default=0, verbose_name="商品销量")
#
#     class Meta:
#         db_table = "salesproduct"
#         verbose_name = "销售管理"
#         verbose_name_plural = verbose_name


class yifu(models.Model):
    category = models.CharField(max_length=200, verbose_name="商品类别")
    salesnum = models.IntegerField(default=0, verbose_name="商品销量")

    class Meta:
        db_table = "yifu"
        verbose_name = "衣服销售管理"
        verbose_name_plural = verbose_name


class dianqi(models.Model):
    category = models.CharField(max_length=200, verbose_name="商品类别")
    salesnum = models.IntegerField(default=0, verbose_name="商品销量")

    class Meta:
        db_table = "dianqi"
        verbose_name = "电器销售管理"
        verbose_name_plural = verbose_name
