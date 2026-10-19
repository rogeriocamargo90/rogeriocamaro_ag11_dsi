# 💧 Controle de Níveis de Água

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](Concluído-success.svg)](https://github.com/)

Projeto desenvolvido para a atividade prática da agenda de **Desenvolvimento de Sistemas** (Turma FMA).

---

---

## 📋 Sobre o Projeto
Este sistema foi desenvolvido em Python para ser executado no terminal, simulando o monitoramento automatizado de um reservatório de água. O programa utiliza uma **lista** com cinco níveis progressivos de água, aplicando regras condicionais e a biblioteca **`colorama`** para exibir alertas coloridos e destacados conforme o grau de risco de cada situação.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.x** (Linguagem de programação)
* **Colorama** (Biblioteca para estilização e coloração de textos no terminal)

---

## 📊 Tabela de Níveis e Cores

| Nível do Reservatório | Situação | Cor Sugerida |
| :--- | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho |
| **Nível 2** | Baixo | 🟡 Amarelo |
| **Nível 3** | Médio | 🟢 Verde |
| **Nível 4** | Alto | 🔵 Ciano |
| **Nível 5** | Muito alto (alerta) | 🔵 Azul |

---

## ⚙️ Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `colorama` através do terminal:
   ```bash
   pip install colorama