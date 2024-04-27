from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #食物列表
    path('',views.index,name = 'index'),
    path('new',views.new,name = 'new'),
    #資料要進資料庫
    path('add',views.add,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    #產品各自顯示頁面
    path('<int:id>',views.show,name='show'),
]