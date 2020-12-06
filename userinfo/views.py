import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from userinfo.forms import UserInfoForm, UploadImageForm, ReceiveUserInfoForm, ProjectExperienceForm, \
    WorkExperienceForm, SchoolExperienceForm
from userinfo.models import UserProfile, OrderUser, SchoolExperience


class IndexView(View):
    '''首页'''

    def get(self, request):
        return render(request, 'index_q.html')


class UserinfoView(LoginRequiredMixin, View):
    """
    用户个人信息
    """

    def get(self, request):
        user = UserProfile.objects.get(id=request.user.id)
        order_user = OrderUser.objects.get(id=request.user.id, is_pass=True)
        return render(request, 'usercenter-info.html', {"user": user, "order_user": order_user})

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class ReceiveUserinfoView(LoginRequiredMixin, View):
    """
    新建接单用户个人信息
    """
    def get(self, request):
        user = UserProfile.objects.get(id=request.user.id)
        # order_user = OrderUser.objects.get(id=request.user.id, is_pass=True)
        return render(request, 'createinfo.html', {"user": user})

    def post(self, request):
        receive_user_info_form = ReceiveUserInfoForm(request.POST, instance=request.user)
        print("1")
        school_experience_form = SchoolExperienceForm(request.POST, instance=request.user)
        print("2")
        work_experience_form = WorkExperienceForm(request.POST, instance=request.user)
        print("3")
        project_experience_form = ProjectExperienceForm(request.POST, instance=request.user)
        print("未进入")
        if receive_user_info_form.is_valid() and school_experience_form.is_valid():
            print("已进入")
            receive_user_info_form_obj = OrderUser(**receive_user_info_form.cleaned_data)
            receive_user_info_form_obj.save()
            school_experience_form_obj = SchoolExperience(**school_experience_form.cleaned_data)
            school_experience_form_obj.save()
            return render(request, 'usercenter-info.html', locals())
        else:
            return HttpResponse(json.dumps(receive_user_info_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    '''用户图像修改'''

    def post(self, request):
        # 上传的文件都在request.FILES里面获取，所以这里要多传一个这个参数
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['image']
            request.user.image = image
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


@login_required
def test_index1(request):
    return render(request, 'index1.html')
