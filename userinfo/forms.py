from userinfo.models import UserProfile, OrderUser, ProjectExperience, WorkExperience, SchoolExperience
from django import forms


class UploadImageForm(forms.ModelForm):
    '''用户更改图像'''

    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    '''个人中心信息修改'''

    class Meta:
        model = UserProfile
        fields = ['gender', 'birthday', 'address', 'mobile']


class ProjectExperienceForm(forms.ModelForm):
    '''项目经验'''

    class Meta:
        model = ProjectExperience
        fields = ['title', 'desc', 'skill', 'start_time', 'end_time']


class WorkExperienceForm(forms.ModelForm):
    '''项目经验'''

    class Meta:
        model = WorkExperience
        fields = ['company', 'job_desc', 'skill', 'start_time', 'end_time']


class SchoolExperienceForm(forms.ModelForm):
    '''学习经验'''

    class Meta:
        model = SchoolExperience
        fields = ['school', 'desc',  'start_time', 'end_time']


class ReceiveUserInfoForm(forms.ModelForm):
    '''新建接单用户信息'''

    class Meta:
        model = OrderUser
        fields = ['id_card', 'real_name', 'job_time', 'introduce', 'skill', 'industry']