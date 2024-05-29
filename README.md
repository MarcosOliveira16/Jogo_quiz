# Jogo_quiz
Este pequeno projeto busca ser um simples jogo do tipo "Quiz" (perguntas e respostas).
- Feito em Python
- Conhecimentos básicos/intermediários
- Destaque: sistema de guardar o progresso na mesma ou em diferentes execuções implementado.
- Roda no terminal
- Banco de perguntas contém 40 questões e suas respectivas respostas

Claro, vou elaborar uma documentação básica para o seu jogo quiz em estilo Markdown, explicando a metodologia utilizada e fornecendo uma visão geral do funcionamento do código:

# Documentação - Jogo Quiz

## Introdução
Este documento fornece uma visão geral do código-fonte de um jogo quiz implementado em Python. O jogo consiste em apresentar uma série de perguntas ao jogador, que deve fornecer respostas corretas para acumular pontos. O código é estruturado em classes e funções para garantir modularidade e facilidade de manutenção.

## Metodologia
O jogo foi desenvolvido utilizando a linguagem de programação Python e segue uma abordagem procedural. Foram utilizadas as seguintes técnicas e conceitos:

### Estrutura de Classes
- **Classe `Jogador`:** Representa o jogador do jogo, armazenando seu nome e pontuação.
- **Classe `Jogo`:** Contém métodos para gerenciar o jogo, como apresentar perguntas, verificar respostas e atualizar o ranking.

### Funcionalidades
- **Cadastro de Jogadores:** Permite que o jogador cadastre seu nome antes de iniciar o jogo.
- **Apresentação de Perguntas:** Seleciona aleatoriamente perguntas de um conjunto pré-definido e exibe-as ao jogador.
- **Verificação de Respostas:** Verifica se a resposta fornecida pelo jogador está correta e atualiza sua pontuação.
- **Exportação e Importação de Rankings:** Permite exportar o ranking atual para um arquivo de texto e importar rankings previamente salvos.

### Fluxo de Execução
1. O jogo é iniciado e apresenta um menu com várias opções.
2. O jogador pode escolher entre iniciar o jogo, importar/exportar rankings, exibir o ranking atual ou sair do jogo.
3. Se o jogador optar por iniciar o jogo, ele será solicitado a cadastrar seu nome.
4. Após o cadastro, o jogo exibe perguntas ao jogador e verifica suas respostas.
5. O jogo continua até que todas as perguntas sejam respondidas ou o jogador decida sair.
6. Ao final do jogo, o jogador tem a opção de exportar seu ranking ou voltar ao menu principal.

### Manipulação de Arquivos
- As informações do progresso do jogador e do ranking são armazenadas em arquivos de texto (`Progresso.txt` e `Ranking.txt`, respectivamente).
- Os arquivos são lidos e gravados utilizando operações de leitura e escrita de arquivos em Python.

## Execução
Para executar o jogo, basta rodar o arquivo Python `quiz.py`. Certifique-se de ter o Python instalado em seu sistema.

## Requisitos
- Python 3.x

## Conclusão
O jogo quiz implementado em Python oferece uma experiência interativa e divertida para os jogadores. Sua estrutura modular e funcionalidades bem definidas permitem fácil manutenção e extensão. Este documento fornece uma visão geral do código-fonte e da metodologia utilizada, permitindo uma compreensão clara do funcionamento do jogo.
