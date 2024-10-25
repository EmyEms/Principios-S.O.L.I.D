## O que é S.O.L.I.D?

S.O.L.I.D é um conjunto de cinco princípios de design de software que tornam o código mais **modular, flexível e fácil de manter**. Formalizados por Robert C. Martin, esses princípios ajudam a criar sistemas que seguem boas práticas de desenvolvimento, permitindo que o código seja mais facilmente extensível, desacoplado e com responsabilidades bem definidas.

## Sobre os Códigos

# Código Inicial (Violando S.O.L.I.D.)
O código inicial apresenta um sistema de gerenciamento de partidas de um jogo online, mas viola todos os princípios S.O.L.I.D., resultando em um código com responsabilidades misturadas e difícil de manter e estender. Entre os problemas:

-Responsabilidade Única (SRP): A classe principal realiza múltiplas tarefas, como gerenciar jogadores, criar e iniciar partidas.
-Aberto/Fechado (OCP): O código contém condicionais para cada tipo de partida, dificultando a adição de novos tipos sem modificar o código existente.
-Substituição de Liskov (LSP): Não há estrutura que permita substituir tipos de partida sem modificar a lógica interna da classe principal.
-Segregação de Interfaces (ISP): A ausência de interfaces específicas aumenta o acoplamento.
-Inversão de Dependência (DIP): A classe principal depende diretamente de implementações concretas para os tipos de partida, o que reduz a flexibilidade.

# Código Refatorado (Aplicando S.O.L.I.D.)
No código refatorado, cada um dos princípios S.O.L.I.D. foi aplicado para resolver esses problemas e tornar o sistema mais modular e extensível. As principais mudanças são:

-SRP: Separação das responsabilidades em classes específicas, com Lobby gerenciando jogadores e FabricaDePartidas cuidando da criação de partidas.
-OCP: A criação de uma fábrica permite adicionar novos tipos de partidas sem modificar a lógica central.
-LSP: Tipos específicos de partida agora implementam uma interface comum, tornando-os intercambiáveis no Lobby.
-ISP: A interface Partida define apenas o método necessário, evitando métodos não utilizados.
-DIP: Lobby depende da abstração Partida, enquanto a fábrica é responsável por instanciar tipos concretos, facilitando a expansão e os testes.

