from django import forms


class CompressForm(forms.Form):
    message = forms.CharField(label='message to decompress', max_length=1000, widget=forms.TextInput(
        attrs={'placeholder': 'message', 'class': 'custom-input'}))
