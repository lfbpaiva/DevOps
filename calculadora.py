CUPONS_PERCENTUAIS = {
    "DEVOPS10": 10,
    "BOASVINDAS5": 5,
}


def obter_desconto_do_cupom(cupom):
    """
    Retorna o percentual de desconto de um cupom promocional.

    Cupons sao comparados sem diferenciar maiusculas de minusculas.
    """
    if cupom is None:
        return 0

    codigo = cupom.strip().upper()
    if codigo not in CUPONS_PERCENTUAIS:
        raise ValueError("Cupom promocional invalido.")

    return CUPONS_PERCENTUAIS[codigo]


def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)

    O desconto do cupom soma com o desconto_percentual informado.
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    desconto_total = desconto_percentual + obter_desconto_do_cupom(cupom)
    if desconto_total > 100:
        raise ValueError("O desconto total nao pode passar de 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    total = subtotal * (1 - desconto_total / 100)

    return round(total, 2)
