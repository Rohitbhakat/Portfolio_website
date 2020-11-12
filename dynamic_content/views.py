from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from dynamic_content.models import Customer_detail, Product, Upload_video, Service, Banner, about_us, Vision_Mission, Head_footer, Seo_Meta
from django.views.decorators.csrf import csrf_exempt 
from django.core.mail import send_mail
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags\
# from django.shortcuts import render, redirect


def index(request):
    
    seo_bool= False
    prod_bool=False
    vision_bool= False
    video_bool=False
    service_bool=False
    banner_bool=False
    about_bool=False
    products = Product.objects.all()
    if products.count() !=0:
        prod_bool=True
    
    video= Upload_video.objects.all()
    if video.count() !=0:
        video_bool=True
    services = Service.objects.all()
    if services.count() !=0:
        service_bool=True
    banners=Banner.objects.all()
    if banners.count() !=0:
        banner_bool=True
    about= about_us.objects.all()
    if about.count() !=0:
        about_bool=True

    heading = Head_footer.objects.all()
    
    video= Upload_video.objects.all()
    if video.count() !=0:
        video_bool=True

    vision = Vision_Mission.objects.all()
    if vision.count() !=0:
        vision_bool =True

    seo = Seo_Meta.objects.all()
    if seo.count() !=0:
        seo_bool =True
    # print(vision)

    return render(request, 'index.html',{'products':products,'video':video,'services':services,
    'banners':banners,'about':about,'prod_bool':prod_bool,'video_bool':video_bool,'video':video,'service_bool':service_bool,
    'banner_bool':banner_bool, 'about_bool':about_bool, 'heading':heading, 'vision':vision,'vision_bool':vision_bool,'seo_bool':seo_bool,'seo':seo})

@csrf_exempt
def customer_info(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        number = request.POST.get('number')
        
        
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        myemail = Head_footer.objects.all()
        for i in myemail:
            mail= i.my_email
        # print(mail)
        # print(message)
        # print(name)
        # print(email)
        # print(message)
        # send mail
        # Sending Mail..........................
        try:
            html_content =render_to_string('email_template.html',{'name':name, 'message':message,'email':email,'number':number})
            text_content = strip_tags(html_content)
            newemail = EmailMultiAlternatives(
                'Customer Info',
                text_content,
                'Kusanagi.designs@gmail.com',
                [mail],
            )
            newemail.attach_alternative(html_content,'text/html')
            newemail.send()
            ####### End sending mail###########

            # Data entry#
            create_obj = Customer_detail.objects.create(name = name, message=message,email=email,number=number)
            create_obj.save()
            message='Hi '+str(name)+', we have received your message, will contact you soon'
            print(message)
            
            return HttpResponse(message)
        except Exception as e:
            print(e)
            message='Hi '+str(name)+', there is some issue please try again after some time'
            return HttpResponse(message)
    else:
        return redirect('/')


def handler404(request, exception):
    return render(request,'404.html')