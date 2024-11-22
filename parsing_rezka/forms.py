from django import forms
from . import models, parser_rezka


class ParsingForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka', 'rezka'),
    )
    media_types = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_types']

    def parser_data(self):
        if self.data['media_types'] == 'rezka':
            rezka_pars = parser_rezka.parsing()
            for i in rezka_pars:
                models.Rezka.objects.create(**i)
