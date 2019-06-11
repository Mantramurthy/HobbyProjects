from django.contrib import admin
from WebApp.models import OnlineOp
class OnlineOpAdmin(admin.ModelAdmin):
    list_display = ['id','Patient_Name','Mobile','Age','Gender','Timmings']
admin.site.register(OnlineOp,OnlineOpAdmin)