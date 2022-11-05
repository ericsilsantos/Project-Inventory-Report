from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "hamburguer",
        "Lan Chonete",
        "2022-05-11",
        "2022-06-11",
        "123456789",
        "Não guarde. COMA!"
    )
    assert product.id == 1
    assert product.nome_do_produto == "hamburguer"
    assert product.nome_da_empresa == "Lan Chonete"
    assert product.data_de_fabricacao == "2022-05-11"
    assert product.data_de_validade == "2022-06-11"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "Não guarde. COMA!"
