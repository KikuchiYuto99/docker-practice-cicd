from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["title"].widget.attrs = {'placeholder': 'タスク名'}
        self.fields["description"].widget.attrs = {'placeholder': '詳細'}
        
    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date and start_date < timezone.now():
            raise ValidationError("開始日を過去に設定することはできません。")
        
        return start_date
    
    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if end_date and end_date < timezone.now():
            raise ValidationError("終了日を過去に設定することはできません。")
        
        return end_date
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and end_date < start_date:
            self.add_error('end_date', '終了日は開始日より後の日付を設定する必要があります。')