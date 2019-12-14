from django.conf import settings
from django.core.mail import BadHeaderError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


# Create your views here.
def contact(request):
    if request == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']

            try:
                # email = EmailMessage(contact_name,
                #                      content,
                #                      contact_email,
                #                      ["wajkoo.sers@gmail.com"],
                #                      reply_to=[contact_email])
                # email.send()
                subject = 'PORTFOLIO MESSAGE'
                message = "CONTACT_NAME: " + contact_name + "\nCONTACT_EMAIL: " + contact_email + "\n\n\n" + \
                          "CONTENT: \n" + content
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ["turi.vajk@gmail.com", ]

                send_mail(subject, message, email_from, recipient_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thx')
    return render(request, "contact.html", {"form": form})


def thx(request):
    return render(request, 'thx.html')
