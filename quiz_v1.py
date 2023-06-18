#O código tem o intuito de ser um jogo do tipo 'quiz', perguntas e respostas

from os import path
import os
import time
import random
import copy

#Classe jogador
class jogador:
    def __init__(self):
        self.nome = ''
        self.pontos = 0
        self.acertou = False
        
#Classe quiz
class quiz:
    def __init__(self):
        self.perguntas = {'Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?\n'
                            'a) Tem entre 2 a 4 litros. São retirados 450 mililitros\n'
                            'b) Tem entre 4 a 6 litros. São retirados 450 mililitros\n'
                            'c) Tem 10 litros. São retirados 2 litros\n'
                            'd) Tem 7 litros. São retirados 1,5 litros\n'
                            'e) Tem 0,5 litros. São retirados 0,5 litros\n':0,
                            'De quem é a famosa frase “Penso, logo existo”?\n'
                            'a) Platão\n'
                            'b) Galileu Galilei\n'
                            'c) Descartes\n'
                            'd) Sócrates\n'     
                            'e) Francis Bacon\n':1,
                            'De onde é a invenção do chuveiro elétrico?\n'
                            'a) França\n'
                            'b) Inglaterra\n'
                            'c) Brasil\n'
                            'd) Austrália\n'
                            'e) Itália\n':2,
                            'Quais o menor e o maior país do mundo?\n'
                            'a) Vaticano e Rússia\n'
                            'b) Nauru e China\n'
                            'c) Mônaco e Canadá\n'
                            'd) Malta e Estados Unidos\n'
                            'e) São Marino e Índia\n':3,
                            'Qual o nome do presidente do Brasil que ficou conhecido como Jango?\n'
                            'a) Jânio Quadros\n'
                            'b) Jacinto Anjos\n'
                            'c) Getúlio Vargas\n'
                            'd) João Figueiredo\n'
                            'e) João Goulart\n':4,
                            'Qual o grupo em que todas as palavras foram escritas corretamente?\n'
                            'a) Asterístico, beneficiente, meteorologia, entertido\n'
                            'b) Asterisco, beneficente, meteorologia, entretido\n'
                            'c) Asterisco, beneficente, metereologia, entretido\n'
                            'd) Asterístico, beneficiente, metereologia, entretido\n'
                            'e) Asterisco, beneficiente, metereologia, entretido\n':5,
                            'Qual o livro mais vendido no mundo a seguir à Bíblia?\n'
                            'a) O Senhor dos Anéis\n'
                            'b) Dom Quixote\n'
                            'c) O Pequeno Príncipe\n'
                            'd) Ela, a Feiticeira\n'
                            'e) Um Conto de Duas Cidades\n':6,
                            'Quantas casas decimais tem o número pi?\n'
                            'a) Duas\n'
                            'b) Centenas\n'
                            'c) Infinitas\n'
                            'd) Vinte\n'
                            'e) Milhares\n':7,
                            'Atualmente, quantos elementos químicos a tabela periódica possui?\n'
                            'a) 113\n'
                            'b) 109\n'
                            'c) 108\n'
                            'd) 118\n'
                            'e) 92\n':8,
                            'Quais os países que têm a maior e a menor expectativa de vida do mundo?\n'
                            'a) Japão e Serra Leoa\n'
                            'b) Austrália e Afeganistão\n'
                            'c) Itália e Chade\n'
                            'd) Brasil e Congo\n'
                            'e) Estados Unidos e Angola\n':9,
                            'O que a palavra legend significa em português?\n'
                            'a) Legenda\n'
                            'b) Conto\n'
                            'c) História\n'
                            'd) Lenda\n'
                            'e) Legendário\n':10,
                            'Qual o número mínimo de jogadores em cada time numa partida de futebol?\n'
                            'a) 8\n'
                            'b) 10\n'
                            'c) 9\n'
                            'd) 5\n'
                            'e) 7\n':11,
                            'Quais os principais autores do Barroco no Brasil?\n'
                            'a) Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira\n'
                            'b) Miguel de Cervantes, Gregório de Matos e Danthe Alighieri\n'
                            'c) Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos\n'
                            'd) Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira\n'
                            'e) Álvares de Azevedo, Gregório de Matos e Bento Teixeira\n':12,
                            'Quais as duas datas que são comemoradas em novembro?\n'
                            'a) Independência do Brasil e Dia da Bandeira\n'
                            'b) Proclamação da República e Dia Nacional da Consciência Negra\n'
                            'c) Dia do Médico e Dia de São Lucas\n'
                            'd) Dia de Finados e Dia Nacional do Livro\n'
                            'e) Black Friday e Dia da Árvore\n':13,
                            'Quem pintou \'Guernica\'?\n'
                            'a) Paul Cézanne\n'
                            'b) Pablo Picasso\n'
                            'c) Diego Rivera\n'
                            'd) Tarsila do Amaral\n'
                            'e) Salvador Dalí\n':14,
                            'Quanto tempo a luz do Sol demora para chegar à Terra?\n'
                            'a) 12 minutos\n'
                            'b) 1 dia\n'
                            'c) 12 horas\n'
                            'd) 8 minutos\n'
                            'e) 12 segundos\n':15,
                            'Qual a tradução da frase \'Fabiano cogió su saco antes de salir\'?\n'
                            'a) Fabiano coseu seu paletó antes de sair\n'
                            'b) Fabiano fechou o saco antes de sair\n'
                            'c) Fabiano pegou seu paletó antes de sair\n'
                            'd) Fabiano cortou o saco antes de cair\n'
                            'e) Fabiano rasgou seu paletó antes de cair\n':16,
                            'Qual a nacionalidade de Che Guevara?\n'
                            'a) Cubana\n'
                            'b) Peruana\n'
                            'c) Panamenha\n'
                            'd) Boliviana\n'
                            'e) Argentina\n':17,
                            'Quais são os três predadores do reino animal reconhecidos pela habilidade de caçar em grupo, se camuflar para surpreender as presas e possuir sentidos apurados, respectivamente:\n'
                            'a) Tubarão branco, crocodilo e sucuri\n'
                            'b) Tigre, gavião e orca\n'
                            'c) Hiena, urso branco e lobo cinzento\n'
                            'd) Orca, onça e tarântula\n'
                            'e) Leão, tubarão branco e urso cinzento\n':18,
                            'Qual a altura da rede de vôlei nos jogos masculino e feminino?\n'
                            'a) 2,4 para ambos\n'
                            'b) 2,5 m e 2,0 m\n'
                            'c) 1,8 m e 1,5 m\n'
                            'd) 2,45 m e 2,15 m\n'
                            'e) 2,43 m e 2,24 m\n':19,
                            'Em que ordem surgiram os modelos atômicos?\n'
                            'a) Thomson, Dalton, Rutherford, Rutherford-Bohr\n'
                            'b) Rutherford-Bohr, Rutherford, Thomson, Dalton\n'
                            'c) Dalton, Rutherford-Bohr, Thomson, Rutherford\n'
                            'd) Dalton, Thomson, Rutherford-Bohr, Rutherford\n'
                            'e) Dalton, Thomson, Rutherford, Rutherford-Bohr\n':20,
                            'Qual personagem folclórico costuma ser agradado pelos caçadores com a oferta de fumo?\n'
                            'a) Caipora\n'
                            'b) Saci\n'
                            'c) Lobisomem\n'
                            'd) Boitatá\n'
                            'e) Negrinho do Pastoreio\n':21,
                            'Em que período da pré-história o fogo foi descoberto?\n'
                            'a) Neolítico\n'
                            'b) Paleolítico\n'
                            'c) Idade dos Metais\n'
                            'd) Período da Pedra Polida\n'
                            'e) Idade Média\n':22,
                            'Qual das alternativas abaixo apenas contêm classes de palavras?\n'
                            'a) Vogais, semivogais e consoantes\n'
                            'b) Artigo, verbo transitivo e verbo intransitivo\n'
                            'c) Fonologia, Morfologia e Sintaxe\n'
                            'd) Hiatos, ditongos e tritongos\n'
                            'e) Substantivo, verbo e preposição\n':23,
                            'Qual a montanha mais alta do Brasil?\n'
                            'a) Pico da Neblina\n'
                            'b) Pico Paraná\n'
                            'c) Monte Roraima\n'
                            'd) Pico Maior de Friburgo\n'
                            'e) Pico da Bandeira\n':24,
                            'Qual a velocidade da luz?\n'
                            'a) 300 000 000 metros por segundo (m/s)\n'
                            'b) 150 000 000 metros por segundo (m/s)\n'
                            'c) 199 792 458 metros por segundo (m/s)\n'
                            'd) 299 792 458 metros por segundo (m/s)\n'
                            'e) 30 000 000 metros por segundo (m/s)\n':25,
                            'Em qual local da Ásia o português é língua oficial?\n'
                            'a) Índia\n'
                            'b) Filipinas\n'
                            'c) Moçambique\n'
                            'd) Macau\n'
                            'e) Portugal\n':26,
                            '\'It is six twenty\' ou \'twenty past six\'. Que horas são em inglês?\n'
                            'a) 12:06\n'
                            'b) 6:20\n'
                            'c) 2:20\n'
                            'd) 6:02\n'
                            'e) 12:20\n':27,
                            'Quem é o autor de \'O Príncipe\'?\n'
                            'a) Maquiavel\n'
                            'b) Antoine de Saint-Exupéry\n'
                            'c) Montesquieu\n'
                            'd) Thomas Hobbes\n'
                            'e) Rousseau\n':28,
                            'Como é a conjugação do verbo caber na 1.ª pessoa do singular do presente do indicativo?\n'
                            'a) Eu caibo\n'
                            'b) Ele cabe\n'
                            'c) Que eu caiba\n'
                            'd) Eu cabo\n'
                            'e) Nenhuma das alternativas\n':29,
                            'Quais destas construções famosas ficam nos Estados Unidos?\n'
                            'a) Estátua da Liberdade, Golden Gate Bridge e Empire State Building\n'
                            'b) Estátua da Liberdade, Big Ben e The High Line\n'
                            'c) Angkor Wat, Taj Mahal e Skywalk no Grand Canyon\n'
                            'd) Lincoln Memorial, Sidney Opera House e Burj Khalifa\n'
                            'e) 30 St Mary Axe, The High Line e Residencial 148 Spruce Street\n':30,
                            'Quais destas doenças são sexualmente transmissíveis?\n'
                            'a) Aids, tricomoníase e ebola\n'
                            'b) Chikungunya, aids e herpes genital\n'
                            'c) Gonorreia, clamídia e sífilis\n'
                            'd) Botulismo, cistite e gonorreia\n'
                            'e) Hepatite B, febre tifoide e hanseníase\n':31,
                            'Qual destes países é transcontinental?\n'
                            'a) Rússia\n'
                            'b) Filipinas\n'
                            'c) Marrocos\n'
                            'd) Groenlândia\n'
                            'e) Tanzânia\n':32,
                            'Em qual das orações abaixo a palavra foi empregada incorretamente?\n'
                            'a) Mais uma vez, portou-se mal.\n'
                            'b) É um homem mal.\n'
                            'c) Esse é o mal de todos.\n'
                            'd) Mal falou nele, o fulano apareceu.\n'
                            'e) É um mau vendedor.\n':33,
                            'Qual foi o recurso utilizado inicialmente pelo homem para explicar a origem das coisas?\n'
                            'a) A Filosofia\n'
                            'b) A Biologia\n'
                            'c) A Matemática\n'
                            'd) A Astronomia\n'
                            'e) A Mitologia\n':34,
                            'Qual das alternativas menciona apenas símbolos nacionais?\n'
                            'a) Bandeira insígnia da presidência, bandeira nacional, brasão, hinos e selo\n'
                            'b) Bandeira nacional, armas nacionais, hino nacional e selo nacional\n'
                            'c) Bandeira nacional, brasão, hino nacional e hino da independência\n'
                            'd) Bandeira nacional, cores nacionais, hino nacional e hino da independência\n'
                            'e) Bandeira insígnia da presidência, brasão flora e fauna e hinos\n':35,
                            'Quais os planetas do sistema solar?\n'
                            'a) Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio\n'
                            'b) Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Terra, Urano, Vênus\n'
                            'c) Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio\n'
                            'd) Júpiter, Marte, Mercúrio, Netuno, Plutão, Saturno, Sol, Terra, Urano, Vênus\n'
                            'e) Terra, Vênus, Saturno, Júpiter, Marte, Netuno, Mercúrio\n':36,
                            'Qual era o nome de Aleijadinho?\n'
                            'a) Alexandrino Francisco Lisboa\n'
                            'b) Manuel Francisco Lisboa\n'
                            'c) Alex Francisco Lisboa\n'
                            'd) Francisco Antônio Lisboa\n'
                            'e) Antônio Francisco Lisboa\n':37,
                            'Júpiter e Plutão são os correlatos romanos de quais deuses gregos?\n'
                            'a) Ares e Hermes\n'
                            'b) Cronos e Apolo\n'
                            'c) Zeus e Hades\n'
                            'd) Dionísio e Deméter\n'
                            'e) Zeus e Ares\n':38,
                            'Qual o maior animal terrestre?\n'
                            'a) Baleia Azul\n'
                            'b) Dinossauro\n'
                            'c) Elefante africano\n'
                            'd) Tubarão Branco\n'
                            'e) Girafa\n':39}
        
        self.respostas = ['Alternativa b: Entre 4 a 6 litros. São retirados 450 mililitros.',
                          'Alternativa c: Descartes.',
                          'Alternativa c: Brasil.',
                          'Alternativa a: Vaticano e Rússia.'
                          'O Vaticano, sede da igreja católica, tem apenas 44 hectares (0,44 km2). A Rússia, localizada em dois continentes (Ásia e Europa), tem 17 milhões de km2.',
                          'Alternativa e: João Goulart.'
                          'João Belchior Marques Goulart (1919-1976) foi o 24º presidente do Brasil, cujo período de governo compreende os anos de 1961 a 1964.',
                          'Alternativa b: Asterisco, beneficente, meteorologia, entretido.'
                          'Estas palavras são exemplos de barbarismo, um vício de linguagem em que as palavras são pronunciadas ou escritas incorretamente.',
                          'Alternativa b: Dom Quixote.'
                          'Dom Quixote, de Miguel de Cervantes, é um clássico da literatura espanhola. A obra foi escrita em duas partes, uma em 1605, e a outra em 1615.',
                          'Alternativa c: Infinitas.'
                          'Ao longo dos tempos, vários estudiosos têm se dedicado a calcular o número pi e já chegaram ao número de 62,8 trilhões de casas decimais.',
                          'Alternativa d: 118.'
                          'Os últimos elementos foram adicionados à tabela periódica em 2016. Eles são: 113 (Nihônio), 115 (Moscóvio), 117 (Tenessino) e 118 (Oganessônio).',
                          'Alternativa a: Japão e Serra Leoa.'
                          'No Japão, a expectativa de vida é em média 84 anos, enquanto na Serra Leoa é 53 anos.',
                          'Alternativa d: Lenda.'
                          'Legend, que parece significar “legenda”, faz parte do grupo dos falsos cognatos. Falsos cognatos são palavras de línguas distintas que apresentam semelhanças na grafia e/ou na pronúncia, mas cujos significados são diferentes. Outros exemplos são: costume, que significa fantasia, e to push, que significa empurrar.',
                          'Alternativa e: 7.'
                          'Uma partida de futebol conta com o número máximo de 11 jogadores e mínimo de 7, contando com o goleiro, em cada equipe.',
                          'Alternativa a: Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira.'
                          'Gregório de Mato (1633-1696), conhecido como Boca do Inferno, é o maior representante do Barroco no Brasil. Tinha esse apelido devido às críticas sociais contidas na sua poesia.'
                          'Bento Teixeira (1561-1618) é o autor do poema Prosopopeia, publicado em 1601, que é considerado o marco inicial do Barroco brasileiro.'
                          'Manuel Botelho de Oliveira (1636-1711), um dos grandes representantes do Barroco, é autor do livro Música do Parnaso, publicado em Lisboa quando o autor tinha quase 70 anos. Trata-se da sua obra com maior destaque.',
                          'Alternativa b: Proclamação da República e Dia Nacional da Consciência Negra.'
                          'A Proclamação da República é comemorada no dia 15 de novembro, data em que Marechal Deodoro da Fonseca proclamou a república em 1889.'
                          'O Dia Nacional da Consciência Negra é comemorado no dia 20 de novembro, data em que Zumbi dos Palmares morreu, em 1695.',
                          'Alternativa b: Pablo Picasso.'
                          'Pablo Picasso (1881-1973) pintou Guernica, uma das suas obras de maior destaque, em 1937. A pintura feita em óleo sobre tela retrata o bombardeio à cidade espanhola Guernica em 26 de abril de 1937, aquando da Guerra Civil Espanhola.',
                          'Alternativa d: 8 minutos.'
                          'Essa é uma questão que se fundamenta na ótica. Ela é calculada com base na distância do Sol em relação à Terra, que é de aproximadamente 150 000 000 km, considerando que a velocidade da luz no vácuo é 300 000 Km/s.'
                          '150 000 000 dividido por 300 000 é igual a 500 segundos, ou seja, 8,33 minutos.',
                          'Alternativa c: Fabiano pegou seu paletó antes de sair.'
                          'Apesar da grafia e da pronúncia semelhantes, saco em espanhol, significa paletó em português.'
                          'Este é um dos falsos cognatos mais conhecidos da língua espanhola. Outros exemplos são: apellido, que significa sobrenome, e embarazada, que significa grávida.',
                          'Alternativa e: Argentina.'
                          'Conhecido como um dos líderes da Revolução Cubana, ao lado dos irmãos Fidel e Raúl Castro, Ernesto Guevara de La Serna nasceu em Rosário, Argentina, no dia 14 de junho de 1928.',
                          'Alternativa c: Hiena, urso branco e lobo cinzento.'
                          'A hiena é o único animal que enfrenta o leão, atacando-o quando estão em grupo. Enquanto isso, o urso branco, ou urso polar, se camufla entre o gelo do Ártico. O lobo cinzento, por sua vez, tem excelentes audição e visão noturna, características que fazem dele grandes caçadores.',
                          'Alternativa e: 2,43 m e 2,24 m.'
                          'Antigamente, a altura era de 1,98 m. Atualmente é 2,43 m para jogadores adultos masculinos e 2,24 m para jogadores adultos femininos. A altura da rede também varia de acordo com a idade dos jogadores.',
                          'Alternativa e: Dalton, Thomson, Rutherford, Rutherford-Bohr.'
                          'Ao logo dos tempos, os modelos atômicos evoluíram. O Modelo atômico de Dalton foi proposto em 1803. Em 1898 foi a vez de Thomson apresentar o seu modelo. Em 1911, Rutherford mostrou a sua proposta. Pouco depois, baseado no modelo de Rutherford, o cientista Niels Bohr aprimorou um modelo que apresentou em 1913, o Modelo atômico de Rutherford-Bohr.',
                          'Alternativa a: Caipora.'
                          'Considerada a protetora da floresta, a Caipora assusta os caçadores, os quais levam-lhe fumo de corda. O fumo é deixado junto a um tronco de árvore com o intuito de agradar a Caipora para, assim, os caçadores poderem caçar.',
                          'Alternativa b: Paleolítico.'
                          'Foi no Paleolítico que o fogo começou a ser utilizado, quando os homens aprenderam que era possível obter fogo por meio do atrito de pedaços de madeira e pedra.',
                          'Alternativa e: Substantivo, verbo e preposição.'
                          'Classes de palavras são palavras que se organizam de acordo com as suas funções na língua portuguesa. Existem 10 classes de palavras: substantivo, verbo, preposição, adjetivo, pronome, artigo, numeral, conjunção, interjeição e advérbio.',
                          'Alternativa a: Pico da Neblina.'
                          'O Pico da Neblina é o ponto mais elevado do Brasil, contando com 2995 metros de altura. Localiza-se no Amazonas, na fronteira com a Venezuela e a Colômbia.',
                          'Alternativa d: 299 792 458 metros por segundo (m/s).'
                          'A primeira medição real da luz foi feita pelo astrônomo Ole Romer, que em 1676 chegou a um número próximo da velocidade da luz. Hoje, sabe-se com precisão que a velocidade da luz é 299 792 458 metros por segundo.',
                          'Alternativa d: Macau.'
                          'Macau tem duas línguas oficiais, mandarim e português. Macau, uma região especial da China, foi território português até 1999.',
                          'Alternativa b: 6:20.'
                          'Em inglês, “past” é usado para indicar até 29 minutos passados de uma determinada hora. A partir de trinta minutos, é usada a expressão “half past”: It is half past eight. ou It is eight thirty.',
                          'Alternativa a: Maquiavel.'
                          'O Príncipe é a obra mais célebre de Nicolau Maquiavel (1469-1527). Foi publicada postumamente, em 1532, apesar de ter sido concluída em 1513.',
                          'Alternativa a: Eu caibo.'
                          'Caber é um verbo irregular da 2ª conjugação. Apesar de estranho, “eu caibo” é a forma correta de conjugá-lo na 1ª pessoa do presente do indicativo.',
                          'Alternativa a: Estátua da Liberdade, Golden Gate Bridge e Empire State Building.'
                          'A Estátua da Liberdade, localizada na Ilha da Liberdade em Manhattan, Nova York, pode ser vista de vários locais, graças a sua altura, que é de 92,99 metros.'
                          'Golden Gate Bridge, localizada em São Francisco, na Califórnia, é o principal cartão postal da cidade.'
                          'Empire State Building, localizada em Manhattan, Nova York, mais precisamente na Quinta Avenida, é um arranha-céu de 102 andares.',
                          'Alternativa c: Gonorreia, clamídia e sífilis.'
                          'Gonorreia e clamídia são infecções sexualmente transmissíveis (IST) causadas por bactérias, que podem atingir além dos órgãos genitais, a garganta e os olhos.'
                          'Sífilis também é uma infecção sexualmente transmissível, cujo principal sintoma é uma ferida no pênis, vulva, vagina, colo uterino, ânus, boca, ou outros locais da pele.',
                          'Alternativa a: Rússia.'
                          'A Rússia, cujo nome oficial é Federação Russa, é o maior país em extensão territorial do mundo. Essa nação é transcontinental, pois pertence a mais de um continente: Europa e Ásia.',
                          'Alternativa b: É um homem mal.'
                          '\'Mal\' e \'mau\' são duas palavras homófonas, ou seja, são pronunciadas da mesma maneira, porém escritas de maneiras diferentes. A palavra mal com \'l\' é antônima de bem; já a palavra mau com \'u\' é antônimo de bom.',
                          'Alternativa e: A Mitologia.'
                          'A mitologia é um sistema de crenças que inclui uma série de narrativas e lendas, as quais fizeram parte do imaginário coletivo de diversas civilizações antigas. Dessa forma, no começo do desenvolvimento da humanidade, diversos povos utilizaram a mitologia para explicar alguns fenômenos e a origem das coisas.',
                          'Alternativa b: Bandeira nacional, armas nacionais, hino nacional e selo nacional.'
                          'Os Símbolos Nacionais são: a bandeira nacional, as armas nacionais ou brasão da república, o selo nacional e o hino nacional. Implementados pela Lei n° 5.700, de 1º de setembro de 1971, juntos, eles representam a união do nosso país.',
                          'Alternativa a: Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio.'
                          'O Sistema Solar é formado por oito planetas: Terra, Vênus, Saturno, Urano, Júpiter, Marte, Netuno, Mercúrio. Além disso, ele é constituído por dezenas de satélites naturais, milhares de asteroides, meteoros, meteoroides e cometas que giram em torno do Sol.',
                          'Alternativa e: Antônio Francisco Lisboa.'
                          'Aleijadinho (1730-1814), apelido de Antônio Francisco Lisboa, foi um dos maiores representantes do barroco brasileiro. Recebeu essa alcunha pois foi acometido por uma doença que deformou sua mãos e pés. No entanto, mesmo nessas condições, continuou trabalhando como escultor, entalhador, carpinteiro e arquiteto.',
                          'Alternativa c: Zeus e Hades.'
                          'Na mitologia romana, Júpiter tem Zeus como seu correlato grego. Ele é considerado o pai dos deuses, sendo o deus dos céus, da chuva, da luz e do raio. Já Plutão, tem Hades como seu correlato grego, o deus do submundo e dos infernos.',
                          'Alternativa c: Elefante africano.'
                          'O elefante africano é o maior animal terrestre. Ele pode medir até 4 metros de altura e 7 de comprimento. Seu peso pode chegar até 8 toneladas.']
        

