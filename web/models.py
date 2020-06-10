from django.db import models

# Create your models here.


class Customer(models.Model):
    """
    客户表
    """
    name = models.CharField(verbose_name='姓名', max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    company = models.CharField(verbose_name='公司', max_length=32)

    def __str__(self):
        return self.name


class Payment(models.Model):
    money = models.IntegerField(verbose_name='付款金额')
    customer = models.ForeignKey(verbose_name='关联客户', to='Customer')
    create_time = models.DateTimeField(verbose_name='付款时间', auto_now_add=True)
