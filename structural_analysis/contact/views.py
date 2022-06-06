from django.shortcuts import render
from django.http import HttpResponse

from contact.forms import FeedbackForm

# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')

def feedback(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data.get('name')
            print(name)
            return HttpResponse("Thanks")
            # redirect to a new URL:
            #return HttpResponse("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'contact/contact.html', {'form': form})