from classes.encontrar_palavras import EncontrarPalavras


def main():
    busca_napp1 = EncontrarPalavras(case_sensitive=True)
    busca_napp1.encontrar_palavra('NaPp', 'csv')
    busca_napp2 = EncontrarPalavras(case_sensitive=False)
    busca_napp2.encontrar_palavra('NaPp', 'csv')
    busca_napp3 = EncontrarPalavras(case_sensitive=True)
    busca_napp3.encontrar_palavra('NaPp', 'txt')
    busca_napp4 = EncontrarPalavras(case_sensitive=False)
    busca_napp4.encontrar_palavra('NaPp', 'txt')


if __name__ == '__main__':
    main()
