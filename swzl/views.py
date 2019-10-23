# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import json
import time
from TestModel.models import *
from django.db.models import Avg, Count, Min, Sum
import xlrd
import uuid
from collections import OrderedDict
import hashlib
import urllib
import random
import logging
import requests
import os
import ast

logger = logging.getLogger(__name__)


# 内部方法，用于获取当前时间戳
# done
def _get_timestamp():
    return int(time.time())


# 内部方法用于返回json消息
# done
def _generate_json_message(flag, message):
    if flag:
        return HttpResponse("{\"error\":0,\"msg\":\""+message+"\"}",
                            #content_type="application/x-www-form-urlencoded",
                            content_type='application/json',
                            )
    else:
        return HttpResponse("{\"error\":1,\"msg\":\""+message+"\"}",
                            #content_type="application/x-www-form-urlencoded",
                            content_type='application/json',
                            )


# 内部方法用于将对象返回值转换成json串
# done
def _generate_json_from_models(response_list):
    return HttpResponse(json.dumps(response_list),
                        #content_type="application/x-www-form-urlencoded",
                        content_type='application/json',
                        )

# 用户管理界面跳转
# done
def manage_user(request):
    context = {}
    return render(request, 'manage_user.html', context)


# 缴费类别管理界面跳转
# done
def manage_lost(request):
    context = {}
    return render(request, 'manage_lost.html', context)


def manage_bus(request):
    context = {}
    return render(request, 'manage_bus.html', context)


def manage_type(request):
    context = {}
    return render(request, 'manage_type.html', context)


# 创建缴费记录
def create_payment(request):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    context = {}
    try:
        if request.POST:
            try:
                PaymentInfo.objects.get(payment_class_name=request.POST['payment_class_name'])
            except:
                payment_info = PaymentInfo(
                    payment_id=uuid.uuid1(),
                    payment_class_name=request.POST['payment_class_name'],
                    payment_create_time=current_time,
                    stu_payment_time=request.POST['stu_payment_time'],
                    payment_amount=request.POST['payment_amount'],
                    payment_status=request.POST['payment_status'],
                    stu_num_id=request.POST['stu_num_id'],
                    create_user_id=request.POST['create_user_id'],
                    payment_res_desc=request.POST['payment_res_desc']
                    )
                payment_info.save()
        return HttpResponseRedirect('/manage_payment')
    except:
        return HttpResponseRedirect('/manage_payment')


def remove_payment(request):
    context = {}
    try:
        payment_ids = request.POST['payment_ids']
        #import pdb;pdb.set_trace()
        for payment_id in payment_ids.split(","):
            payment_info = PaymentInfo.objects.get(payment_id=payment_id)
            payment_info.delete()
        return _generate_json_message(True, "Remove payment Success")
    except:
        return _generate_json_message(True, "Remove payment Failed")


def create_type(request):
    context = {}
    try:
        if request.POST:
            try:
                LostType.objects.get(lost_type_name=request.POST['lost_type_name'])
            except:
                lost_type_info = LostType(
                    lost_type_name=request.POST['lost_type_name'],
                    lost_type_id = uuid.uuid1(),
                    )
                lost_type_info.save()
        return HttpResponseRedirect('/manage_type')
    except:
        return HttpResponseRedirect('/manage_type')

def remove_type(request):
    context = {}
    try:
        lost_type_ids = request.POST['lost_type_ids']
        for type_id in lost_type_ids.split(","):
            lost_type_info = LostType.objects.get(lost_type_id=type_id)
            lost_type_info.delete()
        return _generate_json_message(True, "Remove Lost Type Success")
    except:
        return _generate_json_message(True, "Remove Lost Type Failed")

def get_all_type(request):
    list_response = []
    list_type = LostType.objects.all()
    for res in list_type:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)


def modify_type(request):
    try:
        if request.POST:
            lost_type_info = LostType.objects.get(lost_type_id=request.POST['lost_type_id'])
            lost_type_info.lost_type_name = request.POST['lost_type_name']
            lost_type_info.save()
        return HttpResponseRedirect('/manage_type')
    except:
        return HttpResponseRedirect('/manage_type')

