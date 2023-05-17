# A Alpaca Instruction Following Dataset

## Motivação
### com que motivação alpaca foi criado
Para permitir mais pesquisas de código aberto sobre o acompanhamento de instruções em grandes modelos de linguagem, foram geradas 52.000 demonstrações de acompanhamento de instruções usando o modelo text-davinci-003 da OpenAI.
### quem criou o dataset
- [Rohan Taori](https://www.rohantaori.com/)
- [Ishaan Gulrajani](https://ishaan.io/)
- [Tianyi Zhang](https://tiiiger.github.io/)
- [Yann Dubois](https://yanndubs.github.io/)
- [Xuechen Li](https://www.lxuechen.com/)
- [Carlos Guestrin](https://guestrin.su.domains/)
- [Percy Liang](https://cs.stanford.edu/~pliang/)
- [Tatsunori B. Hashimoto](https://thashim.github.io/)

## Composição

### Quais são as instâncias que compõem o conjunto de dados representam (por exemplo, documentos, fotos, pessoas, países)?
As demonstrações de seguimento [seed set](https://github.com/yizhongw/self-instruct/blob/main/data/seed_tasks.jsonl)  de instruções são criadas a partir do conjunto inicial lançado pelo projeto self-instruct. Dado que o conjunto de dados é gerado, é difícil determinar exatamente quem ou o que as instâncias representam.

### Quantas intancias há no total
no total, há  52,002 instancias no dataset.

###Os conjunto de dados  contém todas as possíveis instâncias, mas sim uma amostra (não necessariamente aleatória) de instâncias de um conjunto maior?
não aplicavel.

### De que dados cada instância consiste?

- `instruction`: `str`,  uma string que descreve a tarefa que o modelo deve realizar. Cada uma das 52.000 instruções é única.
- `input`: `str`,  uma string que descreve a tarefa que o modelo deve realizar. Cada uma das 52.000 instruções é única.
- `output`: `str`, uma string que representa a resposta à instrução gerada pelo modelo  `text-davinci-003`.

### Há alguma informação faltando nas instâncias individuais?
não.

### As relações entre as instâncias individuais são explicitamente indicadas (por exemplo, avaliações de filmes dos usuários, links de redes sociais)?
não aplicavel.

### Existe um rótulo ou alvo associado a cada instância?
O alvo de ajuste fino é a resposta gerada pelo `text-davinci-003`.
### Existem divisões de dados recomendadas (por exemplo, treinamento, desenvolvimento/validação, teste)?
Os modelos Alpaca (tanto a demonstração quanto os que serão lançados) são treinados em todos os 52.000 dados. Não há divisão recomendada dos dados para o conjunto de dados.
### Existem erros, fontes de ruído ou redundâncias no conjunto de dados?
Todas as 52.000 instruções são únicas. No entanto, algumas instruções geradas podem não ser sensatas, ou seja, pode não existir uma boa resposta para a instrução.
### O conjunto de dados é autocontido ou possui links ou dependências de recursos externos (por exemplo, sites, tweets, outros conjuntos de dados)?
o dataset é autocontindo.

### O conjunto de dados contém dados que podem ser considerados confidenciais (por exemplo, dados protegidos por privilégio legal ou por confidencialidade médico-paciente, dados que incluem o conteúdo de comunicações não públicas de indivíduos)?
não.

### O conjunto de dados contém dados que, se visualizados diretamente, podem ser ofensivos, insultantes, ameaçadores ou que possam causar ansiedade de outra forma?
As respostas geradas podem conter algumas inadequações. Em nossos testes preliminares, não encontramos nenhuma resposta ofensiva.

## Processo de coleta
O [Github repository](https://github.com/tatsu-lab/stanford_alpaca) contem o codigo para gerar o dataset

## Usos
    
### O conjunto de dados já foi utilizado em alguma tarefa?
O conjunto de dados é usado para treinar os modelos Alpaca que são utilizados tanto para demonstração quanto para lançamento.
### Existe um repositório que vincula a qualquer um ou todos os artigos ou sistemas que utilizam o conjunto de dados?
Por favor veja https://github.com/tatsu-lab/stanford_alpaca

### Existe algo sobre a composição do conjunto de dados ou a forma como foi coletado, pré-processado, limpo ou rotulado que possa afetar o uso futuro?
Este conjunto de dados é gerado usando a API da OpenAI. Portanto, este conjunto de dados não pode ser usado para fins comerciais que concorram com a OpenAI.
### Existem tarefas para as quais o conjunto de dados não deve ser usado? 
O conjunto de dados não deve ser usado para fins comerciais que concorram com a OpenAI.
## Distribuição
### O conjunto de dados pode ser distribuído a terceiros fora da entidade (por exemplo, empresa, instituição, organização) em nome da qual o conjunto de dados foi criado.
O dataset pode ser baixado gratuitamente.

### Como o conjunto de dados será distribuído (por exemplo, arquivo compactado no site, API, GitHub)?
O dataset pode ser baixado pelo:[Github repository](https://github.com/tatsu-lab/stanford_alpaca) as a json file.

### O conjunto de dados será distribuído sob uma licença de direitos autorais ou propriedade intelectual (PI), e/ou sob os termos de uso aplicáveis (ToU)?
Esse dataset é distribuido dentro [the ODC-By license](https://opendatacommons.org/licenses/by/1-0/).

### Algumas terceiras partes impuseram restrições baseadas em propriedade intelectual (PI) ou outras restrições nos dados associados às instâncias?
não

### Existem controles de exportação ou outras restrições regulatórias aplicáveis ao conjunto de dados ou a instâncias individuais?
não

## Manuntenção

### Quem está dando suporte/hospedando/manutenção ao conjunto de dados?
O conjunto de dados está hospedado no GitHub e o repositório do GitHub é mantido por Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois e Xuechen Li.
### O proprietário/curador/gerente do conjunto de dados pode ser contatado através do seguinte endereço de e-mail: [informações de contato não fornecidas].
Por favor relate o problema em [Github repository](https://github.com/tatsu-lab/stanford_alpaca)

### O conjunto de dados será atualizado (por exemplo, para corrigir erros de rotulagem, adicionar novas instâncias, excluir instâncias)?
Nós não temos planos para atualizações