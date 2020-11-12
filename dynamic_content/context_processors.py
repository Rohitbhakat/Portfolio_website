from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from dynamic_content.models import Customer_detail, Product, Upload_video, Service, Banner, about_us, Vision_Mission, Head_footer, Seo_Meta
from django.views.decorators.csrf import csrf_exempt 
from django.core.mail import send_mail
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags\


def add_variable_to_context(request):
    heading = Head_footer.objects.all()
    return {'heading':heading}