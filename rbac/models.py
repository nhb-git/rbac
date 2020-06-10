from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=32)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    roles = models.ManyToManyField(verbose_name='用户的角色', to='Role', blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(verbose_name='角色名称', max_length=20, unique=True)
    permission = models.ManyToManyField(verbose_name='角色的权限', to='Permission', blank=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    权限表
    """
    name = models.CharField(verbose_name='权限名称', max_length=64)
    alias = models.CharField(verbose_name='权限别名', max_length=64, unique=True)
    url = models.CharField(verbose_name='url路径', max_length=128, unique=True)
    icon = models.CharField(verbose_name='图标', max_length=32, null=True, blank=True)
    is_menu = models.BooleanField(verbose_name='是否为菜单', default=False)
    parent_menu = models.ForeignKey(verbose_name='父菜单', to='self', to_field='id', on_delete=models.CASCADE,
                                    blank=True)
