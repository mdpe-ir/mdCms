from django.shortcuts import render, get_object_or_404

# Create your views here.
from pageBuilder.models import PagesModel


def index(request, slug):
    context = {}
    template = 'home/index.html'

    page = get_object_or_404(PagesModel, slug=slug)

    context['title'] = page.title
    context['content'] = page.html

    return render(request, template, context)