# bus line 
def create_bus_line(request):
     context = {}
     try:
         if request.POST:
             try:
                 BusLines.objects.get(bus_line_name=request.POST['bus_line_name'])
             except:
                 bus_line_info = BusLines(
                     bus_line_name=request.POST['bus_line_name'],
                     bus_line_id = uuid.uuid1(),
                     )
                 bus_line_info.save()
         return HttpResponseRedirect('/manage_bus')
     except:
         return HttpResponseRedirect('/manage_bus')

        
def remove_bus_line(request):
    context = {}
    try:
        bus_line_ids = request.POST['bus_line_ids']
        for bus_line_id in bus_line_ids.split(","):
            bus_line_info = BusLines.objects.get(bus_line_id=bus_line_id)
            bus_line_info.delete()
        return _generate_json_message(True, "Remove Bus Line Success")
    except:
        return _generate_json_message(True, "Remove Bus Line Failed")


def get_all_bus_line(request):
    list_response = []
    list_bus_line = BusLines.objects.all()
    for res in list_bus_line:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)


def get_bus_line_by_name(request):
    pass


def modify_bus_line(request):
    try:
        if request.POST:
            bus_line_info = BusLines.objects.get(bus_line_id=request.POST['m_bus_line_id'])
            bus_line_info.bus_line_name = request.POST['m_bus_line_name']
            bus_line_info.bus_line_id = request.POST['m_bus_line_id']
            bus_line_info.save()
        return HttpResponseRedirect('/manage_bus')
    except:
        return HttpResponseRedirect('/manage_bus')


def create_lost(request):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    context = {}
    #import pdb;pdb.set_trace()
    try:
        if request.POST:
            try:
                LostInfo.objects.get(login_name=request.POST['login_name'])
            except:
                #image_file = request.FILES.get('image_file')
                #base_path = os.getcwd()
                #upload_file_path = base_path+"/image_file/"
                #file_name = os.path.join(upload_file_path, uuid.uuid1())
                #f = open(file_name, 'wb')
                #for chunk in image_file.chunks():
                #    f.write(chunk)
                #f.close()

                lost_info = LostInfo(
                    pick_up_time=request.POST['pick_up_time'],
                    bus_line_name=request.POST['bus_line_name'],
                    lost_type_name=request.POST['lost_type_name'],
                    lost_id=_get_timestamp(),
                    receive_address=request.POST['receive_address'],
                    is_received=0,
                    description=request.POST['description'],
                    received_name=request.POST['received_name'],
                    received_id_card=request.POST['received_id_card'],
                    received_phone_number=request.POST['received_phone_number'],
                    received_desc=request.POST['received_desc'],
                    contact_number=request.POST['contact_number'],
                    #image_path = file_name
                    image_path = "",
                    image_obj = request.FILES.get('image_file')
                    )
                lost_info.save()
        # return render(request, 'manage_user.html', context)
        return HttpResponseRedirect('/manage_lost')
    except:
        return HttpResponseRedirect('/manage_lost')


def remove_lost(request):
    context = {}
    try:
        lost_ids = request.POST['lost_ids']
        #import pdb;pdb.set_trace()
        for lost_id in lost_ids.split(","):
            lost_info = LostInfo.objects.get(lost_id=lost_id)
            lost_info.delete()
        return _generate_json_message(True, "Remove Lost Success")
    except:
        return _generate_json_message(True, "Remove Lost Failed")



def get_all_lost(request):
    list_response = []
    list_lost = LostInfo.objects.all()
    for res in list_lost:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)


def get_lost_by_bus_line(request):
    list_response = []
    search_date = request.POST['search_date']
    lost_type_name = request.POST['lost_type_name']
    bus_line_name = request.POST['bus_line_name']
    list_response = []
    list_lost = LostInfo.objects.all()
    if search_date:
        list_lost = list_lost.filter(pick_up_time=search_date)
    if bus_line_name:
        list_lost = list_lost.filter(bus_line_name=bus_line_name)
    if lost_type_name:
        list_lost = list_lost.filter(lost_type_name=lost_type_name)
    for res in list_lost:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)


