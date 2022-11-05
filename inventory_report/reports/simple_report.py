from datetime import datetime
from statistics import mode


class SimpleReport:
    @classmethod
    def generate(self, products):
        atual = datetime.now().isoformat()
        validade = min([
            prod['data_de_validade']
            for prod in products
            if prod['data_de_validade'] > atual
        ])
        fabricacao = min([prod['data_de_fabricacao'] for prod in products])
        empresas = [emp["nome_da_empresa"] for emp in products]
        empresa = mode(empresas)
        return (
            f"Data de fabricação mais antiga: {fabricacao}\n"
            f"Data de validade mais próxima: {validade}\n"
            f"Empresa com mais produtos: {empresa}"
        )
