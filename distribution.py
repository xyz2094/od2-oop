import random
from abc import ABC, abstractmethod
from typing import List

from attributes import Atributos

class MetodoDistribuicao(ABC):
    """Classe base abstrata para os métodos de distribuição de atributos."""
    @abstractmethod
    def distribuir(self) -> Atributos:
        pass
        
    def _distribuir_valores_interativo(self, rolagens: List[int]) -> Atributos:
        """Lógica interativa para o usuário distribuir os valores rolados."""
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

class EstiloClassico(MetodoDistribuicao):
    """Rola 3d6 em ordem para cada atributo."""
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
    """Rola 6x 3d6 e o usuário distribui os valores."""
    def _rolar_3d6(self) -> int:
        return sum(random.randint(1, 6) for _ in range(3))

    def distribuir(self) -> Atributos:
        print("\nGerando atributos no Estilo Aventureiro (3d6, distribua como quiser)...")
        input("Pressione Enter para rolar os 6 valores...")
        
        rolagens = [self._rolar_3d6() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)

class EstiloHeroico(EstiloAventureiro):
    """Rola 6x 4d6 (tira o menor) e o usuário distribui os valores."""
    def _rolar_4d6_drop_lowest(self) -> int:
        rolagens = [random.randint(1, 6) for _ in range(4)]
        rolagens.remove(min(rolagens))
        return sum(rolagens)

    def distribuir(self) -> Atributos:
        print("\nGerando atributos no Estilo Heróico (4d6 drop lowest, distribua como quiser)...")
        input("Pressione Enter para rolar os 6 valores...")
        
        rolagens = [self._rolar_4d6_drop_lowest() for _ in range(6)]
        return self._distribuir_valores_interativo(rolagens)