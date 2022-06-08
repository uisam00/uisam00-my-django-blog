from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    send = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # enviar email
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        send = True
        email = EmailMessage(
            "Mensagem do Blog Django",
            "De {} <{}> Escreveu: \n\n{}".format(name,email,message),
            "nao-responder@inbox.mailtrap.io",
            ["uisam.santos@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False
    context = {
        'form': ContactForm,
        'success': send
    }
    return render(request, 'contact/contact.html', context)

