from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from ecommerce.payment.forms import PaymentForm
from ecommerce.payment.forms import CardForm
from ecommerce.payment.models import Payment


@login_required
def payment_form(request,  *args, **kwargs):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user.card')
        else:
            form = PaymentForm()

    context = {
        "form": form
    }
    return render(request, 'details.html', context)


def card_details(request, *args, template_name="payment.html"):
    get_last_id = Payment.objects.latest('id').pk
    payment = get_object_or_404(Payment, pk=get_last_id)
    form = CardForm(request.POST or None, instance=payment)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your payment was successful!')
        return HttpResponseRedirect(request.path_info)
    else:
        form = CardForm()
    return render(request, template_name, {'form': form})
