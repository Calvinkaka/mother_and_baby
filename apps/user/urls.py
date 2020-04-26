from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.user.views import *

urlpatterns = [
    # url('register$', views.register, name='register'),
    # url('register_handle$', views.register_handle, name='register_handle')
    # 注册
    url('^register$', RegisterView.as_view(), name='register'),
    # 用户激活
    url('^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    # 登录
    url('^login$', LoginView.as_view(), name='login'),
    url('^logout$', LogoutView.as_view(), name='logout'),

    # 用户中心-信息页
    # url('^$', login_required(UserInfoView.as_view()), name='user'),
    url('^$', UserInfoView.as_view(), name='user'),
    # 用户中心-订单页
    # url('^order$', login_required(UserOrderView.as_view()), name='order'),
    url('^order/(?P<page>\\d+)$', UserOrderView.as_view(), name='order'),
    # 用户中心-地址页
    # url('^address$', login_required(AddressView.as_view()), name='address'),
    url('^address$', AddressView.as_view(), name='address'),
]

