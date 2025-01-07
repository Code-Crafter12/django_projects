from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request')

        try:
            booking = ServiceBooking.objects.create(
                name=name,
                email=email,
                service=service,
                service_date=service_date,
                special_request=special_request
            )
            booking.send_sms_notification()
            messages.success( request, 'Your service has been booked. The owner will be notified.')

        except Exception as e:
            print("Error creating booking:", e)
            return messages.error(request, 'Failed to book service. Please try again.', status=400)

    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request')

        try:
            booking = ServiceBooking.objects.create(
                name=name,
                email=email,
                service=service,
                service_date=service_date,
                special_request=special_request
            )
            booking.send_sms_notification()
            messages.success( request, 'Your service has been booked. The owner will be notified.')

        except Exception as e:
            print("Error creating booking:", e)
            return messages.error(request, 'Failed to book service. Please try again.', status=400)

    return render(request, 'core/service.html')

def technicians(request):
    return render(request, 'core/technicians.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        
        try:
            send_mail(
                subject,
                full_message,
                email,
                ['shahidareeba174@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
        except Exception:
            messages.error(request, 'Error sending message. Please try again.')
        
        return render(request, 'core/contact.html')

    return render(request, 'core/contact.html')