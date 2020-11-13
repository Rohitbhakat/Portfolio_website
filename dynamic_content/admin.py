from django.contrib import admin

from dynamic_content.models import Customer_detail, Product, Upload_video, Service, Banner, about_us, Head_footer, Vision_Mission,Seo_Meta
# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import Group

# admin.site.unregister(Group)

class Customer_detailAdmin(admin.ModelAdmin):
    list_display=('id','name','number','email')
    list_per_page=5

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','specification')

class Upload_videoAdmin(admin.ModelAdmin):
    list_display=('video_name','videofile') 

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','content')

class about_usAdmin(admin.ModelAdmin):
    list_display=('Name','para1')
    # def has_add_permission(self,request, obj=None):
    #     return False     
    # def has_delete_permission(self, request, obj=None):
    #     return False

class Head_footerAdmin(admin.ModelAdmin):
    list_display=('logo_name_display', 'logo')
    # def has_add_permission(self,request, obj=None):
    #     return False

class Seo_MetaAdmin(admin.ModelAdmin):
    def has_add_permission(self,request,obj=None):
        return False

class Vision_MissionAdmin(admin.ModelAdmin):
    list_display=(  'vision_name', 'vision_subhead')
    # def has_add_permission(self,request, obj=None):
    #     return False
# class Seo_MetaAdmin(admin.ModelAdmin):



admin.site.register(Product, ProductAdmin)
admin.site.register(Upload_video, Upload_videoAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Banner)
# admin.site.register(MultiplePricing, MultiplePricingAdmin)
admin.site.register(about_us, about_usAdmin)
# admin.site.register(Servicedetail, ServicedetailAdmin)
admin.site.register(Head_footer, Head_footerAdmin)
# admin.site.register(Media_link ,Media_linkAdmin)
# admin.site.register(Application, ApplicationAdmin)
admin.site.register(Vision_Mission, Vision_MissionAdmin)
admin.site.register(Seo_Meta, Seo_MetaAdmin)
admin.site.register(Customer_detail, Customer_detailAdmin)