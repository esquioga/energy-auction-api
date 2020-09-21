import pandas as pd


class AunctionParser:
    _AUCTION_MAP = {
        'auction_id': 'ID \nNegociação',
        'auction': 'Leilão\n(1)',
        'auction_type': 'Tipo de\nleilão',
        'notice': 'Nº Edital',
        'product': 'Produto',
        'seller_initials': 'Sigla do\nvendedor\n(2)',
        'seller_company_name': 'Razão social do vendedor',
        'seller_cnpj': 'CNPJ do\nvendedor',
        'buyer_initials': 'Sigla do\ncomprador\n(3)',
        'buyer_company_name': 'Razão social do comprador',
        'buyer_cnpj': 'CNPJ do\ncomprador',
        'ceg': 'C.E.G.',
        'power_plant_name': 'Nome da usina\n(4)',
        'situation': 'Situação',
        'note': 'Nota Explicativa',
        'submarket_registry': 'Submercado do registro do contrato\n(5)',
        'plant_type': 'Tipo de usina',
        'plant_state': 'UF da usina',
        'power_source': 'Fonte \nenergética',
        'fuel_type': 'Combustível / Rio da usina',
        'eletrical_output': 'Potência\nda usina\n(MW)\n(6)',
        'installed_eletrical_output':
        'Potência Final\nInstalada C.C.\n(MWp) (235)',
        'energy_physical_guarentee':
        'Garantia Física\nda usina\n(MW médio)\n(7)',
        'negotiated_energy_by_contract':
        'Energia negociada por contrato\n(MWh)\n(8)',
        'negotiated_energy_by_year':
        'Energia negociada por contrato para o ano A\n(MW médio)\n(39); (188)',
        'negotiated_energy_by_year_plus_1':
        'Energia negociada por contrato para o ano A+1\n(MW médios)\n(39)',
        'negotiated_energy_by_year_plus_2':
        'Energia negociada por contrato para o ano A+2\n(MW médios)\n(39)',
        'negotiated_energy_by_year_plus_3':
        'Energia negociada por contrato para o ano A+3\n(MW médios)\n(39)',
        'negotiated_energy_mean':
        'Energia negociada por contrato para os demais anos\n(MW médios)\n(39)',
        'contract_type': 'Tipo de contrato\n(QTD/DIS)',
        'financial_amount':
        'Montante financeiro negociado por contrato\n(Reais em milhões)\n (39)',
        'financial_amount_updated':
        'Montante financeiro negociado por contrato \natualizado\n(Reais em milhões)',
        'price_on_auction_date':
        'Preço de Venda ou ICB\nna data do leilão (R$/MWh)\n(55)',
        'ice': 'ICE (R$/MWh)\n(56)',
        'auction_date': 'Data de\nRealização\ndo leilão',
        'ipca_auction_date': 'IPCA na data do leilão',
        'ipca_latest': 'IPCA Ago/20',
        'price_updated': 'Preço de venda atualizado (R$/MWh)',
        'revenue':
        'Receita fixa por contrato\nna data do leilão para o ano A\n(R$/ano)\n(39)',
        'revenue_plus_1':
        'Receita fixa por contrato\nna data do leilão para o ano A+1\n(R$/ano)\n(39)',
        'revenue_plus_n':
        'Receita fixa por contrato\nna data do leilão para os demais anos\n(R$/ano)\n(39)',
        'initial_date': 'Data do\nInício de Suprimento',
        'final_date': 'Data do\nFim de Suprimento',
        'can_scale':
        'Possibilidade de escalonamento da entrega da energia do contrato\n(SIM/NÃO)',
        'scaled_delivery': 'Entrega escalonada\n(SIM/NÃO)'
    }

    @staticmethod
    def parse_xsl(file):
        df: pd.DataFrame = pd.read_excel(file,
                           sheet_name='Resultado Consolidado',
                           skiprows=9)
        df = df.drop(df.columns[0], axis=1)
        df.columns = AunctionParser._AUCTION_MAP.keys()
        df = df.apply(lambda value: value.astype(str).str.upper())
        df = df.replace('NÃO', False).replace('SIM', True)
        return df.to_json(orient='records')