#Variáveis globais
player = jogador()
comecar_jogo = quiz()
bandeira = False #Para auxiliar na exibição do ranking
lido = None #Usado para importar um raking
cont = 0  # 'cont' é usado para perguntar se a pessoa deseja sair ou não do quiz
deletei = False #Para evitar que fique guardado após executar uma importação e depois apagar o historico
aux_perguntas = copy.deepcopy(comecar_jogo.perguntas) #Guarda as perguntas para caso em uma mesma execução o usuario finalize o quiz e possa jogá-lo novamente
encerrou = -1 #Controlar a exibição de pontos de uma partida inacabada no ranking
mesma_execucao = True
respondidas = None #Guarda a quantidade de perguntas respondidas para exibir na def status_quiz

#Funções globais
#Limpa a tela (terminal ou tela de exibição do código)
def limpa_tela():
    os.system('cls') or None

def menu():
    print("\n* ---------------- Menu ---------------- *\n"
      "|          1 - Iniciar                   |\n"
      "|          2 - Importar ranking          |\n"
      "|          3 - Exportar ranking          |\n"
      "|          4 - Exibe ranking             |\n"
      "|          5 - Reiniciar ranking         |\n"
      "|          6 - Sair                      |\n"
     "* -------------------------------------- *\n")

def boas_vindas():
    print("---------------------------------------------\n"
        "|                                           |\n"
        "|                                           |\n"
        "|          Olá, bem vindo ao quiz!          |\n"
        "|                                           |\n"
        "|                                           |\n"
        "---------------------------------------------")
    
