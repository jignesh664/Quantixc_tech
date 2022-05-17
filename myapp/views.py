from django.shortcuts import render

from .models import Contact

# for flash massages
from django.contrib import messages
# for mail 
from django.conf import settings 
from django.core.mail import send_mail 
# Create your views here.



def index(request):
    return render(request,'index.html')

def contact(request):
	if request.method=="POST":
		user=Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message']

			)
					
		subject = 'Welcome to QuantixCube Technologies'
		message = f'Dear {user.name}, Greating from QuantixCube Technologies,Thanks for intresting with us,we contact shortly!!'                                                                                    
		email_from = settings.EMAIL_HOST_USER 
		recipient_list = [request.POST['email'],]
		send_mail( subject, message, email_from, recipient_list ) 

		messages.success(request,'Your message has been sent,Thank you! Will Reach You Soon!!!')
		return render(request,'index.html')
	else:
		return render(request,'index.html')		


	