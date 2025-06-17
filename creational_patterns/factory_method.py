from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    A classe Creator declara o factory method que retorna um objeto do tipo da 
    interface Produto. As subclasses de Creator fornecem a implementação do
    factory method. 
    """
    @abstractmethod
    def factory_method(self):
        """
        A classe Creator pode fornecer uma implementação padrão para o factory
        method. Porém, obrigatoriamente as subclasses precisam implementá-lo.
        """
        pass

    def some_operation(self) -> str:
        """
        Note também, apesar do nome, a classe base não possui como papel
        principal a criação dos produtos. Geralmente, contém regras de negócio a
        depender do objeto produto.
        Subclasses mudam indiretamente as regras de negócio, ao implementar o 
        factory method e retornar diferentes tipos de objetos de produtos.
        """

        # Chamar o factory method para criar produtos.
        product = self.factory_method()

        # Agora, use o produto:
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators sobreescrevem o factory method e mudam o o tipo dos objetos
produtos retornados pela base class.
"""


class ConcreteCreator1(Creator):
    """
    Note que a assinatura do método ainda usa os tipos abstratos de produtos,
    mesmo que o produto concreto é retornado pelo método. Esse caminho permite
    que o Creator possa ser independente da criação de classes de produtos.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    A interface Product declara as operações em comum para todos os objetos
    produtos implementarem de forma obrigatória.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products fornece várias implementações da interface Product.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    O client code trabalha com uma instância de ConcreteCreator, através da 
    interface base. Contudo, como o cliente se mantém trabalhando com Creator,
    via interface base, você pode passar no parâmetro qualquer subclasse criada.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())