def despedida():
    print("------------------------------------------\n"
      "|                                          |\n"
      "|                                          |\n"
      "|          Nesse caso até mais...          |\n"
      "|                                          |\n"
      "|                                          |\n"
      "---------------------------------------------")
    time.sleep(3)
    quit()

def carrega_progresso():
    #Caso seja a mesma execução esse código não deve ser executado, pq a pergunta já foi removida
    if mesma_execucao == True:
        return
    with open('Progresso.txt', 'r') as arquivo:
        ler = arquivo.readlines()

    aux = copy.deepcopy(ler)
    for linha in aux:
        if 'Player' in linha:
            achar = '\n'
            guarda_ind_nome = linha.find(achar)
            player.nome = linha[8:guarda_ind_nome]
            ler.pop(0)
        if 'Ponto(s)' in linha:
            achar = '\n'
            guarda_ind_pontos = linha.find(achar)
            player.pontos = int(linha[10:guarda_ind_pontos])
            ler.pop(0)
        if 'Respondida(s)' in linha:
            achar = '\n'
            guarda_ind_resp = linha.find(achar)
            global respondidas
            respondidas = int(linha[15:guarda_ind_resp])
            ler.pop(0)
            break

    #Reescrevo o arquivo para poder excluir as perguntas já respondidas na execução anterior
    arquivo = open('Progresso.txt', 'wt')
    for pergunta in ler:
        arquivo.writelines(pergunta)
    arquivo.close()

    #Uso o novo arquivo para remover as perguntas ditas acima
    arquivo = open('Progresso.txt', 'rt')
    ler = arquivo.read()
    remover_itens = []
    for chave, valor in comecar_jogo.perguntas.items():
        if chave in ler:
           remover_itens.append(chave)

    for item in remover_itens:
        comecar_jogo.perguntas.pop(item)
    global deletei
    deletei = False

