import time
from django.db import models

# Create your models here.


class ValuePlan(models.Model):
    """
    时价表
    """
    code = models.CharField(verbose_name="营业分部代码", max_length=32)
    category = models.CharField(verbose_name="车类别", max_length=32)
    vehicle = models.CharField(verbose_name="具体车型", max_length=32)
    effective_date = models.CharField(verbose_name="价格代码生效日期", max_length=32)
    effective_first = models.CharField(verbose_name="价格代码有效第一日", max_length=32)
    effective_last = models.CharField(verbose_name="价格代码有效最后一日", max_length=32)
    value = models.CharField(verbose_name="价格代码", max_length=32)
    src = models.CharField(verbose_name="预订方式", max_length=32)

    class Meta:
        db_table = 't_value_plan'


class UploadFile(models.Model):
    """
    上传的文件
    """
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='./upload')
    ctime = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S'))

    class Meta:
        db_table = 't_upload_file'
