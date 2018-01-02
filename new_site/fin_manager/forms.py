from django import forms
from models import Wallets
class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallets
        fields = ('name', 'description')

    def save(self, user=None):
        wallet_form = super(WalletForm, self).save(commit=False)
        if user:
            wallet_form.owner_id = user
        wallet_form.save()
        return wallet_form



