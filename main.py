from characters import Personagem
from distribution import (
    MetodoDistribuicao,
    EstiloClassico,
    EstiloAventureiro,
    EstiloHeroico
)

def menu_principal():
    """Função principal que gerencia o loop do menu e a criação do personagem."""
    while True:
        print("\n===== OLD DRAGON 2 =====\n")
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
            
            metodo_escolhido: MetodoDistribuicao
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

if __name__ == "__main__":
    menu_principal()