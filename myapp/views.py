# python first
# django second
# your apps
# local directory


from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from django.shortcuts import render, render_to_response
from myapp.forms import ContactForm

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


#send_mail(
    #'Subject here',
    #'Here is the message.',
    #'from@example.com',
   # ['to@example.com'],
  #  fail_silently=False,
#)

"""
from appName.forms import formName  # dont forget to import the form
from django.views.generic import TemplateView
from portfolio.models import Experience
"""

# Create your views here.


def index(request):
    return render_to_response('index.html')
    return render_to_response('project1.html')


def contact(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = "First confirmation Reach out"
        message = "Hope this works fine"
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_form.email, settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to_list, fail_silently=True)

        messages.success(request, "Thank you for your message!")
        return render_to_response('index.html')

    return render_to_response('index.html')


"""
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site Contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'otheremail@gmail.com']
        contact_message = "%s : %s via %s" % (
            form_full_name,
            form_message,
            form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  fail_silently=False)  # True if wanting to save to db
        context = {
            "form": form,
        }
    return render(request, 'index.html', context)


# new imports that go at the top of the file

# our view


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })


"""
