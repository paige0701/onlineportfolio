from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.
from django.template.loader import render_to_string


def home(request):
    return render(request,'home.html')

def sendemail(request):


    if request.method=='POST':
        subject = 'Email from ' + request.POST.get('name')
        # message = render_to_string('auth/account_activation_email.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': account_activation_token.make_token(user),
        # })
        # user.email_user(subject,message, settings.DEFAULT_FROM_EMAIL)
        message=request.POST.get('comments')
        from_email = request.POST.get('email')
        receiver = ['paigechoi0701@gmail.com',]
        # to_list = [from_email,settings.EMAIL_HOST_USER]
        # to_list = [user.email,settings.EMAIL_HOST_USER]
        # send_mail(subject, message, from_email, receiver)
        send_mail(subject, message, from_email, ['cde0701@gmail.com'])

        # print("current site = ", current_site)
        # return redirect('account_activation_sent')

        # return redirect('accountactivationsent')

        return redirect(home)