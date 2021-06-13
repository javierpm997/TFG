#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 01, 2021 01:27:57 PM UTC  platform: Linux

import sys


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

import ModificarTipoAnalisis_support

def vp_start_gui(pIdTipoAnalisis):
    '''Starting point when module is the main routine.'''
    global val, w, root, idTipoAnalisis
    idTipoAnalisis = pIdTipoAnalisis
    root = tk.Tk()
    top = Toplevel1 (root)
    ModificarTipoAnalisis_support.init(root, top)
    root.mainloop()


w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    ModificarTipoAnalisis_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+508+105")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("Añadir Tipo de Análisis")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.117, rely=0.089, relheight=0.811
                , relwidth=0.758)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.TEntry1 = ttk.Entry(self.Frame1)
        self.TEntry1.place(relx=0.505, rely=0.329, relheight=0.058
                , relwidth=0.448)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="fleur")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.11, rely=0.329, height=21, width=69)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(text='''Nombre''')

        self.TEntry2 = ttk.Entry(self.Frame1)
        self.TEntry2.place(relx=0.505, rely=0.411, relheight=0.058
                , relwidth=0.448)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="xterm")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.11, rely=0.411, height=21, width=89)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(text='''Descripción''')


        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.747, rely=0.877, height=33, width=73)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(command=lambda:ModificarTipoAnalisis_support.ejecutar_Aceptar(idTipoAnalisis, self.TEntry1.get(),self.TEntry2.get()))
        self.Button1.configure(text='''Aceptar''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.527, rely=0.877, height=33, width=87)
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(command=lambda:ModificarTipoAnalisis_support.destroy_window())
        self.Button2.configure(text='''Cancelar''')

        tk.Label3 = tk.Label(self.Frame1)
        tk.Label3.place(relx=0.21, rely=0.658, height=21, width=429)
        tk.Label3.configure(activebackground="#f9f9f9")
        tk.Label3.configure(anchor='w')
        tk.Label3.configure(text='''Los campos vacíos no se modificarán''')

if __name__ == '__main__':
    vp_start_gui()





