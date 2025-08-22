from distribution import MetodoDistribuicao

class Personagem:
    """Classe que representa o personagem, unindo nome e atributos."""
    def __init__(self, nome: str, metodo_distribuicao: MetodoDistribuicao):
        self.nome = nome
        print(f"\nIniciando a criação de '{self.nome}'...")
        self.atributos = metodo_distribuicao.distribuir()

    def mostrar_ficha(self):
        """Exibe a ficha final do personagem no console."""
        print("\n" + "=" * 35)
        print(f"FICHA FINAL DE: {self.nome.upper()}")
        print("=" * 35)
        print(self.atributos)
        print("=" * 35)