def modify_lost(request):
    try:
        if request.POST:
            lost_info = LostInfo.objects.get(lost_id=request.POST['m_lost_id'])
            lost_info.pick_up_time = request.POST['m_pick_up_time']
            lost_info.bus_line_name = request.POST['m_bus_line_name']
            lost_info.lost_type_name = request.POST['m_lost_type_name']
            lost_info.receive_address = request.POST['m_receive_address']
            lost_info.is_received = request.POST['m_is_received']
            lost_info.description = request.POST['m_description']
            lost_info.received_name = request.POST['m_received_name']
            lost_info.received_id_card = request.POST['m_received_id_card']
            lost_info.received_phone_number = request.POST['m_received_phone_number']
            lost_info.received_desc = request.POST['m_received_desc']
            lost_info.contact_number = request.POST['m_contact_number']
            lost_info.save()
        return HttpResponseRedirect('/manage_lost')
    except:
        return HttpResponseRedirect('/manage_lost')


# 创建用户信息/用户注册
# success
def create_user(request):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    context = {}
    #import pdb;pdb.set_trace()
    try:
        if request.POST:
            try:
                UserInfo.objects.get(login_name=request.POST['login_name'])
                UserInfo.objects.get(username=request.POST['username'])
            except:
                user_info = UserInfo(
                    login_name=request.POST['login_name'],
                    username=request.POST['username'],
                    password=request.POST['password'],
                    user_id=_get_timestamp(),
                    user_permission=request.POST['user_permission'],
                    is_deleted=0,
                    create_time=current_time,
                    description=request.POST['description'],
                    class_id=request.POST['class_id']
                    )
                user_info.save()
        # return render(request, 'manage_user.html', context)
        return HttpResponseRedirect('/manage_user')
    except:
        return HttpResponseRedirect('/manage_user')


# 删除用户信息
# success
def remove_user(request):
    context = {}
    try:
        user_ids = request.POST['user_ids']
        for user_id in user_ids.split(","):
            user_info = UserInfo.objects.get(user_id=user_id)
            user_info.delete()
        return _generate_json_message(True, "Remove User Success")
    except:
        return _generate_json_message(True, "Remove User Failed")


# 修改用户信息
# success
def modify_user(request):
    try:
        if request.POST:
            user_info = UserInfo.objects.get(user_id=request.POST['user_id'])
            user_info.username = request.POST['username']
            user_info.username = request.POST['login_name']
            user_info.password = request.POST['password']
            user_info.user_permission = request.POST['user_permission']
            user_info.create_time = request.POST['create_time']
            user_info.is_deleted = request.POST['is_deleted']
            user_info.description = request.POST['description']
            user_info.class_id = request.POST['class_id']
            user_info.save()
        return HttpResponseRedirect('/manage_user')
    except:
        return HttpResponseRedirect('/manage_user')


# 查找用户信息
# success
def get_user_info_by_id(request):
    try:
        user_id = request.POST['user_id']
        if user_id:
            list_response = []
            list_user = UserInfo.objects.filter(user_id=user_id)
            for res in list_user:
                dict_tmp = {}
                dict_tmp.update(res.__dict__)
                dict_tmp.pop("_state", None)
                list_response.append(dict_tmp)
        return _generate_json_from_models(list_response)
    except:
        return _generate_json_message(False, "can`t get user info by this id")


# 获取所有用户信息
# success
def get_all_user_info(request):
    list_response = []
    list_user = UserInfo.objects.all()
    for res in list_user:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)


# 用户登录
# success
def user_login(request):
    if request.POST:
        context = {}
        login_username = request.POST['username']
        login_password = request.POST['password']
        try:
            if login_username:
                user_info = UserInfo.objects.get(username=login_username)
            if user_info is not None:
                if user_info.password == login_password:
                    return render(request, 'manage_lost.html', context)
                else:
                    return render(request, 'manage_lost.html', context)
        except:
            return _generate_json_message(False, "login false")


# 初始化登录界面
def init_web(request):
    return render(request, 'signin.html')


# 找不到界面
def page_not_found(request, exception):
    return render(request, '404.html', status=404)



