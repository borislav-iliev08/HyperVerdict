from django.views.generic import TemplateView


class CommonHomeView(TemplateView):
    template_name = 'common/home.html'
