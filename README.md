
# 🌡️ Conversor e Criador de Termômetros — Python CLI

Um programa de terminal interativo em **Python** que permite **criar seu próprio termômetro** personalizado (com unidades e pontos de fusão/ebulição definidos pelo usuário) e **converter temperaturas** entre diferentes escalas (Celsius, Kelvin e Fahrenheit).

---

## 🚀 Funcionalidades

✅ **Criar um termômetro personalizado**

* Defina o nome, unidade e pontos de referência (fusão e ebulição).
* Converta temperaturas do seu termômetro para escalas conhecidas (°C, K, °F).

✅ **Conversões entre escalas padrão**

* Kelvin → Celsius
* Fahrenheit → Celsius
* Fahrenheit → Kelvin

✅ **Interface em modo texto (CLI)**

* Menu interativo com ASCII Art.
* Mensagens de erro amigáveis.
* Limpeza automática da tela entre as etapas (compatível com Windows e Linux).

---

## 🧠 Como funciona

O programa segue a seguinte estrutura de execução:

```
┌────────────────────────────┐
│        MENU PRINCIPAL      │
├────────────────────────────┤
│ [1] Criar um termômetro    │
│ [2] Converter temperaturas │
└────────────────────────────┘
```

1. **Criar Termômetro:**

   * O usuário fornece:

     * Nome do termômetro (ex: “Zeta”)
     * Unidade de medida (ex: “Z”)
     * Pontos de gelo e de vapor da água no novo sistema.
   * O programa calcula automaticamente a correspondência entre o novo sistema e escalas conhecidas.

2. **Converter Temperaturas:**

   * O usuário escolhe entre as conversões diretas (Kelvin ↔ Celsius ↔ Fahrenheit).

---

## 💡 Fórmulas Utilizadas

**Conversão do novo termômetro para Celsius:**

```
C = 100 * (T - ponto_gelo) / (ponto_vapor - ponto_gelo)
```

**Para Kelvin:**

```
K = 100 * (T - ponto_gelo) / (ponto_vapor - ponto_gelo) + 273.15
```

**Para Fahrenheit:**

```
F = 180 * (T - ponto_gelo) / (ponto_vapor - ponto_gelo) + 32
```

---

## ⚙️ Requisitos

* **Python 3.8+**
* Biblioteca padrão do Python (`os`) — já inclusa.

---

## ▶️ Como executar

1. **Clone ou baixe** o repositório:

   ```bash
   git clone https://github.com/seuusuario/conversor-termometro.git
   cd conversor-termometro
   ```

2. **Execute o programa:**

   ```bash
   python main.py
   ```

3. **Siga as instruções do menu interativo.**

---

## 📁 Estrutura do código

```
📦 conversor-termometro
 ┣ 📜 main.py              # Código principal
 ┣ 📜 README.md            # Documentação do projeto
```

---

## 🧩 Principais Funções

| Função                       | Descrição                                         |
| ---------------------------- | ------------------------------------------------- |
| `main()`                     | Controla o loop principal e exibe o menu.         |
| `criar_termometro()`         | Permite criar e configurar um novo termômetro.    |
| `exibir_opcoes_conversoes()` | Exibe opções de conversão para o novo termômetro. |
| `kelvin_para_celsius()`      | Converte temperaturas de Kelvin para Celsius.     |
| `fahrenheit_para_celsius()`  | Converte de Fahrenheit para Celsius.              |
| `fahrenheit_para_kelvin()`   | Converte de Fahrenheit para Kelvin.               |

---

## 🧭 Exemplos de uso

```
> O que deseja fazer?
[1] Criar um termômetro
[2] Converter temperaturas em termômetros conhecidos
Sua opção: 1

Qual é o nome desse termômetro? Zeta
Qual letra acompanhará a unidade de medida? Z
Ponto de vapor da água mostrado no Zetaômetro: 180
Ponto de gelo da água mostrado no Zetaômetro: 20
```

Saída:

```
O termômetro Zeta, unidade Z.
Fusão: 20ºZ | Ebulição: 180ºZ.
[1] Converter para Celsius
[2] Converter para Kelvin
[3] Converter para Fahrenheit
```

---

## 🧑‍💻 Autor

Desenvolvido por **Mariana Rodrigues** 💻
📧 Contato: [LinkedIn](https://www.linkedin.com/in/mariana-candido-20b59b88/) | [GitHub](https://github.com/M4R0C4)

---

## 📝 Licença

Este projeto é distribuído sob a licença **MIT**.
Sinta-se livre para usar, modificar e compartilhar.

---

Quer que eu adicione um **exemplo visual** (como um print simulado do menu no terminal) ou um **badge de Python** para deixar o README mais bonito no GitHub?
