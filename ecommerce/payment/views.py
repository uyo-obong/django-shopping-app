from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from ecommerce.payment.forms import PaymentForm


@login_required
def payment_form(request,  *args, **kwargs):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.core')
        else:
            form = PaymentForm()

    context = {
        "form": form
    }
    return render(request, 'details.html', context)


def card_details(request):
    form = {}
    return render(request, 'payment.html', form)