import xadmin
from snippets.models import EmailVerifyRecord
from xadmin import views

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class GlobalSetting(object):
    site_title = "shhnwangjian后台管理系统"
    site_footer = "http://www.cnblogs.com/shhnwangjian/"


xadmin.site.register(views.CommAdminView, GlobalSetting)

