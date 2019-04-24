from django.shortcuts import render
from app_sqlites.models import yifu, dianqi
from django.views.generic.base import TemplateView


# django 中的数据可以渲染到Html页面上
def fyifu(request):
    # 获取文章数据
    yifus = yifu.objects.all()
    # salesproducts = Salesproduct.objects.all().order_by("-salesnum")
    # print(salesproducts)
    # 将数据传递给页面
    context = {
        "yifus": yifus
    }
    return render(request, "index.html", context=context)


def fdianqi(request):
    dianqis = dianqi.objects.all()
    context = {
        "dianqis": dianqis
    }
    return render(request, "index.html", context=context)

# def index(request):
#     return render(request, 'index.html')

# def index(request):
#     #数据库查询数据，传递给模板进行解析
#     data1="我是数据1"
#     data2={"name":"我是数据2"}
#     data3=["周一","周二","周三"]
#
#     #使用模板
#     #context 上下文，格式必须是字典
#     context = {
#         "d1":data1,
#         "d2":data2,
#         "d3":data3
#     }
#     return render(request, 'index.html',context)