#Cadastramento do jogador
def cadastra_players():
    arquivo_existe = path.exists('Progresso.txt')
    if arquivo_existe:
        aux = input('Deseja continuar de onde parou da última vez? (S/N)\nR:')
        carregar = aux.upper()
        if carregar == 'S':
            global mesma_execucao
            mesma_execucao = False
            limpa_tela()
            carrega_progresso()
            return
        else:
            apaga_progresso()

    #zera os pontos ao iniciar uma nova gameplay
    player.pontos = 0
    print("\nVamos começar com o seu cadastrando, tá?!? =D\n")
    #Esperar a interação do usuário para prosseguir
    input('\nPressione qualquer tecla para continuar.')

    global deletei
    deletei = False
    global bandeira
    bandeira = False
    global respondidas
    respondidas = 0
    print('-' * 20, "Cadastro de jogador", '-' * 20)
    player.nome = input("Digite seu nome: ")

    print('-' * 20, "Fim do cadastro", '-' * 20, '\n')
    input('\nPressione qualquer tecla para continuar.')
    limpa_tela()

#Feedback da rodada
def feedback():
    print("Resultado da rodada:")
    if player.acertou == True:
        print('Acertou!')
        player.acertou = None #Para resetar o atributo 'acertou' nas próximas execuções
    else:
        print('Errou!')

