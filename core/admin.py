from django.contrib import admin
from .models import GeneralSetting, ImageSetting,Skills,Experience
# Register your models here.




@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','paramater','created_date','updated_date']
    list_editable=['name','paramater']

    class Meta:
        verbose = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):
    list_display=["id","name","description","file"]
    

    class Meta:
        verbose = ImageSetting

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display=["id","order","name","percentage"]
    list_editable=["name","percentage"]
    

    class Meta:
        verbose = Skills

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=["id","company_name","job_title","job_location","start_date","end_date","updated_date","created_date"]

    class Meta:
        verbose = Experience
