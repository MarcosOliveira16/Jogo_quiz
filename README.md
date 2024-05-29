# Jogo_quiz
Este pequeno projeto busca ser um simples jogo do tipo "Quiz" (perguntas e respostas).
- Feito em Python
- Conhecimentos básicos/intermediários
- Destaque: sistema de guardar o progresso na mesma ou em diferentes execuções implementado.
- Roda no terminal
- Banco de perguntas contém 40 questões e suas respectivas respostas


Claro! Abaixo está a documentação elaborada em estilo Markdown para o código fornecido:

```markdown
# Documentação do Jogo de Quiz

## Introdução

Este documento descreve a metodologia e a estrutura do código para um jogo de quiz desenvolvido em Python. O jogo permite que os usuários joguem um quiz interativo, importem/exportem rankings, e limpem o histórico do jogador.

## Funcionalidades

### Funções Globais

#### `limpa_tela()`
- Limpa a tela do terminal ou tela de exibição do código.

#### `menu()`
- Exibe o menu principal do jogo, mostrando as opções disponíveis.

#### `boas_vindas()`
- Exibe uma mensagem de boas-vindas ao usuário quando o jogo é iniciado.

#### `despedida()`
- Exibe uma mensagem de despedida e encerra o jogo.

#### `carrega_progresso()`
- Carrega o progresso do jogador a partir de um arquivo de texto.
- Remove as perguntas já respondidas da lista de perguntas.

#### `cadastra_players()`
- Permite que o jogador faça seu cadastro para iniciar o jogo.
- Permite continuar de onde parou da última vez, se houver progresso salvo.

#### `feedback()`
- Exibe o resultado da rodada (se o jogador acertou ou errou).

#### `exibe_resposta(resp_jogador, perguntas, id)`
- Exibe a resposta correta da pergunta e verifica se o jogador acertou.
- Atualiza os pontos do jogador.

#### `guarda_respostas(perguntas, id)`
- Recebe a resposta do jogador para a pergunta atual e a processa.

#### `salva_progresso(guarda_perguntas)`
- Salva o progresso do jogador em um arquivo de texto.
- Remove as perguntas respondidas da lista de perguntas.

#### `apaga_progresso()`
- Apaga o arquivo de progresso do jogador.

#### `status_quiz()`
- Exibe o status do quiz atual, mostrando quantas perguntas foram respondidas e quantos pontos o jogador tem.

#### `exibe_perguntas(perguntas_aux)`
- Exibe as perguntas do quiz e processa as respostas dos jogadores.

#### `exibe_ranking()`
- Exibe o ranking atual, mostrando os melhores jogadores e suas pontuações.

#### `exporta_raking()`
- Exporta o ranking atual para um arquivo de texto na nuvem.

#### `importa_ranking()`
- Importa o ranking de um arquivo de texto na nuvem.

### Estrutura do Jogo

O jogo segue a seguinte estrutura:

1. **Boas-vindas**: O jogo é iniciado com uma mensagem de boas-vindas.
2. **Menu Principal**: O usuário pode escolher entre várias opções no menu principal, como iniciar o jogo, importar/exportar rankings, exibir rankings e limpar o histórico do jogador.
3. **Jogar Quiz**: O usuário pode iniciar o jogo e responder às perguntas do quiz.
4. **Progresso e Ranking**: O progresso do jogador é salvo e atualizado conforme ele avança no jogo. Os rankings são exibidos e atualizados de acordo com as pontuações dos jogadores.
5. **Despedida**: O jogo é encerrado com uma mensagem de despedida.

## Conclusão

Este documento fornece uma visão geral da estrutura e funcionalidades do jogo de quiz desenvolvido em Python. Ele oferece uma experiência interativa para os usuários, permitindo que joguem e acompanhem seu progresso ao longo do tempo.
```

Esse documento pode ser salvo em um arquivo README.md dentro do diretório do projeto para fornecer uma referência útil sobre o funcionamento do jogo.
