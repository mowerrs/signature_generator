from django import forms


class SignatureForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    title = forms.CharField(
        label="Title",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    division = forms.CharField(
        label="Division",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    phone = forms.CharField(
        label="Phone",
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
