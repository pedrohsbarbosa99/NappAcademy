def n_medias(*notas, **kwnotas):
    media = 0
    if notas and kwnotas:
        nota = float(len(notas) + len(kwnotas))
        media = (sum(notas) + sum(kwnotas.values())) / nota
    elif notas:
        media = sum(notas) / float(len(notas))
    elif kwnotas:
        media = sum(kwnotas.values())/float(len(kwnotas))
    return media