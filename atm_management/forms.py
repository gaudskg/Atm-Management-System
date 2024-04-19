from django import forms
from .models import ATMSite

class ATMSiteForm(forms.ModelForm):
    class Meta:
        model = ATMSite
        fields = ['name', 'site_id', 'address', 'city', 'contact_details']