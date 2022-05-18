from django.contrib import admin
from logs.models.offer_log import Offer_log
from logs.models.offer_his import Offer_his
from logs.models.order_log import Order_log
from logs.models.order_his import Order_his
from logs.models.user_backup import User_backup
from logs.models.user_login_his import User_login_his
from logs.models.user_profile_his import User_profile_his


# Register your models here.

class Order_hisAdm(admin.ModelAdmin):
    list_display = ('log_id', 'order_id', 'old_status', 'new_status', 'log_date',)
    list_display_links = ('log_id', 'order_id',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('order_id', 'old_status', 'new_status', 'log_date',)
    readonly_fields = ('log_id', 'order_id', 'old_status', 'new_status', 'log_date',)


class Order_logAdm(admin.ModelAdmin):
    list_display = ('log_id', 'order_id', 'created_at', 'deleted_at', 'last_status', 'title', 'user_id', 'deadline')
    list_display_links = ('log_id', 'order_id', 'title')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('order_id', 'created_at', 'deleted_at', 'last_status', 'title' 'user_id', 'deadline')
    readonly_fields = ('log_id', 'order_id', 'created_at', 'deleted_at', 'last_status', 'title', 'user_id', 'deadline')


class Offer_hisAdm(admin.ModelAdmin):
    list_display = ('log_id', 'offer', 'old_status', 'new_status', 'log_date',)
    list_display_links = ('log_id', 'offer',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('offer', 'old_status', 'new_status', 'log_date',)
    readonly_fields = ('log_id', 'offer', 'old_status', 'new_status', 'log_date',)


class Offer_logAdm(admin.ModelAdmin):
    list_display = ('log_id', 'action', 'offer', 'cost', 'datetime', 'last_status',)
    list_display_links = ('log_id', 'offer',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('action', 'offer', 'cost', 'datetime', 'last_status',)
    readonly_fields = ('log_id', 'action', 'offer', 'cost', 'datetime', 'last_status',)


class Backup_Adm(admin.ModelAdmin):
    list_display = ('log_id', 'user_id', 'username', 'created_at', 'deleted_at',)
    list_display_links = ('log_id', 'user_id',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = ('user_id', 'username', 'created_at', 'deleted_at',)
    readonly_fields = ('log_id', 'user_id', 'username', 'created_at', 'deleted_at',)


class Login_hisAdm(admin.ModelAdmin):
    list_display = ('log_id', 'user_id', 'logged_at', 'was_active', 'username',)
    list_display_links = ('log_id', 'user_id',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = ('user_id', 'logged_at', 'was_active', 'username',)
    readonly_fields = ('log_id', 'user_id', 'logged_at', 'was_active', 'username',)


class Profile_hisAdm(admin.ModelAdmin):
    list_display = (
        'log_id', 'log_date', 'user_id', 'old_password', 'new_password', 'first_name', 'second_name', 'old_email',
        'new_email',
        'username',)
    list_display_links = ('log_id', 'user_id',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = (
        'log_date', 'user_id', 'old_password', 'new_password', 'first_name', 'second_name', 'old_email', 'new_email',
        'username',)
    readonly_fields = (
        'log_id', 'log_date', 'user_id', 'old_password', 'new_password', 'first_name', 'second_name', 'old_email',
        'new_email', 'username',)


admin.site.register(Offer_his, Offer_hisAdm)
admin.site.register(Offer_log, Offer_logAdm)
admin.site.register(Order_his, Order_hisAdm)
admin.site.register(Order_log, Order_logAdm)
admin.site.register(User_backup, Backup_Adm)
admin.site.register(User_login_his, Login_hisAdm)
admin.site.register(User_profile_his, Profile_hisAdm)
