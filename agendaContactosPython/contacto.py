import csv


class Contacto:
    def __init__(self, nombre, movil, mail):
        self.nombre = nombre
        self.movil = movil
        self.mail = mail


class Agenda:
    def __init__(self):
        self.__contactos = []

    def agregar_contacto(self, nombre, movil, mail):
        contacto = Contacto(nombre, movil, mail)
        self.__contactos.append(contacto)
        self.__guardar()

    def eliminar_contacto(self, nombre):
        for index, c in enumerate(self.__contactos):
            if c.nombre.lower() == nombre.lower():
                del self.__contactos[index]
                self.__guardar()
                break

    def mostrar_agenda(self):
        for c in self.__contactos:
            self.__print_contactos(c)

    def buscar_contacto(self, nombre):
        for c in self.__contactos:
            if c.nombre.lower() == nombre.lower():
                self.__print_contactos(c)
                return c
                break
        else:
            self.no_encontrado()

    def no_encontrado(self):
        print('Ese contacto no existe!')
        return False

    def actualizar_contacto(self, nombre):
        for c in self.__contactos:
            if c.nombre.lower() == nombre.lower():
                datos = self.introducir_datos()
                c.nombre = datos[0]
                c.movil = datos[1]
                c.mail = datos[2]
                break
        else:
            self.no_encontrado()

    def __guardar(self):
        with open('contactos.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('nombre', 'movil', 'mail'))

            for c in self.__contactos:
                writer.writerow((c.nombre, c.movil, c.mail))

    def __print_contactos(self, c):
        print(f'\nNombre: {c.nombre}\nMovil: {c.movil}\nMail: {c.mail}')

    def introducir_datos(self):
        nombre = str(input('Escribe el nombre del contacto: '))
        movil = str(input('Escribe movil del contacto: '))
        mail = str(input('Escribe mail del contacto: '))
        return nombre, movil, mail

    def leer_csv(self):
        with open('contactos.csv', 'r') as f:
            leer = csv.reader(f)
            for index, row in enumerate(leer):
                if index == 0:
                    continue
                self.agregar_contacto(row[0], row[1], row[2])

def run():

    agenda = Agenda()

    agenda.leer_csv()

    while True:
        tecla_pulsada = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [m]ostar contactos
            [s]alir
        '''))

        if tecla_pulsada == 'a':
            print('Añadir contacto')
            datos = agenda.introducir_datos()
            agenda.agregar_contacto(datos[0], datos[1], datos[2])

        elif tecla_pulsada == 'ac':
            print('Actualizar contacto')
            nombre = str(
                input('Escribe el nombre del contacto para Actualizar: '))
            agenda.actualizar_contacto(nombre)

        elif tecla_pulsada == 'b':
            print('Buscar contacto')
            nombre = str(input('Escribe el nombre del contacto a Buscar: '))
            agenda.buscar_contacto(nombre)

        elif tecla_pulsada == 'e':
            print('Eliminar contacto')
            nombre = str(input('Escribe el nombre del contacto a eliminar: '))
            agenda.eliminar_contacto(nombre)

        elif tecla_pulsada == 'm':
            print('Mostrar contactos')
            agenda.mostrar_agenda()

        elif tecla_pulsada == 's':
            break
        else:
            print('Opción no encontrada, pulsa tecla adecuada.')


if __name__ == '__main__':
    print('\nB I E N V E N I D O  A  L A  A G E N D A')
    run()
