from django.conf.urls import url
from django.urls import path

from App import views

urlpatterns=[
    path('home/', views.home, name= 'home'),
    path('add/', views.add, name= 'add'),
    path('add_ajax/.', views.add_ajax, name='add_ajax'),
    path('gy', views.gy, name='gy'),
    path('echarts_ncov_map/', views.echarts_ncov_map, name='echarts_ncov_map'),
    path('echarts_ncov_map_add/', views.echarts_ncov_map_add, name='echarts_ncov_map_add'),

    path('echarts_ncov_line/', views.echarts_ncov_line, name='echarts_ncov_line'),
    path('echarts_ncov_world/', views.echarts_ncov_world, name='echarts_ncov_world'),
    path('echarts_ncov_world_bar/', views.echarts_ncov_world_bar, name='echarts_ncov_world_bar'),


    path('get_ajax01/', views.get_ajax01, name= 'get_ajax01'),

    path('get_ajax02/', views.get_ajax02, name= 'get_ajax02'),

    path('chengyuindex/', views.chengyu_idnex, name = 'chengyuidnex'),

    path('chengyugame/', views.chengyu_name, name ='chengyugame'),

    path('chengyumore/', views.chengyu_more, name ='chengyumore'),


    path('car_logo/', views.car_logo, name = 'car_logo'),

    path('english_add/',views.english_add, name='english_add'),
    path('english_study/',views.english_study, name='english_study'),




]