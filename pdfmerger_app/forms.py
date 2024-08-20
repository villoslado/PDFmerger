from django import forms


class pdf_merge_form(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={"multiple": True, "accept": "application/pdf"}
        ),
        required=True,
        label="Upload PDFs (order matters)",
    )
