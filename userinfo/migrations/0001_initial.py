# Generated by Django 2.0.2 on 2019-12-01 07:23

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_auto_20191124_1500'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('type', models.CharField(choices=[('receive', '接单用户'), ('publish', '发单用户')], default='publish', max_length=10, verbose_name='用户类别')),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别')),
                ('address', models.CharField(blank=True, default='', max_length=100, verbose_name='现地址')),
                ('mobile', models.CharField(blank=True, max_length=13, null=True, verbose_name='手机号')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y%m', verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='标题')),
                ('desc', models.CharField(blank=True, max_length=1000, verbose_name='描述')),
                ('skill', models.CharField(blank=True, max_length=100, verbose_name='使用技能')),
                ('start_time', models.CharField(blank=True, max_length=200, verbose_name='项目开始时间')),
                ('end_time', models.CharField(blank=True, max_length=200, verbose_name='项目结束时间')),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=100, verbose_name='学校')),
                ('desc', models.CharField(blank=True, max_length=1000, verbose_name='内容描述')),
                ('start_time', models.CharField(blank=True, max_length=200, verbose_name='学习开始时间')),
                ('end_time', models.CharField(blank=True, max_length=200, verbose_name='学习结束时间')),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, verbose_name='公司')),
                ('job_desc', models.CharField(blank=True, max_length=1000, verbose_name='工作内容描述')),
                ('skill', models.CharField(blank=True, max_length=100, verbose_name='使用技能')),
                ('start_time', models.CharField(blank=True, max_length=200, verbose_name='工作开始时间')),
                ('end_time', models.CharField(blank=True, max_length=200, verbose_name='工作结束时间')),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUser',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id_card', models.CharField(blank=True, max_length=18, verbose_name='身份证')),
                ('real_name', models.CharField(blank=True, max_length=50, verbose_name='真实姓名')),
                ('job_time', models.CharField(blank=True, max_length=30, verbose_name='工作年限')),
                ('introduce', models.CharField(blank=True, max_length=1000, verbose_name='简介')),
                ('skill', models.CharField(blank=True, max_length=100, verbose_name='擅长技能')),
                ('industry', models.CharField(blank=True, max_length=200, verbose_name='所属行业')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_pass', models.BooleanField(default=False, verbose_name='是否审核通过')),
                ('is_delete', models.BooleanField(default=False)),
                ('work_status', models.CharField(blank=True, choices=[('freedom', '自由职业'), ('fullwork', '全职')], default='freedom', max_length=10, verbose_name='性别')),
                ('role', models.CharField(blank=True, max_length=32, verbose_name='角色')),
            ],
            options={
                'verbose_name': '接单用户信息',
                'verbose_name_plural': '接单用户信息',
            },
            bases=('userinfo.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=True, to='project.Project'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='user',
            field=models.ForeignKey(on_delete=True, related_name='we_user', to='userinfo.OrderUser'),
        ),
        migrations.AddField(
            model_name='schoolexperience',
            name='user',
            field=models.ForeignKey(on_delete=True, related_name='se_user', to='userinfo.OrderUser'),
        ),
        migrations.AddField(
            model_name='projectexperience',
            name='user',
            field=models.ForeignKey(on_delete=True, related_name='pe_user', to='userinfo.OrderUser'),
        ),
    ]
