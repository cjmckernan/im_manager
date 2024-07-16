from django import forms


class CreditCardForm(forms.Form):
    card_number = forms.CharField(
        label="Card Number",
        max_length=16,
        widget=forms.TextInput(attrs={"placeholder": "Card Number"}),
    )
    expiry_date = forms.CharField(
        label="Expiry Date (MM/YY)",
        max_length=5,
        widget=forms.TextInput(attrs={"placeholder": "MM/YY"}),
    )
    cvv = forms.CharField(
        label="CVV",
        max_length=3,
        widget=forms.PasswordInput(attrs={"placeholder": "CVV"}),
    )
    cardholder_name = forms.CharField(
        label="Cardholder Name",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Cardholder Name"}),
    )
