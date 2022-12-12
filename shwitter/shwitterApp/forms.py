from django import forms
from .models import Shweet


class ShweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Shweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
        )



    class Meta:
        model = Shweet
        exclude = ("user", )
