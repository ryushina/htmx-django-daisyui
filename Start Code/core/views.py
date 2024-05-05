from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from core.models import Todo
from core.forms import TodoForm


@login_required
def index(request):
    context = {"todos": Todo.objects.filter(user=request.user), "form": TodoForm()}
    return render(request, "index.html", context)


@login_required
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        # return an html partial
        context = {"todo": todo}
        return render(request, "index.html#todoitem-partial", context)


@login_required
def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    context = {"todo": todo}
    return render(request, "index.html#todoitem-partial", context)
