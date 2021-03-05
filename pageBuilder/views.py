from django.shortcuts import render


# Create your views here.


def index(request):
    template = 'pageBuilder/newPage.html'
    context = {}
    context['title'] = "ساخت صفحه ی جدید"
    return render(request, template, context)
