from lib.linha import cria_linha


def test_cria_linha():
    es_comum = {'item': 'a', 'data_lancamento': 'a'}
    es0 = es_comum | {'tipo_movimento': 'Ent', 'quantidade': 0, 'valor': 0}
    assert cria_linha(es0) == {'item': 'a', 'data_lancamento': 'a', 'qtd_entrada': 0, 'vlr_entrada': 0,
                               'qtd_saida': 0, 'vlr_saida': 0}
    es1 = es_comum | {'tipo_movimento': 'Ent', 'quantidade': 1.5, 'valor': 1.2}
    assert cria_linha(es1) == {'item': 'a', 'data_lancamento': 'a', 'qtd_entrada': 1.5, 'vlr_entrada': 1.2,
                               'qtd_saida': 0, 'vlr_saida': 0}
    es2 = es_comum | {'tipo_movimento': 'Sai', 'quantidade': 1.4, 'valor': 1.1}
    assert cria_linha(es2) == {'item': 'a', 'data_lancamento': 'a', 'qtd_entrada': 0, 'vlr_entrada': 0,
                               'qtd_saida': 1.4, 'vlr_saida': 1.1}
    es3_t = cria_linha(es1, es2)
    assert es3_t == {'item': 'a', 'data_lancamento': 'a', 'qtd_entrada': 1.5, 'vlr_entrada': 1.2, 'qtd_saida': 1.4,
                     'vlr_saida': 1.1}
    es4_t = cria_linha(es0, es1)
    assert es4_t == {'item': 'a', 'data_lancamento': 'a', 'qtd_entrada': 1.5, 'vlr_entrada': 1.2, 'qtd_saida': 0,
                     'vlr_saida': 0}
