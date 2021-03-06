import email
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from contact.forms import FeedbackForm

from .forms import NameForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data.get('name')

            # redirect to a new URL:
            return HttpResponse("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'blog/name.html', {'form': form})