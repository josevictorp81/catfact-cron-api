from translate import Translator

def translate(fact: str) -> str:
    t = Translator(to_lang='pt-br')
    return t.translate(fact)