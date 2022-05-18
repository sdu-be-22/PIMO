from django.contrib import admin

from .models.offer import Offer
from .models.order import Order
from .models.post import Post


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'title', 'max_cost', 'created_by', 'created_at', 'deadline', 'status',)
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'max_cost', 'created_at', 'deadline', 'details')
    list_filter = ('status',)
    list_editable = ('status', 'max_cost',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'created_at', 'status', 'title', 'max_cost', 'created_by', 'deadline', 'details')
    readonly_fields = ('id', 'created_at', 'updated_at')


class OfferAdm(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'order_id', 'cost', 'status',)
    list_display_links = ('id', 'user_id', 'order_id',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'user_id', 'order_id', 'cost', 'status',)
    readonly_fields = ('id',)


class PostAdm(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'details', 'likes',)
    list_display_links = ('id', 'title',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('title', 'created_at', 'details', 'likes',)
    readonly_fields = ('id',)


admin.site.register(Order, OrderAdm)
admin.site.register(Post, PostAdm)
admin.site.register(Offer, OfferAdm)
