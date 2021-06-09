from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .models import Person
from .forms import PersonForm
from django.views.generic import DetailView, UpdateView


class UpdateDetailView(UpdateView):
    model = Person
    template_name = 'person/index.html'
    context_object_name = 'person'
    fields = ['first_name', 'last_name', 'email']


def create(request):
    if request.method == 'POST':

        form = get_object_or_404(PersonForm(request.POST), pk=id)

        if form.is_valid():

            form.save()
            return redirect('/person')

    # if a GET (or any other method) we'll create a blank form

    form = PersonForm()

    data = {
        'form': form
    }
    return render(request, 'person/index.html', data)





