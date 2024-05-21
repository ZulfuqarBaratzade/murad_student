from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class UpdateDateCreateDate(models.Model):
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Create Date"
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date"
    )
    class Meta:
        abstract = True

class GeneralSetting(UpdateDateCreateDate):
    name = models.CharField(
        default="",
        max_length=100,
        blank=True,
        help_text='This is for name',
    )
    description=models.CharField(
        default="",
        max_length=254,
        blank=True,
    )
    paramater=models.CharField(
        default="",
        max_length=100,
        blank=True,
    )

    class Meta:
        verbose_name = "General Settings"
        verbose_name_plural = "General Settings"
        ordering =("name","paramater")




class ImageSetting(UpdateDateCreateDate):
   name = models.CharField(
        default="",
        max_length=100,
        blank=True,
        help_text='This is for name',
    )
   description=models.CharField(
        default="",
        max_length=254,
        blank=True,
    )
   file=models.ImageField(
       default="",
       blank=True,
       verbose_name="Image",
       upload_to='img/')
   class Meta:
        verbose_name = "Image Settings"
        verbose_name_plural = "Image Settings"
        ordering =("file", )
    
class Skills(UpdateDateCreateDate):
    order=models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    name = models.CharField(
        default="",
        blank=True,
        max_length=100,
        verbose_name="Name",
        help_text="This is for name",
    )
    percentage=models.IntegerField(
        default=50,
        verbose_name="Percantage",
        validators=[MinValueValidator(0),MaxValueValidator(100)]
    )
    def __str__(self):
        return f"Skills: {self.name}"
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ("order",)



class Experience(UpdateDateCreateDate):
    company_name = models.CharField(
        default="",
        blank=True,
        max_length=100,
        verbose_name="company name",
    )
    job_title = models.CharField(
        default="",
        blank=True,
        max_length=100,
        verbose_name="job title",
    )
    job_location=models.CharField(
        default="",
        blank=True,
        max_length=100,
        verbose_name="Job Location",
    )
    start_date = models.DateField(
        verbose_name="Start Date"
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date"
    )
    def __str__(self):
        return f"Experience : {self.company_name}"


    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience"
        ordering = ("start_date"),