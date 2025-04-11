from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import *
from userapp.models import *
from ssccb.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def admin_dashboard(request):
    pending=UserRegisration.objects.filter(status='pending').count()
    accepted=UserRegisration.objects.filter(status='Accepted').count()
    rejected=UserRegisration.objects.filter(status='Rejected').count()
    total=UserRegisration.objects.all().count()
    data=UserRegisration.objects.filter(status='pending')
    
    return render(request,'admin/admin-index.html',{'pending':pending,'accepted':accepted,'rejected':rejected,'total':total,'data':data})

def admin_cmastatus(request):
    data=UploadFiles.objects.filter(user_id__status='Accepted').all()
    
    return render(request,'admin/admin-user-datastatus.html',{'data':data})

def admin_userrequest(request):
    data=UserRegisration.objects.order_by('-user_id')
    
    return render(request,'admin/admin-user-request.html',{'data':data})

def user_accept(request,id):
        accept = get_object_or_404(UserRegisration,user_id=id)
        accept.status = 'Accepted'
        accept.save(update_fields=['status']) 
        accept.save()   
        html_content = "<br/><p>SSCCB Want to inform you that Your Regisration  Request is <b>accepted</b> by team of SSCCB as it is issued by a Codebook.in\
           <br>Thanks for your Resgistration</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [accept.email ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Your SSCCB Registration Status ", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
          if msg.send():
               print("Sent")
               return redirect('admin_userrequest')
        except: 
             return redirect('admin_userrequest')      
        return redirect('admin_userrequest')
    
def user_reject(request,id):
        reject = get_object_or_404(UserRegisration,user_id=id)
        reject.status = 'Rejected'
        reject.save(update_fields=['status']) 
        reject.save()   
        html_content = "<br/><p>SSCCB Want to inform you that Your Regisration  Request is <b>Rejected</b> by team of SSCCB as it is issued by a Codebook.in\
           <br>Thanks for your Resgistration</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [reject.email ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Your SSCCB Registration Status ", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
          if msg.send():
               print("Sent")
               return redirect('admin_userrequest')
        except: 
             return redirect('admin_userrequest')      
        return redirect('admin_userrequest')


# def (request):
    
    
#     return render(request,'admin/')

# def (request):
    
    
#     return render(request,'admin/')