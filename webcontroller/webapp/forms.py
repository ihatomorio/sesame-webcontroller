from django import forms


class SesameForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=256,
        required=True,
    )

    auth_token = forms.CharField(
        label='Auth Token',
        max_length=76,
        required=True,
    )