def exibe_resposta(resp_jogador, perguntas, id):
    #Exibe resposta
    print(f"\nResposta: {comecar_jogo.respostas[id]}\n")
    #verifica as respostas de cada candidato, se certa atribui 1 ponto
    # o segundo indice é '12' pq o caracter referente a letra que será a resposta correta, esta na posição 12
    if resp_jogador == comecar_jogo.respostas[id][12]:
        player.pontos += 1
        player.acertou = True

    feedback()
    
    comecar_jogo.perguntas.pop(perguntas) #Recebe só o texto do dicionario
    input('\nPressione qualquer tecla para continuar.')


def guarda_respostas(perguntas, id):
    #Guarda as respostas de cada participante
    resp_jogador = input('Digite sua resposta: ')
    exibe_resposta(resp_jogador, perguntas, id)

def salva_progresso(guarda_perguntas):
#como fazer o sistema de progresso: criar um arquivo para guardar uma lista de perguntas que já foram feitas
# e comparar com a lista geral ao iniciar(e ir removendo as já feitas), pra assim pular as questões que já 
# foram feitas.
    arquivo = open('Progresso.txt', 'wt')
    arquivo.write("Player: " + player.nome + "\n" + "Ponto(s): " + str(player.pontos) + '\n' + 'Respondida(s): ' + str(respondidas) + '\n')
    for pergunta in guarda_perguntas:
        arquivo.writelines(pergunta)
    arquivo.close()
    print('Progresso atual salvo.')
    global encerrou
    encerrou = 1
    
    return -1

