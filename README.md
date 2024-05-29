# Jogo_quiz
Este pequeno projeto busca ser um simples jogo do tipo "Quiz" (perguntas e respostas).
- Feito em Python
- Conhecimentos básicos/intermediários
- Destaque: sistema de guardar o progresso na mesma ou em diferentes execuções implementado.
- Roda no terminal
- Banco de perguntas contém 40 questões e suas respectivas respostas

# Documentação - Jogo Quiz

## Introdução
Este documento detalha o desenvolvimento de um jogo de quiz em Python, uma aplicação interativa projetada para desafiar e entreter os jogadores com uma variedade de perguntas. O jogo é uma fusão de código estruturado e lógica de programação, criando uma experiência envolvente para os usuários.

## Metodologia

### Estrutura de Classes
O código é organizado em duas classes principais:

- **Classe `Jogador`:** Responsável por armazenar informações sobre o jogador, incluindo seu nome e pontuação.
- **Classe `Jogo`:** Encarregada de gerenciar as operações do jogo, como apresentar perguntas, verificar respostas e atualizar o ranking.

### Funcionalidades
O jogo oferece uma série de funcionalidades que garantem uma experiência dinâmica e imersiva:

- **Cadastro de Jogadores:** Antes de iniciar o jogo, os jogadores têm a oportunidade de se cadastrar, fornecendo seu nome para personalizar a experiência.
- **Apresentação de Perguntas:** O jogo seleciona aleatoriamente perguntas de um banco de dados pré-determinado e as exibe ao jogador de forma iterativa.
- **Verificação de Respostas:** Após o jogador responder uma pergunta, o jogo verifica se a resposta está correta e atualiza a pontuação do jogador de acordo.
- **Exportação e Importação de Rankings:** Os jogadores têm a capacidade de exportar seu ranking atual para um arquivo de texto e importar rankings previamente salvos, adicionando uma camada de personalização e competição ao jogo.

### Fluxo de Execução
O jogo segue um fluxo de execução bem definido, proporcionando uma experiência fluida e intuitiva para os jogadores:

1. **Menu Principal:** Ao iniciar o jogo, os jogadores são apresentados a um menu principal, oferecendo várias opções, como iniciar o jogo, gerenciar rankings e sair do jogo.
2. **Cadastro de Jogadores:** Se os jogadores optarem por iniciar o jogo, são solicitados a cadastrar seus nomes para personalizar a experiência.
3. **Jogo em Andamento:** Uma vez cadastrados, o jogo apresenta uma série de perguntas ao jogador, registrando suas respostas e atualizando sua pontuação.
4. **Final do Jogo:** Ao completar todas as perguntas ou decidir sair, os jogadores têm a opção de exportar seu ranking ou retornar ao menu principal.

### Manipulação de Arquivos
O jogo utiliza operações de leitura e escrita de arquivos em Python para armazenar informações cruciais, como o progresso do jogador e o ranking atual:

- **`Progresso.txt`:** Este arquivo contém detalhes sobre o progresso do jogador, incluindo seu nome, pontuação e o número de perguntas respondidas.
- **`Ranking.txt`:** Aqui são armazenados os rankings dos jogadores, permitindo que os jogadores exportem e importem seus rankings para competições futuras.

## Execução
Para desfrutar do jogo quiz, basta executar o arquivo Python `quiz.py` em um ambiente Python 3.x. Certifique-se de ter as dependências necessárias instaladas para uma experiência de jogo perfeita.

## Requisitos
O jogo requer o seguinte ambiente de execução:

- Python 3.x

## Conclusão
O jogo quiz em Python oferece uma jornada emocionante e desafiadora para os jogadores, combinando uma estrutura de código sólida com funcionalidades inovadoras. Esta documentação fornece uma visão abrangente do código-fonte e da metodologia por trás do jogo, destacando suas características distintivas e proporcionando uma compreensão profunda de sua mecânica de funcionamento.
