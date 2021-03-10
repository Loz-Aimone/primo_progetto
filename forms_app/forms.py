from django import forms
class formContatto(forms.Form):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "area testuale: scrivi pure!","background-color: BLACK", "color: white"}))
