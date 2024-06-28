from django.db import models

# Create your models here.

class Task(models.Model):
    class Meta:
        db_table = "tasks"
        
    title = models.CharField(verbose_name="タスク名", max_length=255)
    
    description = models.TextField(verbose_name="詳細", null=True, blank=True)
    
    complete = models.IntegerField(verbose_name="完了フラグ", default=0)
    
    start_date = models.DateTimeField(verbose_name="開始日", null=True, blank=True)
    
    end_date = models.DateTimeField(verbose_name="終了日", null=True, blank=True)
    
    def __str__(self):
        return self.title