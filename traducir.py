from googletrans import Translator

def traducir_entoes(texto):
    translator = Translator()
    return translator.translate(texto, src='en', dest='es').text
