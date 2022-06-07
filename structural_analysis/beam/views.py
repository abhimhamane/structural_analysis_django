from django.shortcuts import render, redirect
from beam.forms import BeamInput

from beam.bs_logic import SimpleBeamInstance

# Create your views here.
def home(request):
    return render(request, 'beam/home.html')

def create_beam(request):
    html_name = 'beam/create_beam.html'
    form = BeamInput()
    if request.method == 'POST':
        form = BeamInput(request.POST)
        if form.is_valid():
            beam_obj = form.save()
            beam_id = beam_obj.pk
            beam_length = float(beam_obj.beam_length)
            beam_E = float(beam_obj.beam_E)
            beam_Izz = float(beam_obj.beam_Izz)
            beam_left_support = str(beam_obj.beam_left_support)
            beam_right_support = str(beam_obj.beam_right_support)

            b1 = SimpleBeamInstance(beam_id, beam_length, beam_E, beam_Izz, beam_left_support, beam_right_support)
            beam1 = b1.create_sympy_beam()
            sympy_symbols = b1.apply_support_loads(beam1)
            
            print(sympy_symbols)
            print(type(sympy_symbols[0]))
            form = BeamInput(request.POST)
            
            return render(request, 'beam/create_beam.html', {'form': form})
    form = BeamInput()
    args = {'form': form}
    return render(request, html_name, args)
