from django.shortcuts import render
from . import models, forms, parser_rezka
from django.views import generic
from django.http import HttpResponse


class RezkaView(generic.ListView):
    template_name = 'rezka/rezka_list.html'
    context_object_name = 'rezka'
    model = models.Rezka

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RezkaFormView(generic.FormView):
    template_name = 'rezka/rezka_form.html'
    form_class = forms.ParsingForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('200 Ok')
        else:
            return super(RezkaFormView, self).post(request, *args, **kwargs)
