from django.forms import ModelForm

from neoclub.models import Player, Visit


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'last_name', 'nick_name')


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ('player', 'time', 'computers')
