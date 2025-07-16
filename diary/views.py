from django.shortcuts import render, redirect, get_object_or_404
from .forms import ThoughtForm
from django.contrib.auth.decorators import login_required
from .models import Thought

# Create your views here.


@login_required
def create(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.author = request.user
            thought.save()
            return redirect('diary:thoughts')
    else:
        form = ThoughtForm()
    return render(request, 'diary/create.html', {'form': form})


@login_required
def listed(request):
    thoughts = Thought.objects.filter(author=request.user).order_by('-date')
    return render(request, 'diary/thoughts.html', {'thoughts': thoughts})

@login_required
def view_thought(request, slug):
    thought = get_object_or_404(Thought, slug=slug, author=request.user)
    return render(request, 'diary/read.html', {'thought': thought})
