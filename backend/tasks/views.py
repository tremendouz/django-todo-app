from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    #return HttpResponse("hello")
    return render(request, "home.html", {"html_var": "VAR"})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"html_var": "CLASS_BASED_VAR"}
        return render(request, "home.html", context)
    
class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(*args, **kwargs)
        context = {"html_var": "CLASS_BASED_VAR"}
        return context
