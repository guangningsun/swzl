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
import commands
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
#                      content_type="application/json")
#    res["Access-Control-Allow-Origin"] = "*"
#    res["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE,OPTIONS"
#    res["Access-Control-Max-Age"] = "1000"
#    res["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
#   return res


# 学生管理界面跳转
# done
def manage_student(request):
    context = {}
    return render(request, 'manage_student.html', context)


# 缴费管理界面跳转
# done
def manage_payment(request):
    context = {}
    return render(request, 'manage_payment.html', context)


# 用户管理界面跳转
# done
def manage_user(request):
    context = {}
    return render(request, 'manage_user.html', context)


# 缴费类别管理界面跳转
# done
def manage_p_class(request):
    context = {}
    return render(request, 'manage_payment_class.html', context)


def manage_class(request):
    context = {}
    return render(request, 'manage_class.html', context)


def manage_settings(request):
    context = {}
    return render(request, '404.html', context)

def manage_report(request):
    context = {}
    return render(request, '404.html', context)

def upload(request):
    context = {}
    return render(request, 'upload.html', context)

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


def get_all_payment_info(request):
    list_response = []
    list_payment = PaymentInfo.objects.all()
    for res in list_payment:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)


def modify_payment(request):
    pass


def get_payment_list_by_stu_id_card(request):
    pass







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
                    return render(request, 'upload.html', context)
                else:
                    return render(request, 'upload.html', context)
        except:
            return _generate_json_message(False, "login false")


# 初始化登录界面
def init_web(request):
    return render(request, 'signin.html')


def audio_upload(request):
    context = {}
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    if request.method == 'POST':
        try:
            import pdb;pdb.set_trace()
            # get file
            audio_file = request.FILES.get('audio_file')
            # init prepare data
            prepare_data={'uid':'123', 'token':'123','lang': 'zh'}
            prepare_req = requests.post('http://xz502.tpddns.cn:8210/v1/trans/api/prepare', data=prepare_data)
            task_id=""
            # linux 文件夹路径
            bash_path = os.getcwd()
            upload_file_path = bash_path+"/audio_file/"
            file_name = os.path.join(upload_file_path, audio_file.name)
            f = open(file_name, 'wb')
            for chunk in audio_file.chunks():
                f.write(chunk)
            f.close()
            if json.loads(prepare_req.text)['ok'] == 0:
                task_id = json.loads(prepare_req.text)['data'].encode('utf-8')
                #audio_data = { "task_id" : task_id , 'filename' : "@/"+file_name }
                #upload_req = requests.post('http://xz502.tpddns.cn:8210/v1/trans/api/upload', data=audio_data)
                #upload_req = os.system("curl -F \"task_id="+prepare_res_data+"\" -F \"filename=@/"+file_name+"\" http://xz502.tpddns.cn:8210/v1/trans/api/upload")
                (status, output) = commands.getstatusoutput("curl -F \"task_id="+task_id+"\" -F \"filename=@/"+file_name+"\" http://xz502.tpddns.cn:8210/v1/trans/api/upload")
                upload_status = output.split("ok")[1].replace("}", "").replace(":","").replace("\"","").replace("\'","")
                ok_success = '0'
                if str(upload_status) == ok_success:
                    progress_data = {"task_id": task_id}
                    progress_req = requests.post('http://xz502.tpddns.cn:8210/v1/trans/api/getProgress', data=progress_data)
                    pd = json.loads(progress_req.text)['data'].encode('utf-8')
                    progress_status = json.loads(pd)["status"]
                    if progress_status == 3:
                        result_data = {"task_id": task_id}
                        result_req = requests.post('http://xz502.tpddns.cn:8210/v1/trans/api/getResult', data=result_data)
                        #return HttpResponse(result_req.text, content_type='application/json',)
                        res_data_list = ast.literal_eval(json.loads(result_req.text)["data"])
                        context = {"req_data": res_data_list[0]["transcript"]}
                        return render(request, 'upload.html', context)
            else:
                return "false"
        except:
            return HttpResponseRedirect('/upload')
    return HttpResponseRedirect('/upload')


# 找不到界面
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

