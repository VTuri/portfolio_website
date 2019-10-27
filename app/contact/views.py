from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
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
                email = EmailMessage(contact_name,
                                     content,
                                     contact_email,
                                     ["wajkoo.sers@gmail.com"],  # TODO change it for prod
                                     reply_to=[contact_email]
                                     )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thx')
    return render(request, "contact.html", {"form": form})


def thx(request):
    return render(request, 'thx.html')
