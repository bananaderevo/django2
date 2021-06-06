from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from faker import Faker

from .forms import ArticlesForm
from .models import Articles, createpassword

fake = Faker()


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Articles.objects.last()
            field_object = Articles._meta.get_field('text')
            user_number = int(field_object.value_from_object(obj))
            for i in range(user_number):
                User.objects.create_user(username=fake.name().replace(' ', '').lower(),
                                        email=fake.name().replace(' ', '') + '@gmail.com',
                                        password=createpassword())
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'CreateRandUsers/create.html', data)
