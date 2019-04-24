from django.contrib import admin
from app_sqlites.models import yifu, dianqi


# Register your models here.
class YifuAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "salesnum"]
    # 添加一个链接，可以链接到具体的位置
    list_display_links = ["category", "salesnum"]
    # 定义每页可以显示10行
    list_per_page = 10


admin.site.register(yifu, YifuAdmin)


class DianqiAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "salesnum"]
    # 添加一个链接，可以链接到具体的位置
    list_display_links = ["category", "salesnum"]
    # 定义每页可以显示10行
    list_per_page = 10


admin.site.register(dianqi, DianqiAdmin)
