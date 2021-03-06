from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.db.models import Q

from .forms import NewCallForm, UpdateCallForm, UpdateCallFormClient, NewCallFormClient, NoteFormClient
from .models import Call

def is_teammember(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 1


def is_customer(user=None):
    if not user or user.is_anonymous:
        return False
    return user.user_type == 2

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

@user_passes_test(is_customer)
def list_calls_client(request, user_id):
    calls = Call.objects.filter(customer_id=user_id).order_by("-id")
    return render(
        request,
        'calls/calls_list.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_customer)
def update_call_client(request, call_id):
    call = Call.objects.get(id=call_id)
    if request.method == 'POST':
        form = UpdateCallFormClient(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("calls:list_calls"))

    else:
        form = UpdateCallFormClient(instance=call)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Modification d'appel",
            'form':form,
        }
    )

@user_passes_test(is_customer)
def new_call_client(request):
    if request.method == 'POST':
        form = NewCallFormClient(request.POST)
        if form.is_valid():
            form.instance.customer = request.user.customer
            form.save()

    else:
        form = NewCallFormClient()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Nouvel Appel",
            'form':form,
        }
    )

@user_passes_test(is_teammember)
def list_calls_non_att(request):
    calls = Call.objects.filter(teammember__isnull=True).order_by("-id")
    return render(
        request,
        'calls/calls_list_non_att.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_teammember)
def update_teammember(request, call_id):
    call = Call.objects.get(id=call_id)
    call.teammember = request.user.teammember
    call.save()
    return HttpResponseRedirect(reverse("calls:list_calls"))

@user_passes_test(is_customer)
def list_calls_client_resolus(request, user_id):
    calls = Call.objects.filter(customer_id=user_id, solved=False, note='').order_by("-id")
    return render(
        request,
        'calls/calls_list_notes.html',
        {
            'calls': calls,
        }
    )

@user_passes_test(is_teammember)
def update_note(request, call_id):
    call = Call.objects.get(id=call_id)
    if request.method == 'POST':
        form = NoteFormClient(request.POST, instance=call)
        if form.is_valid():
            form.save()

    else:
        form = NoteFormClient()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Noter un appel",
            'form':form,
        }
    )


def calls_mal_notes(request):
    calls = Call.objects.filter(Q(note=0) | Q(note=1) | Q(note=2) | Q(note=3)).order_by("-id")
    return render(
        request,
        'calls/calls_list_bad_notes.html',
        {
            'calls': calls,
        }
    )