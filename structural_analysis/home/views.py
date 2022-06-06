from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'home/index.html')

def sympyIpy(request):
    return render(request, 'home/sympy_beam_workflow.html')