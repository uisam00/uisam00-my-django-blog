from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome completo'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Digite seu e-mail'}))
    message = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={'placeholder': 'Assunto'}))
