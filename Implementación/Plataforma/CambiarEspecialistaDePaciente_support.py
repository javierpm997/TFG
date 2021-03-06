#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 07, 2021 03:28:02 PM UTC  platform: Linux

import sys
from Plataforma import Plataforma
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root, mPlataforma
    mPlataforma = Plataforma()
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def cambiarEspecialistaDePaciente(pIdPaciente, pIdEspecialista):
    mPlataforma.cambiarEspecialistaDePaciente(pIdPaciente, pIdEspecialista)
    top_level.quit()
    destroy_window()

if __name__ == '__main__':
    import CambiarEspecialistaDePaciente
    CambiarEspecialistaDePaciente.vp_start_gui()




