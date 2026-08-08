import pytest

from calculadora import calcular_total


def test_cupom_devops10_funciona_com_minusculas():
    itens = [(200.0, 1)]

    assert calcular_total(itens, cupom="devops10") == 180.0


def test_cupom_soma_com_desconto_existente():
    itens = [(100.0, 1)]

    total = calcular_total(
        itens,
        desconto_percentual=5,
        cupom="DEVOPS10",
    )

    assert total == 85.0


def test_cupom_invalido_gera_erro():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], cupom="XPTO")
