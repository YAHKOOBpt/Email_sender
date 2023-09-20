from django.shortcuts import render,redirect

from .models import *
from django.conf import settings
from django.core.mail import EmailMessage
# from django.core.mail.backends import EmailMessage



# Create your views here.
def index(request):
    if request.method == "POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        city=request.POST.get('city')
        code=request.POST.get('code')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        file = request.FILES.get('file')

        obj =Todo(name=name, address=address,city=city,post=code,phone=phone,email=email,document_name=file)
        obj.save()
        # if file is not None:
        message = 'Dear {},\n we are lointment with Dr.{} on {} '.format(name,address,city)
        email = EmailMessage(
            "subject of email",
            message,
            settings.EMAIL_HOST_USER,
            ['yahkoobmonu@gmail.com']
            
        )
        email.attach(
            file.name,
            file.read(),
            file.content_type
                
        )
        email.send()
        # return redirect('success_page')
    return render(request,'index.html')
        # ... rest of the code ...
        # else:
        #     print("No file uploaded")
        
   
    
