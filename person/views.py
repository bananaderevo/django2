from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import UpdateView

from .forms import PersonForm
from .models import Person


class UpdateDetailView(UpdateView):
    model = Person
    template_name = 'person/index.html'
    context_object_name = 'person'
    fields = ['first_name', 'last_name', 'email']


def create(request):
    if request.method == 'POST':

        form = PersonForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('/person')

    # if a GET (or any other method) we'll create a blank form

    form = PersonForm()

    data = {
        'form': form
    }
    return render(request, 'person/index.html', data)
