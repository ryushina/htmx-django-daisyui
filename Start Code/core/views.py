from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Todo
from core.forms import TodoForm


@login_required
def index(request):
    context = {"todos": Todo.objects.filter(user=request.user), "form": TodoForm()}
    return render(request, "index.html", context)
