from django.conf.urls import url
from cart.views import CartAddView, CartInfoView, CartUpdateView, CartDeleteView

urlpatterns = [
    # 购物车记录添加
    url('^add$', CartAddView.as_view(), name='add'),
    # 购物车页面显示
    url('^$', CartInfoView.as_view(), name='show'),
    # 购物车记录更新
    url('^update$', CartUpdateView.as_view(), name='update'),
    # 购物车记录删除
    url('^delete$', CartDeleteView.as_view(), name='delete'),

]


