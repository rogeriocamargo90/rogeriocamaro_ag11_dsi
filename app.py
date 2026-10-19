"""
Atividade: Controle de Níveis de Água
Aluno: Rogério Jesus de Camargo
Turma: FMA
Curso: Desenvolvimento de Sistemas
Professora: Edna
"""

from colorama import Fore, Style, init

# Inicializa o colorama para garantir compatibilidade em diferentes terminais
init(autoreset=True)


def definir_alerta_reservatorio(nivel):
  """Função responsável por definir a cor, a situação e a mensagem

  de alerta conforme o nível do reservatório informado.
  """
  if nivel == 1:
    return (
        Fore.RED,
        "Nível 1 - Muito baixo (crítico)",
        "ALERTA CRÍTICO: Risco de desabastecimento! O reservatório está extremamente"
        " baixo.",
    )
  elif nivel == 2:
    return (
        Fore.YELLOW,
        "Nível 2 - Baixo",
        "ATENÇÃO: Nível abaixo do ideal. Considere reduzir o consumo.",
    )
  elif nivel == 3:
    return (
        Fore.GREEN,
        "Nível 3 - Médio",
        "ESTÁVEL: O reservatório está operando em um nível adequado e seguro.",
    )
  elif nivel == 4:
    return (
        Fore.CYAN,
        "Nível 4 - Alto",
        "MONITORAMENTO: Nível elevado. Acompanhe a tendência de enchimento.",
    )
  elif nivel == 5:
    return (
        Fore.BLUE,
        "Nível 5 - Muito alto (alerta)",
        "ALERTA DE SEGURANÇA: Reservatório cheio! Risco de transbordo.",
    )
  else:
    return (
        Fore.WHITE,
        "Nível Inválido",
        "Erro: Nível de reservatório não reconhecido na escala.",
    )


def simular_monitoramento():
  """Simula o monitoramento do reservatório percorrendo

  uma lista com os cinco níveis definidos.
  """
  # Lista contendo os cinco níveis de água do reservatório
  niveis_reservatorio = [1, 2, 3, 4, 5]

  print("=" * 60)
  print(" SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA ".center(60, "="))
  print("=" * 60)
  print(f"Aluno: Rogério Jesus de Camargo | Turma: FMA\n")

  # Itera sobre a lista de níveis simulando o ambiente de monitoramento
  for nivel in niveis_reservatorio:
    cor, situacao, mensagem = definir_alerta_reservatorio(nivel)

    print(f"[{situacao}]")
    print(f"{cor}{mensagem}{Style.RESET_ALL}")
    print("-" * 60)


if __name__ == "__main__":
  simular_monitoramento()