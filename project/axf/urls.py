from django.urls import re_path,path
from . import views
app_name='axf'

urlpatterns= [
    path('home/', views.home, name='home'),
    re_path(r'^market/(\d+)/(\d+)/(\d+)/$',views.market,name='market'),
    # path('market/', views.market, name='market'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
#     登陆
    path('login/',views.login,name='login'),
#     注册
    path('register/',views.register,name='register'),
#     验证账号是否被注册
    path('checkuserid/',views.checkuserid,name='checkuserid'),
#     退出登录
    path('quit/',views.quit,name='quit'),
#     修改购物车
#     path('changecart/',views.changecart,name='changecart'),
    re_path(r'^changecart/(\d+)/$', views.changecart, name="changecart"),

#     订单
    path('saveorder/',views.saveorder,name = "saveorder")
]