def apaga_progresso():
    path = "H:\VS Code\Codigos"
    dir = os.listdir(path)
    for file in dir:
        if file == "Progresso.txt":
            os.remove(file)


def status_quiz():
    print(f'Perguntas ({respondidas}/{len(aux_perguntas)}) - Acertos ({player.pontos}/{len(aux_perguntas)}))')

def exibe_perguntas(perguntas_aux):
    #'Guarda_perguntas' serve para guarda as perguntas que já foram feitas
    guarda_perguntas = []
    #Exibe perguntas
    for perguntas in perguntas_aux:
        print('\n', '-' * 20, "Quiz em andamento...", '-' * 20, '\n')
        status_quiz()
        #Gera uma ordem aleatoria na sequencia de perguntas
        perguntas, id = random.choice(list(comecar_jogo.perguntas.items()))
        print(perguntas)
        #'Guarda_perguntas' serve para guarda as perguntas que já foram feitas
        guarda_perguntas.append(perguntas)
        guarda_respostas(perguntas, id)
        global respondidas
        respondidas += 1
        global cont 
        cont += 1
        if cont > 0 and cont < len(perguntas_aux):
            #Controla quando vai ser permitida a chamada da função 'salva_progresso'
            aux = input("Deseja continuar o quiz? (S/N)\nR:")
            controle = aux.upper()
            if controle == 'N':
                cont = 0
                #Leva a função 'salva_progresso' e permiti retornar ao menu inicial
                cont_programa = salva_progresso(guarda_perguntas)
                if cont_programa == -1:
                    input('\nPressione qualquer tecla para voltar ao menu.')
                    limpa_tela()
                    return
                
        limpa_tela()
    print('\n', '-' * 20, "Fim do quiz", '-' * 20, '\n')
    print('Resultado final:')
    status_quiz()
    apaga_progresso()
    cont = 0
    global encerrou
    encerrou = -1
    #Restaura as perguntas
    comecar_jogo.perguntas = copy.deepcopy(aux_perguntas)

