# -*- coding: utf-8 -*-

from django.http import HttpResponse

from app_sqlites.models import yifu


# 插入数据，可以插入一个字段，也可以插入两个字段，
# 访问 http://127.0.0.1:8000/testdb 就可以看到数据添加成功的提示。
# def testdb(request):
#     test1 = yifu(category='测试',salesnum='1000')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# 更新数据
def testdb(request):
    test1 = yifu.objects.get(id=2)
    test1.salesnum = 444
    test1.save()
    return HttpResponse("<p>数据修改成功！</p>")

# 删除数据
# def testdb(request):
#     # test1 = yifu.objects.get(id=7)
#     yifu.objects.filter(id=6).delete()
#     # test1.delete()
#     return HttpResponse("<p>数据删除成功！</p>")


# 展示数据 (一直有问题，无法模拟)
# def testdb(request):
#     b1 = yifu.objects.values('category')
#     b2 = yifu.objects.values('category', 'salesnum')
#     b3 = yifu.objects.all()
#     b8 = yifu.objects.filter(id=1).values("category","salesnum")
#     b9 = yifu.objects.get(id=2).category
#     print(b1)
#     print(b2)
#     print(b3)
#     print(b8)
#     print(b9)
#     b6 = ""
#     b7 = ""
#     for var in b3:
#         b4 = var.category
#         b5 = var.salesnum
#         b6 += var.category + ""
#         b7 = b6
#         print(b4, b5)
#     # return HttpResponse('value 方法的查询方法')
#     return HttpResponse("<p>" + b7 + "</p>")