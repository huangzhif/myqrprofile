from django.db import models

# Create your models here.


class ExamModel(models.Model):
    qrpic = models.FileField(upload_to='qrpic/', verbose_name="二维码照片",
                             blank=True, null=True,help_text="仅支持.jpg，.png，.bmp，.gif")
    remark = models.TextField(max_length=1024, null=True, blank=True,
                              verbose_name="内容",help_text="支持url、英文; 不支持中文啊小老弟")
    newname = models.CharField(max_length=128, null=True, blank=True,
                               verbose_name="新文件名")
    contrast = models.FloatField(max_length=20, null=True, blank=True,
                                 verbose_name="对比度" ,help_text="范围（1.0~10.0）")
    brightness = models.FloatField(max_length=20, null=True, blank=True,
                                   verbose_name="明亮度" ,help_text="范围（1.0~10.0）")


    class Meta(object):
        db_table = "t_exam"
        verbose_name_plural = "二维码表"
        verbose_name = "二维码表"

    def __str__(self):
        return self.remark