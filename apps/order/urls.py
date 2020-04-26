from django.conf.urls import url
from order.views import OrderPlaceView, OrderCommitView, OrderPayView, CheckPayView, CommentView

urlpatterns = [
    # 提交订单页面显示
    url('^place$', OrderPlaceView.as_view(), name='place'),
    # 订单创建
    url('^commit$', OrderCommitView.as_view(), name='commit'),
    # 订单支付
    url('^pay$', OrderPayView.as_view(), name='pay'),
    # 查询支付交易结果
    url('^check$', CheckPayView.as_view(), name='check'),
    # 订单评论
    url('^comment/(?P<order_id>.+)$', CommentView.as_view(), name='comment')
]

