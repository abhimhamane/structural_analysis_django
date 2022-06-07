from statistics import variance
from tkinter import Variable
from unittest.util import _MIN_END_LEN
import sympy
from sympy.physics.continuum_mechanics import Beam

class SimpleBeamInstance():
    def __init__(self, id, length, E, Izz, lt_sprt, rt_sprt):
        self.Id = id
        self.L = length
        self.E = E
        self.Izz = Izz
        self.lt_sprt = lt_sprt
        self.rt_sprt = rt_sprt
    
    def create_sympy_beam(self):
        beam = Beam(self.L, self.E, self.Izz)
        beam.apply_support(0, self.lt_sprt)
        beam.apply_support(self.L, self.rt_sprt)
        #beam.apply_support_loads
        
        return beam
    
    def sympy_variable(x:str):
        return sympy.symbols(x)

    def apply_support_loads(self, beam):
        sympy_symbols = []
        if self.lt_sprt == "fix":
            R_0 = SimpleBeamInstance.sympy_variable("R_0")
            M_0 = SimpleBeamInstance.sympy_variable("M_0")
            sympy_symbols.append(R_0)
            sympy_symbols.append(M_0)
        else:
            R_0 = SimpleBeamInstance.sympy_variable("R_0")
            sympy_symbols.append(R_0)

        if self.rt_sprt == "fix":
            r_end = SimpleBeamInstance.sympy_variable("R_" + str(self.L))
            m_end = SimpleBeamInstance.sympy_variable("M_" + str(self.L))
            sympy_symbols.append(r_end)
            sympy_symbols.append(m_end)
        else:
            r_end = SimpleBeamInstance.sympy_variable("R_" + str(self.L))
            sympy_symbols.append(r_end)
        
        return sympy_symbols

        