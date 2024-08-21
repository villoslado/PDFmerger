from django import forms


class pdf_merge_form(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"accept": "application/pdf"}),
        required=True,
        label="Upload PDF (upload one at a time)",
    )
