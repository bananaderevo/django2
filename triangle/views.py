import math

from django.shortcuts import render

from .forms import TriangleForm


def triangle(request):
    gip = ''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TriangleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            gip = math.hypot(form.cleaned_data['angle'], form.cleaned_data['angle2'])
            return render(request, 'triangle/index.html', {'form': gip})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TriangleForm()

    data = {
        'form': form,
        'gip': gip,
    }

    return render(request, 'triangle/index.html', data)
