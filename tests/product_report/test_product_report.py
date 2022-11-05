from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "hamburguer",
        "Lan Chonete",
        "2022-05-11",
        "2022-06-11",
        "123456789",
        "Não guarde. COMA!"
    )
    relatorio = (
        "O produto hamburguer"
        " fabricado em 2022-05-11"
        " por Lan Chonete com validade"
        " até 2022-06-11"
        " precisa ser armazenado Não guarde. COMA!."
    )
    assert str(product) == relatorio
