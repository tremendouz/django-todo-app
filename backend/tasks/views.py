from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Task

# Create your views here.


def home(request):
    # return HttpResponse("hello")
    return render(request, "home.html", {"html_var": "VAR"})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"html_var": "CLASS_BASED_VAR"}
        return render(request, "home.html", context)


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(
            *args, **kwargs)
        context = {"html_var": "CLASS_BASED_VAR"}
        return context


def tasks_listview(request):
    template_name = 'tasks/tasks_list.html'
    queryset = Task.objects.all()
    #context = {"object_list": [1, 4, 523, 21312, 2]}
    context = {"object_list": queryset}
    return render(request, template_name, context)


class SearchTaskListView(ListView):
    template_name = 'tasks/tasks_list.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Task.objects.filter(
                Q(title__iexact=slug)
            )
        else:
            queryset = Task.objects.none()
        return queryset

    def get_context_data(self, *args, **kwargs):
        # print(self.kwargs)
        context = super(SearchTaskListView, self).get_context_data(
            *args, **kwargs)
        print("CONTEXT")
        print(context)
        return context


class TaskDetailView(DetailView):
    queryset = Task.objects.all()

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(TaskDetailView, self).get_context_data(*args, **kwargs)
        print("CONTEXT")
        print(context)
        return context
