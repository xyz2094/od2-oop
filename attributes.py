from typing import Dict

class Atributos:
    """Classe que representa a ficha de atributos de um personagem."""
    def __init__(self, forca: int, destreza: int, constituicao: int, inteligencia: int, sabedoria: int, carisma: int):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    @classmethod
    def from_dict(cls, data: Dict[str, int]):
        """Cria uma instância de Atributos a partir de um dicionário."""
        return cls(
            forca=data.get("Força", 0),
            destreza=data.get("Destreza", 0),
            constituicao=data.get("Constituição", 0),
            inteligencia=data.get("Inteligência", 0),
            sabedoria=data.get("Sabedoria", 0),
            carisma=data.get("Carisma", 0)
        )

    def __repr__(self) -> str:
        """Retorna uma representação formatada dos atributos para exibição."""
        return (
            f"  Força:        {self.forca}\n"
            f"  Destreza:     {self.destreza}\n"
            f"  Constituição: {self.constituicao}\n"
            f"  Inteligência: {self.inteligencia}\n"
            f"  Sabedoria:    {self.sabedoria}\n"
            f"  Carisma:      {self.carisma}"
        )