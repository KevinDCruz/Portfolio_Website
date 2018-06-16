from django.shortcuts import render, render_to_response
from myapp.forms import ContactForm

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


# Create your views here.


def index(request):
    return render_to_response('index.html')
    return render_to_response('project1.html')


def contact(request):
    form_class = ContactForm
    return render(request, 'index.html', {'form': form_class})


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
