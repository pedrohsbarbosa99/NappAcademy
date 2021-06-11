import os
import glob


class EncontrarPalavras:
    def __init__(self, case_sensitive=True):
        self.case_sensitive = case_sensitive

    def palavra_no_arquivo(self, palavra, arquivo):
        with open(arquivo, 'r') as file:
            if self.case_sensitive:
                for line in file:
                    return palavra in line
            else:
                for line in file:
                    return palavra.lower() in line.lower()
        return False

    def todos_arquivos(self, formato):
        looking_for = '**/*.' + formato
        matched = glob.glob(looking_for, recursive=True)
        return matched

    def encontrar_palavra(self, palavra, formato):
        encontrado_em = []

        arquivos = self.todos_arquivos(formato=formato)

        for arquivo in arquivos:
            if self.case_sensitive:
                if self.palavra_no_arquivo(palavra, arquivo):
                    encontrado_em.append(arquivo)
            else:
                if self.palavra_no_arquivo(palavra.lower(), arquivo):
                    encontrado_em.append(arquivo)
        return encontrado_em
