from django.contrib import admin
from django.core.cache import cache
from goods.models import *
# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''新增或者更新表中的数据时调用'''
        super().save_model(request, obj, form, change)

        # 发出任务，让celery worker重新生成首首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        '''删除表中的数据时调用'''
        super().delete_model(request, obj)
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')


class GoodsAdmin(BaseModelAdmin):
    list_per_page = 10
    list_display = ['name']
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['name']
    search_fields = ['name']


class GoodsSKUAdmin(BaseModelAdmin):
    list_per_page = 10
    list_display = ['name', 'type', 'status']
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['type']
    search_fields = ['type']


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    list_per_page = 10
    # list_display = ['sku']
    actions_on_top = False
    actions_on_bottom = True


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    list_per_page = 10
    list_display = ['sku', 'type', 'display_type']
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['type']
    search_fields = ['type']


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsSKU, GoodsSKUAdmin)
admin.site.register(GoodsType, GoodsTypeAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)