#Exibe ranking
def exibe_ranking():
    if deletei:
        print('Não existe nenhuma pontuação.')
        input('\nPressione qualquer tecla para voltar ao menu.')
        return
    #Exibe o ranking importado, caso o mesmo exista
    if bandeira != False:
        print(lido)
        input('\nPressione qualquer tecla para voltar ao menu.')
        return
    if encerrou == 1:
        print('Há uma partida em andamento, conclua está partida e o rank será exibido.')
        input('\nPressione qualquer tecla para voltar ao menu.')
        return
    if player.pontos > 0:
        print('-' * 20, "Recorde", '-' * 20, '\n')
        print("Player: " + player.nome + " - " + "ponto(s): ", player.pontos)
    else:
        print('Não existe nenhuma pontuação.')

    input('\nPressione qualquer tecla para voltar ao menu.')
    limpa_tela()

#Server para salvar o ranking de maneira a exibí-lo
def exporta_raking():
    aux = input('Essa ação excluirá o seu rank guardado na nuvem, se houver algum.\nDeseja prosseguir? (S/N)\nR:')
    prosseguir = aux.upper()
    if prosseguir == 'S':
        if player.nome != '':
            arquivo = open('Ranking.txt', 'wt')
            arquivo.write("Player: " + player.nome + " - " + " ponto(s): " + str(player.pontos))
            arquivo.close()
            print('Ranking salvo na nuvem com sucesso.')
        elif bandeira:
            print('O atual ranking, já é o salvo na nuvem.')
        else:
            print('Não existe um ranking para ser salvo na nuvem.')
    else:
        print("Operação cancelada.")
    input('\nPressione qualquer tecla para voltar ao menu.')
    limpa_tela()

