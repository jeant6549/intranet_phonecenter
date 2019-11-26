from django import forms

from users.forms import ModelFormWithSubmit
from .models import Call, CallTag, CallNote


class NewCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'customer', 'tags', 'content', 'solved', )

class UpdateCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'customer', 'teammember', 'tags', 'content', 'solved', )


class UpdateCallFormClient(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    note = forms.ModelChoiceField(
        widget=forms.RadioSelect,
        queryset=CallNote.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'customer', 'tags', 'content', 'note' ,'solved', )


class NewCallFormClient(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'tags', 'content', )