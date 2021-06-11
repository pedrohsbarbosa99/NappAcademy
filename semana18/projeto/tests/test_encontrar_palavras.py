from projeto.classes.encontrar_palavras import EncontrarPalavras
import pytest


class TestEncontrarPalavras:
    def test__instanciar_classe(self):
        objeto = EncontrarPalavras(case_sensitive=True)
        assert isinstance(objeto, EncontrarPalavras)

    def test__palavra_no_arquivo_true_case_sensitive(self):
        objeto = EncontrarPalavras(case_sensitive=True)
        diretorio = 'diretorio7/subdiretorio2/arquivo4.txt'
        palavra = 'napp'
        assert objeto.palavra_no_arquivo(palavra, diretorio) is True

    def test__palavra_no_arquivo_false_case_sensitive(self):
        objeto = EncontrarPalavras(case_sensitive=True)
        diretorio = 'diretorio7/subdiretorio2/arquivo4.txt'
        palavra = 'NaPP'
        assert objeto.palavra_no_arquivo(palavra, diretorio) is False

    def test_encontrar_palavra_txt_case_sensitive(self):
        objeto = EncontrarPalavras(case_sensitive=True)
        dados = objeto.encontrar_palavra('napp', 'txt')
        assert type(dados) is list
        assert len(dados) == 4

    def test_encontrar_palavra_txt_not_case_sensitive(self):
        objeto = EncontrarPalavras(case_sensitive=False)
        dados = objeto.encontrar_palavra('napp', 'txt')
        assert type(dados) is list
        assert len(dados) == 6

    def test_encontrar_palavra_csv_case_sensitive(self):
        objeto = EncontrarPalavras(case_sensitive=True)
        dados = objeto.encontrar_palavra('napp', 'csv')
        assert type(dados) is list
        assert len(dados) == 20

    def test_encontrar_palavra_csv_case_sensitive(self):
        objeto = EncontrarPalavras(case_sensitive=False)
        dados = objeto.encontrar_palavra('napp', 'csv')
        assert type(dados) is list
        assert len(dados) == 30
