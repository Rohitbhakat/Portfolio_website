from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
# Create your models here.
class Customer_detail(models.Model):
    name = models.CharField(max_length = 100)
    # subject = models.CharField(max_length = 100)
    date=models.DateTimeField(default=datetime.now, blank=True)
    message= models.TextField()
    number = models.BigIntegerField()
    email = models.CharField(max_length = 100)

class Product(models.Model):
    name = models.CharField(max_length = 100)
    img= fields.ImageField(upload_to = 'pics', dependencies=[
        FileDependency(attname='img=',processor=ImageProcessor(
            format='JPEG', scale={'max_width':500,'max_height':500})),
        
    ])
    img=  fields.ImageField(upload_to='pics')
    
    max_price = models.IntegerField()
    min_price = models.IntegerField()
    Price_display = models.BooleanField(default=False)
    specification = models.TextField()    
    detail_img= fields.ImageField(upload_to = 'pics', dependencies=[
        FileDependency(attname='img=',processor=ImageProcessor(
            format='JPEG', scale={'max_width':500,'max_height':500})),
        
    ])
    detail_img=  fields.ImageField(upload_to='pics')

class Upload_video(models.Model):
    video_name=models.CharField(max_length = 100)
    video_thumbnail=fields.ImageField(upload_to = 'pics', dependencies=[
        FileDependency(attname='video_thumbnail',processor=ImageProcessor(
            format='JPEG', scale={'max_width':500,'max_height':500})),
        
    ])
    video_thumbnail = fields.ImageField(upload_to='pics')
    videofile= models.FileField(upload_to='videos', null=True)
    video_description= models.TextField()
    # Display_onpage = models.BooleanField(default=False)

class Service(models.Model):
    title=models.CharField(max_length = 100)
    content=models.TextField()
    # para1 = models.TextField()
    read_more=models.TextField(blank=True)
    read_more_btn=models.BooleanField(default=False)

class Head_footer(models.Model):
    logo=models.ImageField(upload_to='pics')  
    logo_name_display = models.CharField(max_length = 50)
    Logo_img_display= models.BooleanField(default=False)
    prod_head=  models.CharField(max_length = 300, blank=True)  
    video_head = models.CharField(max_length = 300, blank=True)
    contact_head= models.CharField(max_length = 300, blank=True) 
    favicon = models.FileField(upload_to='svg') 
    my_email= models.CharField(max_length = 100)
    phn_number=models.CharField(max_length = 50, blank=True) 
    address=models.TextField()
    contact_parallax_img= fields.ImageField(upload_to = 'pics', dependencies=[
        FileDependency(attname='img',processor=ImageProcessor(
            format='JPEG', scale={'max_width':1920,'max_height':700})),
        
    ])
    contact_parallax_img = fields.ImageField(upload_to='pics')
    facebook_link = models.CharField(max_length = 100, blank=True) 
    # gif_404 = models.FileField(upload_to='pics', null=True)

class Vision_Mission(models.Model):
    scroll_text=models.CharField(max_length = 100, blank=True)
    vision_name=models.CharField(max_length = 100, blank=True)
    vision_subhead=models.CharField(max_length = 300, blank=True)  
    vision_parallax_img = fields.ImageField(upload_to = 'pics', dependencies=[
        FileDependency(attname='img',processor=ImageProcessor(
            format='JPEG', scale={'max_width':1920,'max_height':700})),
        
    ])
    vision_parallax_img = fields.ImageField(upload_to='pics')
# class footer(models.Model):

class Banner(models.Model):
    img=fields.ImageField(upload_to = 'pics', dependencies=[
        FileDependency(attname='img',processor=ImageProcessor(
            format='JPEG', scale={'max_width':1920,'max_height':700})),
        
    ])
    img = fields.ImageField(upload_to='pics')
    name=models.CharField(max_length = 100)

    head = models.CharField(max_length = 400)
    subhead = models.TextField()
    button_bool = models.BooleanField(default=False)


class about_us(models.Model):
    Name=models.CharField(max_length = 100)
    para1=models.TextField(blank=True)
    para2=models.TextField(blank=True)
    read_more_btn = models.BooleanField(default=False)
    # para3=models.TextField(blank=True)
    # features=models.CharField(max_length = 200, blank=True)    

class Seo_Meta(models.Model):
    meta_desc = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
