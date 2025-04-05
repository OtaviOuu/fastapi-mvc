from src.model.repositories.pessoas_repository import PessoasRepository


class PessoasFinder:
    def __init__(self):
        self.__pessoas_repo = PessoasRepository()

    async def find_people(self) -> dict:
        pessoas = await self.__pessoas_repo.get_all_people()

        formated_pessoas = []
        for pessoa in pessoas:
            formated_pessoas.append({"id": pessoa.id, "nome": pessoa.nome})

        return {
            "type": "Pessoa",
            "count": len(formated_pessoas),
            "attributes": formated_pessoas,
        }
