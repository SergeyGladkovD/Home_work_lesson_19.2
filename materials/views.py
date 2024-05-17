from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from materials.models import Material


# Create your views here.
class MaterialCreateView(CreateView):
	model = Material
	fields = ('title', 'slug', 'content', 'preview', 'created_at')
	success_url = reverse_lazy('materials:list')


class MaterialUpdateView(UpdateView):
	model = Material
	fields = ('title', 'slug', 'content', 'preview', 'created_at')
	success_url = reverse_lazy('materials:list')


class MaterialListView(ListView):
	model = Material


class MaterialDetailView(DetailView):
	model = Material


class MaterialDeleteView(DeleteView):
	model = Material
	success_url = reverse_lazy('materials:list')
