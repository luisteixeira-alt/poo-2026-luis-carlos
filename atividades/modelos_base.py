
class Produto:
    def __init__(self, nome, preco):
        self.__nome = ""
        self.__preco = 0.0

        self.set_nome(nome)
        self.set_preco(preco)


    def get_nome(self):
        return self.__nome


    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Erro: o nome deve ter pelo menos 3 caracteres.")


    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if (
            isinstance(preco, (int, float))
            and not isinstance(preco, bool)
            and preco >= 0
        ):
            self.__preco = float(preco)
        else:
            print("Erro: o preço deve ser um número não negativo.")


if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    objeto_valido = Produto("Cadeira Gamer", 850.00)
    print(
        f"Objeto Criado: {objeto_valido.get_nome()} - "
        f"R$ {objeto_valido.get_preco():.2f}"
    )

    print("\n--- Teste 1: Tentativa de criar com preço negativo ---")
    objeto_invalido = Produto("Mesa", -150.00)
    print(
        f"Resultado mantido com segurança: "
        f"R$ {objeto_invalido.get_preco():.2f}"
    )

    print("\n--- Teste 2: Tentativa de alterar o nome para um texto muito curto ---")
    objeto_valido.set_nome("AB")
    print(f"Nome do objeto protegido: {objeto_valido.get_nome()}")
