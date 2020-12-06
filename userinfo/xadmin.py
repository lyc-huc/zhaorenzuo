# encoding: utf-8
__author__ = 'gong'
__date__ = '2019/8/10 14:42'

from xadmin import views
import xadmin


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = 'NBA后台管理界面'
    # 修改footer
    site_footer = '科比的公司'
    # 收起菜单
    menu_style = 'accordion'


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView ,BaseSetting)

# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)