from django import forms

from base.models import ID_CARD_LENGTH

MAX_LENGTH = 100

class CardForm(forms.Form):
    """
    Form to take card data and input into model.
    """
    name = forms.CharField(label="Name", max_length=MAX_LENGTH)
    id_number = forms.CharField(label="Student ID", min_length=ID_CARD_LENGTH, max_length=ID_CARD_LENGTH)
    picture = forms.FileField(label="Picture")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=MAX_LENGTH)
    email = forms.EmailField()

class MarkFound(forms.Form):
    """
    Marks card as found and inactive.
    """
    password = forms.CharField(label="Password", widget=forms.PasswordInput, max_length=MAX_LENGTH)
