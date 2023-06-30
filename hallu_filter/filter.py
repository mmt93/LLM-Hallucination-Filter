from difflib import SequenceMatcher

def fix_not_finished_sentence(text):
  return text.rsplit('.', 1)[0] + '.'

def quebrar_string(string):
  pedacos = []
  pedaco = ''
  for caractere in string:
      if caractere == '.' or caractere == ',':
          pedaco += caractere
          pedacos.append(pedaco)
          pedaco = ''
      else:
          pedaco += caractere
  if pedaco:
      pedacos.append(pedaco)
  return pedacos

def similar(a, b):
  return SequenceMatcher(None, a, b).ratio()

def return_clean_string(ratio, text, clean_string_list):
  clean_string = []
  for i in range(len(clean_string_list)):
    part_string = clean_string_list[i].split()
    size = len(part_string)
    result_list = text.split()[i:i+size]
    result_str = " ".join(result_list)
    for j in range(len(text)):
      result_list = text.split()[j:j+size]
      result_str = " ".join(result_list)
      if similar(clean_string_list[i], result_str) >= ratio:
        clean_string.append(clean_string_list[i])
        break

  return clean_string

def concatenar_com_espaco(lista_strings, resposta_original):
  if not lista_strings:
    return "Desculpe, não possuo essa informação"
  else:
    resultado = ''.join(lista_strings)
    return verificar_e_adicionar(resposta_original ,fix_not_finished_sentence(resultado))

def obter_resposta(texto):
    indice_inicio = texto.find("Resposta:") + len("Resposta:")
    indice_fim = texto.find("\n", indice_inicio)
    resposta = texto[indice_inicio:indice_fim]
    return resposta


def remover_quebras_de_linha(texto):
  texto_sem_quebras = texto.replace('\n', '')
  return texto_sem_quebras

def verificar_e_adicionar(parametro1, parametro2):
    if parametro1.startswith("Sim,"):
        if not parametro2.startswith("Sim,"):
            parametro2 = "Sim, " + parametro2
    return parametro2

def clean_hallucination(ratio , text, answare):
 return concatenar_com_espaco(return_clean_string(ratio, text,quebrar_string(answare)), answare)
