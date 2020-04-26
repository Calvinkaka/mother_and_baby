from django.conf.urls import url
from goods.views import *

urlpatterns = [
    # 首页
    url('^index$', IndexView.as_view(), name='index'),
    # 详情页
    url('^goods/(?P<goods_id>\\d+)$', DetailView.as_view(), name='detail'),
    # 列表页
    url('^list/(?P<type_id>\\d+)/(?P<page>\\d+)$', ListView.as_view(), name='list'),

]

