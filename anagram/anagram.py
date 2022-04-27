def find_anagrams(palabra, candidatos):
    return [candidato
            for candidato in candidatos
            if _letters(candidato) == _letters(palabra)
            if candidato.lower() != palabra.lower()]


def _letters(palabra):
    return sorted(palabra.lower())