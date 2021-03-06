from django.utils.translation import ugettext as _
from django.http import HttpResponse
from darkoob.migration.forms import StartNewMigrationForm
from darkoob.book.models import Book
from darkoob.migration.models import Migration

import random
import string 
def generate_private_key(len=10):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(len))
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def start_new_migration(request):
    if request.method == 'POST':
        form = StartNewMigrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                book = Book.objects.get(title=cd['book'])
            except:
                return HttpResponse("this book no exist")
            else:
                private_key = generate_private_key()
                Migration.objects.create(book=book, starter=request.user,
                    starter_message=cd['starter_message'], private_key=private_key
                )
                # TODO:Redirect to this page 
                return render(request, 'migration/started.html', 
                    {'private_key': private_key, 'book': book}
                )
    else:
        form = StartNewMigrationForm()
    return render(request, 'migration/start_new_migration.html',{'form':form}) #{'form': form, })
