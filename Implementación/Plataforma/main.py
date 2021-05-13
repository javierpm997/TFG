# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Plataforma import Plataforma;
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    plataforma = Plataforma()
    a = plataforma.anadirUsuarioPaciente(pContrasena='key1',pEmail='prueba2', pNombre='Prueba', pApellidos='Pruebomez', pEspecialista='1')
    print(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
