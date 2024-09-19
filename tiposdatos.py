print(" Clases V2 Reyes Ramirez")
# zona de clases
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mts, Peso {self.peso} Kg")
    def mi_lista(self):
        lista_planetas = ["Mercuruio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno"]
        print(lista_planetas)
        for planeta in lista_planetas:
            print(planeta)

    def lista_frutas(self):
        frutas = ("fresa", "platano", "manzana")
        print(frutas)
        for fruta in frutas:
            print(fruta)
        
    def lista_perros(self):
        perros = {
            "border collie": "Estados unidos",
            "blue healer": "Australia",
            "golden retriver": "Reino unido"
            }
        print(perros)
        for x, y in perros.items():
            print(x, y)
        
    def lista_peliculas(self):
        pelicula = {"Paw patrol", "La Sirenita", "FNAF"}
        print(pelicula)
        for x in pelicula:
            print(x)


# creacion de objeto info
info=Datos(1.75,70.5)

# utilizando obj. --> info
info.mostrar_datos()
print(" Lista de planetas del sistema solar Reyes Ramirez")
info.mi_lista()

print(" Lista de frutas Reyes Ramirez")
info.lista_frutas()

print(" Lista de pais de raza de perros Reyes Ramirez")
info.lista_perros()

print(" Lista de peliculas Reyes Ramirez")
info.lista_peliculas()

