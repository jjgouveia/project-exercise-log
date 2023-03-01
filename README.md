# Exercício de POO em Python 🚀

Nesse exercício treinei herança, interfaces, instanciação de objetos e muitos outros tópicos ligados a POO em Python!

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
  
  Nesse exercício você implementará uma função em Python para resolver um teste técnico similar ao que já foi aplicado pelo Facebook e outras big techs! Tente desenvolver uma solução otimizada e escolha bem qual estrutura de dados será utilizada em termos de complexidade de tempo e espaço! Essa escolha tende a ser um diferencial em um processo seletivo desse tipo.

</details>

# Termos e acordos

Ao iniciar esse exercício, você concorda com as diretrizes do Código de Conduta e do Manual da Pessoa Estudante da Trybe.


<details>
  <summary><strong>🚵 Habilidades a serem trabalhadas:</strong></summary><br />
  
  <ul>
    <li>Colocar em prática POO em Python</li>
    <li>Herança e Interfaces.</li>
  </ul>

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>

# Exercício

## Implemente um sistemas de logs por nível de severidade, seguindo o diagrama abaixo

![Diagrama de Classe](/img/class_diagram.png)

### Classe `Log`

Atributos:

> manipuladores - Será inicializado com um conjunto de subclasses de ManipuladorDeLog;

Métodos:

- `adicionar_manipulador` - adiciona um manipulador ao conjunto de manipuladores do gerenciamento de logs (`Log`);
- `info` - dispara logs com nível de severidade `"INFO"`;
- `alerta` - dispara logs com nível de severidade `"ALERTA"`;
- `erro` - dispara logs com nível de severidade `"ERRO"`;
- `debug` - dispara logs com nível de severidade `"DEBUG"`;
- `__log` - dispara os logs formatados para todos os manipuladores (invocado para cada nível de severidade, para evitar duplicação de código);
- `__formatar` - formata os logs de acordo com o padrão “[ERRO - 01/01/2020 13:00:00]: ZeroDivisionError: division by zero”;

### Classe `ManipuladorDeLog`

A classe `ManipuladorDeLog` é uma `interface` (e, por consequência, uma _classe abstrata_) e deve declarar um método de classe (_classmethod_) e abstrato (_abstractmethod_) `log` que recebe um parâmetro `mensagem` ou `msg`.

### Classes LogEmArquivo e LogEmTela

As classes `LogEmArquivo` e `LogEmTela` devem herdar de `ManipuladorDeLog` e sobrescrever o método de classe `log`, salvando a mensagem em um arquivo (`data/log.txt`) ou a exibindo na tela, respectivamente.

🐦 Dica: Você pode utilizar a função `print` em tela ou em arquivo (que pode ter um nome padrão).

> **Implemente em:** `src/log.py`, `src/manipulador_de_log.py`, `src/log_em_tela.py`, `src/log_em_arquivo.py`
