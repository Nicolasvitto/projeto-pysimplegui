import PySimpleGUI as sg

def mostrar_monstros_fortes(arma, raridade):
  """
  Retorna uma string com os monstros fortes contra os quais a arma é eficaz.
  """
  monstros_por_arma_raridade = {
    "Espada": {
      "Único": ["Fera", "Demônio", "Servo", "Troll", "Trasgo"],
      "Raro": ["Fera", "Servo", "Troll", "Demônio"],
      "Épico": ["Trasgo", "Golem", "Milícia"],
      "Lendário": ["Zumbi", "Bandido"],
    },
    "Machado": {
      "Único": ["Bandido", "Zumbi"],
      "Raro": ["Bandido", "Zumbi"],
      "Épico": ["Fera", "Servo", "Troll", "Demônio"],
      "Lendário": ["Milícia", "Trasgo"],
    },
    "Martelo": {
      "Único": ["Golem", "Milícia"],
      "Raro": ["Golem", "Milícia"],
      "Épico": ["Bandido", "Zumbi"],
      "Lendário": ["Fera", "Servo", "Golem", "Troll, demonio"],
    },
  }

  if arma in monstros_por_arma_raridade and raridade in monstros_por_arma_raridade[arma]:
    return f"A {arma} de raridade {raridade} é pode ser forjado por : {', '.join(monstros_por_arma_raridade[arma][raridade])}"
  else:
    return "Combinação de arma e raridade não encontrada."

def main():
  # Definir layout da interface
  layout = [
    [sg.Text('Forja de Armas', font=("Helvetica", 24))],
    [sg.Text('Selecione o tipo de arma:'), sg.Combo(['Espada', 'Machado', 'Martelo'], key='tipo_arma')],
    [sg.Text('Selecione a raridade:'), sg.Combo(['Único', 'Raro', 'Épico', 'Lendário'], key='raridade')],
    [sg.Button('Forjar Arma', key='botao_forjar')],
    [sg.Text('', key='resultado')],  # Removed 'expand=True'
  ]

  # Criar a janela
  window = sg.Window('Forja de Armas', layout)

  # Loop de eventos
  while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
      break

    if event == 'botao_forjar':
      tipo_arma = values['tipo_arma']
      raridade = values['raridade']
      resultado_forja = mostrar_monstros_fortes(tipo_arma, raridade)
      window['resultado'].update(resultado_forja)

  # Fechar a janela
  window.close()

if __name__ == "__main__":
  main()
