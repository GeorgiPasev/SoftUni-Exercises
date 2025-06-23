from django import forms
from django.core.exceptions import ValidationError

from Organizer.models import Organizer


class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'
        widgets = {
            'secret_key': forms.PasswordInput(),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        qs = Organizer.objects.filter(phone_number=phone)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("That phone number is already in use!")
        return phone