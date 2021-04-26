from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView
from neoclub.forms import PlayerForm, VisitForm
from neoclub.models import Player, Hall, Computers, Visit


def index(request):
    computers = Computers.objects.all()
    context = {'computers': computers}
    return render(request, 'club/index.html', context)


# Удаление/изменение/добавления записи игрока
class DeletePlayers(DeleteView):
    model = Player
    template_name = 'club/delete.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class EditPlayers(UpdateView):
    model = Player
    template_name = 'club/edit.html'
    form_class = PlayerForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('index')
    else:
        form = PlayerForm()
    template_name = 'club/create.html'
    context = {'form': form}
    return render(request, template_name, context)


def player_detail(request, pk):
    player = Player.objects.get(id=pk)
    visits = Visit.objects.filter(player_id=pk)
    context = {'player': player, 'visits': visits}
    return render(request, 'club/player_detail.html', context)


def player_list(request):
    players = Player.objects.all()
    return render(request, 'club/gamers_list.html', {'players': players})


def comp_detail(request, pk):
    computers = Computers.objects.get(id=pk)
    visits = Visit.objects.filter(computers_id=pk)
    context = {'computers': computers, 'visits': visits}
    return render(request, 'club/comp_detail.html', context)


def add_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('index')
    else:
        form = VisitForm()
    template_name = 'club/create.html'
    context = {'form': form}
    return render(request, template_name, context)
