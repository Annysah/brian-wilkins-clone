from django.shortcuts import render

from django.core.mail import send_mail

# Create your views here.
def home(request):
    '''displays the home page'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
        'Django Test',
        f'Name: {name}\n\nEmail: {email}\n\nMessage: {message}',
        'mydjango58@gmail.com',
        ['anisatakinb@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'index.html')