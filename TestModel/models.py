# -*- coding:UTF-8 -*-
from django.db import models


# 0 超级管理员
# 1 管理员
# 2 老师
# 3 普通用户，学生
# 用户类
class UserInfo(models.Model):
    user_id = models.CharField(max_length=200)
    login_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_permission = models.CharField(max_length=200)
    create_time = models.CharField(max_length=200)
    is_deleted = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    class_id = models.CharField(max_length=200)


# 公交线路
class BusLines(models.Model):
    bus_line_id = models.CharField(max_length=20)
    bus_line_name = models.CharField(max_length=200)

# 失物类型
class LostType(models.Model):
    lost_type_id = models.CharField(max_length=200)
    lost_type_name = models.CharField(max_length=200)


class LostInfo(models.Model):
    lost_id = models.CharField(max_length=200)
    pick_up_time = models.CharField(max_length=200)
    bus_line_name = models.CharField(max_length=200)
    lost_type_name = models.CharField(max_length=200)
    receive_address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    is_received = models.CharField(max_length=200)
    received_name = models.CharField(max_length=200)
    received_id_card = models.CharField(max_length=200)
    received_phone_number = models.CharField(max_length=200)
    received_desc = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    image_obj = models.ImageField(upload_to='image_file')


