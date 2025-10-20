#classe veiculos
class veiculos:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

        def ligar(self):
            print("vrummmm")
        
class Carro(veiculo):
    def __init__(self, rodas, marca, teto_solar):
      super().__init__(rodas, marca)
      self.teto_solar = teto_solar
