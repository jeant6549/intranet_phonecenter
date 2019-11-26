from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

from .forms import NewCallForm, UpdateCallForm
from .models import Call

def is_teammember(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 1

@user_passes_test(is_teammember)
def new_call(request):
    if request.method == 'POST':
        form = NewCallForm(request.POST)
        if form.is_valid():
            form.instance.teammember = request.user.teammember
            form.save()

    else:
        form = NewCallForm()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Nouvel Appel",
            'form':form,
        }
    )

@user_passes_test(is_teammember)
def list_calls(request):
    calls = Call.objects.order_by("-id")
    return render(
        request,
        'calls/calls_list.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_teammember)
def update_call(request, call_id):
    call = Call.objects.get(id=call_id)
    if request.method == 'POST':
        form = UpdateCallForm(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return redirect('../../list_calls')

    else:
        form = UpdateCallForm(instance=call)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Modification d'appel",
            'form':form,
        }
    )

@user_passes_test(is_teammember)
def delete_call(request, call_id):
    call = Call.objects.get(id=call_id).delete()
    return redirect('../../list_calls')