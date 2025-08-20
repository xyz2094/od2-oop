import random
from abc import ABC, abstractmethod
from typing import List, Dict

class Atributos:
    def __init__(self, forca: int, destreza: int, constituicao: int, inteligencia: int, sabedoria: int, carisma: int):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    @classmethod
    def from_dict(cls, data: Dict[str, int]):
        return cls(
            forca=data.get("Força", 0),
            destreza=data.get("Destreza", 0),
            constituicao=data.get("Constituição", 0),
            inteligencia=data.get("Inteligência", 0),
            sabedoria=data.get("Sabedoria", 0),
            carisma=data.get("Carisma", 0)
        )

    def __repr__(self) -> str:
        return (
            f"  Força:        {self.forca}\n"
            f"  Destreza:     {self.destreza}\n"
            f"  Constituição: {self.constituicao}\n"
            f"  Inteligência: {self.inteligencia}\n"
            f"  Sabedoria:    {self.sabedoria}\n"
            f"  Carisma:      {self.carisma}"
        )

class MetodoDistribuicao(ABC):
    @abstractmethod
    def distribuir(self) -> Atributos:
        pass

class EstiloClassico(MetodoDistribuicao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        print("\nGerando atributos no Estilo Clássico (3d6, em ordem)...")
        input("Pressione Enter para rolar os dados...")
        
        forca = self._rolar_3d6()
        print(f"Sua Força é: {forca}")
        destreza = self._rolar_3d6()
        print(f"Sua Destreza é: {destreza}")
        constituicao = self._rolar_3d6()
        print(f"Sua Constituição é: {constituicao}")
        inteligencia = self._rolar_3d6()
        print(f"Sua Inteligência é: {inteligencia}")
        sabedoria = self._rolar_3d6()
        print(f"Sua Sabedoria é: {sabedoria}")
        carisma = self._rolar_3d6()
        print(f"Seu Carisma é: {carisma}")

        return Atributos(forca, destreza, constituicao, inteligencia, sabedoria, carisma)

class EstiloAventureiro(MetodoDistribuicao):
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        print("\nGerando atributos no Estilo Aventureiro (3d6, distribua como quiser)...")
        input("Pressione Enter para rolar os 6 valores...")
        
        rolagens = [self._rolar_3d6() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)
        
    def _distribuir_valores_interativo(self, rolagens: List[int]) -> Atributos:
        nomes_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        atributos_finais = {}

        print("\nVocê rolou os seguintes valores:", sorted(rolagens, reverse=True))

        for atributo_atual in nomes_atributos:
            print("\n-------------------------")
            print(f"Valores disponíveis: {rolagens}")
            
            valor_escolhido = 0
            while True:
                try:
                    valor_input = int(input(f"Qual valor você quer para {atributo_atual}? "))
                    if valor_input in rolagens:
                        valor_escolhido = valor_input
                        break
                    else:
                        print("Valor inválido. Por favor, escolha um dos valores da lista.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
            
            atributos_finais[atributo_atual] = valor_escolhido
            rolagens.remove(valor_escolhido)

        print("\nDistribuição concluída!")
        return Atributos.from_dict(atributos_finais)

class EstiloHeroico(EstiloAventureiro):
    def _rolar_4d6_drop_lowest(self) -> int:
        rolagens = [random.randint(1, 6) for _ in range(4)]
        rolagens.remove(min(rolagens))
        return sum(rolagens)

    def distribuir(self) -> Atributos:
        print("\nGerando atributos no Estilo Heróico (4d6 drop lowest, distribua como quiser)...")
        input("Pressione Enter para rolar os 6 valores...")
        
        rolagens = [self._rolar_4d6_drop_lowest() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)

class Personagem:
    def __init__(self, nome: str, metodo_distribuicao: MetodoDistribuicao):
        self.nome = nome
        print(f"\nIniciando a criação de '{self.nome}'...")
        self.atributos = metodo_distribuicao.distribuir()

    def mostrar_ficha(self):
        print("\n" + "=" * 35)
        print(f"FICHA FINAL DE: {self.nome.upper()}")
        print("=" * 35)
        print(self.atributos)
        print("=" * 35)

if __name__ == "__main__":
    
    while True:
        print("\n===== CRIADOR DE PERSONAGENS DE RPG =====\n")
        print("Escolha o método de distribuição de atributos:")
        print("1. Estilo Clássico (3d6 em ordem, aleatório e desafiador)")
        print("2. Estilo Aventureiro (3d6, você distribui os resultados)")
        print("3. Estilo Heróico (4d6 tira o menor, você distribui os resultados)")
        print("4. Sair\n")

        escolha = input("Digite sua opção (1-4): ")

        if escolha == '4':
            print("Obrigado por jogar! Até a próxima aventura.")
            break
        
        if escolha in ['1', '2', '3']:
            nome_personagem = input("\nQual é o nome do seu personagem? ")
            
            metodo_escolhido = None
            if escolha == '1':
                metodo_escolhido = EstiloClassico()
            elif escolha == '2':
                metodo_escolhido = EstiloAventureiro()
            elif escolha == '3':
                metodo_escolhido = EstiloHeroico()

            novo_personagem = Personagem(nome_personagem, metodo_escolhido)
            novo_personagem.mostrar_ficha()
            
            input("\nPressione Enter para continuar...")

        else:
            print("Opção inválida. Por favor, tente novamente.")