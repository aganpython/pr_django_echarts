from django.urls import path

from app_sqlites import views, testdb, search, search2

urlpatterns = [
    path('', views.fyifu),
    # path('',views.fdianqi),
    # path('testdb/', tesdb.testdb, name="testdb"),
    # ('post/', search2.search_post,name="post"),
    # path('search_form/', search.search_form,name="search_form"),
    # path('', search.search),
    # path('index/', views.index),
    # path('',views.yifu),
    # path('', views.dianqi),

]
