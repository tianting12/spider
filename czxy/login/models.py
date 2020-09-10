from django.db import models

# Create your models here.
class User(models.Model):
    '''用户表'''
    geneder=(
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(verbose_name='用户名', max_length=128, unique=True) #unique 表示 唯一值
    password = models.CharField(verbose_name='密码', max_length=256)
    # phone = models.CharField(verbose_name='手机号码', max_length=256)
    email = models.EmailField(verbose_name='邮箱', unique=True)

    sex= models.CharField(verbose_name='性别', max_length=32, choices=geneder, default='男')
    c_time = models.DateTimeField(auto_now_add=True) #将当前时间ex作为注册时间

    #使用_str_帮助人性化显示信息
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['c_time'] #根据时间排序
        verbose_name = '用户'
        verbose_name_plural = '用户'

        # verbose_name指定在admin管理界面中显示中文；verbose_name表示单数形式的显示，verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
