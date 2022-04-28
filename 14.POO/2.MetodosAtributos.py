class FabricaTelefonos():
    marca = 'Huawei'
    color = 'Negro'
    memoriaRam = 32
    almacenamiento = 128
    
    # TODO: metodos(funciones que se llaman metodos)
    # TODO: esto es un metodo de instancia
    def llamar(self, mensaje):
        return mensaje
    
    def escucharMusica(self):
        print('Estas escuchando Rock')
        
    
    
    
    
telefono = FabricaTelefonos() # TODO: creacion de OBJETO
telefono.marca # TODO: atributo 
telefono.color
telefono.memoriaRam
telefono.almacenamiento


print(telefono.llamar("Hola, ¿quién es?"))
telefono.escucharMusica()

