from django.contrib import admin
from .models import Board,Task
# Register your models here.
class BoardModelAdmin(admin.ModelAdmin):
    list_display = ('id','Board_Name','Color')

admin.site.register(Board, BoardModelAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','Board_id','task_name','current_status']

admin.site.register(Task,TaskAdmin)