def importa_ranking():
    #Serve para saber se importei algum rank
    arquivo_existe = path.exists('Ranking.txt')
    if arquivo_existe:
        arquivo = open('Ranking.txt', 'rt')
        print('-' * 20, "Recorde", '-' * 20, '\n')
        for linha in arquivo:
            print(linha + '\n')
        arquivo.close()
        aux = input("Deseja importar este rank? (S/N)\nR:")
        importar = aux.upper()
        if importar == 'S':
            if arquivo_existe:
                global bandeira
                bandeira = True
                arquivo = open('Ranking.txt', 'rt')
                global lido 
                lido = arquivo.read()
                arquivo.close()
                print("Ranking importado.")
                global deletei
                deletei = False
            else:
                print('Não há um \'raking\' para que se possa salvá-lo')
    else:
        print('Não foi encontrado nenhum ranking para importar.')
    input('\nPressione qualquer tecla para voltar ao menu.')
    limpa_tela()


#Apresentação
boas_vindas()
input('\nPressione qualquer tecla para continuar.')

while True:
    limpa_tela()     
    while True:
        menu()
        try:
            opcao = int(input("Digite a opção: "))
            if type(0) == type(opcao):
                break
        except:
            print("Digite apenas números!")

    limpa_tela()
    while True:
        #Inicio + cadastro dos jogadores
        if opcao == 1:
            cadastra_players()
            #Iniciando quiz
            #Faz com que seja possível usar o metodo 'pop' dentro do for, pois não ira mudar o tamanho do dicionario
            perguntas_aux = list(comecar_jogo.perguntas)
            exibe_perguntas(perguntas_aux)
            break
        
        #Importa ranking
        elif opcao == 2:
            importa_ranking()
            break

        #Exporta ranking
        elif opcao == 3:
            exporta_raking()
            break

        #Ranking
        elif opcao == 4:
            exibe_ranking()
            break
        
        #Apagar o histórico do player
        elif opcao == 5:
            if len(player.nome) > 0:
                print('Histórico apagado com sucesso.')
                del player
                player = jogador()
                deletei = True
                bandeira = False
            else:
                print('Histórico vazio.')
            input('\nPressione qualquer tecla para voltar ao menu.')
            limpa_tela()
            
            break

        elif opcao == 6:
            despedida()

        else:
            print('Opção inválida, reveja o \'menu\'!')
            input('\nPressione qualquer tecla para voltar ao menu.')
            limpa_tela()
            break