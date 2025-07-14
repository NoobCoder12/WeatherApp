from django.shortcuts import render, redirect
from .forms import ThoughtForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.author = request.user
            thought.save()
            return redirect('my-thoughts')
    else:
        form = ThoughtForm()
    return render(request, 'diary/create.html', {'form': form})
