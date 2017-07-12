# ==== Using functions ====

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
#
# def index(request):
#     all_albums = Album.objects.all()
#     return render(request, 'music/index.html', {'all_albums' : all_albums})
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album' : album})

# ==== Using generic views ====

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
