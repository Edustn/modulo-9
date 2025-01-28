from pydantic import BaseModel


class Adder(BaseModel):
    """
    Classe de teste para criar a operação de adição
    """

    def Add(self, *args: int) -> float:
        return sum(args)
