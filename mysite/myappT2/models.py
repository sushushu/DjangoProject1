from django.db import models
#
# # Create your models here.
#
#
# class Account(models.Model):
#     username = models.CharField(max_length=64, unique=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
#     register_date = models.DateTimeField("注册日期", auto_now_add=True)
#     signature = models.CharField(verbose_name="签名", max_length=128, blank=True, null=True)
#
#
# class Article(models.Model):
#     """文章表"""
#     title = models.CharField(max_length=255, unique=True)
#     content = models.TextField("文章内容")
#     account = models.ForeignKey("Account", verbose_name="作者", on_delete=models.CASCADE)
#     tags = models.ManyToManyField("Tag", blank=True)
#     pub_date = models.DateTimeField()
#     read_count = models.IntegerField(default=0)
#
#
# class Tag(models.Model):
#     """文章标签表"""
#     name = models.CharField(max_length=64, unique=True)
#     date = models.DateTimeField(auto_now_add=True)