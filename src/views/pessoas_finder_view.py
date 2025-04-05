from src.controllers.pessoas_finder import PessoasFinder

# views => coisas de http


class PessoasFinderView:
    def __init__(self):
        self.__controller = PessoasFinder()

    async def handle_find_people(self, http_request=None) -> dict:
        response = await self.__controller.find_people()
        http_response = {"body": response, "status_code": 200}

        return http_response
