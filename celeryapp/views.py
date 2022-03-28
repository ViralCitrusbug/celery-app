from django.shortcuts import render,HttpResponse
from django.views import View
from .task import sleepy,send_email
# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'index.html')

class SendEmail(View):
    def get(self,request):
        return render(request,'send-email.html')
    
    def post(self,request):
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        receiver = request.POST.get('receiver')
        send_email(subject,body,receiver)
        context = {
            'response':'your Mail is Sent'
        }
        return render(request,'send-email.html',context)