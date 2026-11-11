# Exercícios e estudos de Python

Este repositório reúne scripts independentes usados para praticar conceitos introdutórios de programação com Python. Os exemplos recebem dados pelo terminal, fazem cálculos ou aplicam regras simples e mostram os resultados. Não formam uma aplicação única nem dependem uns dos outros.

## Conteúdo

### Fundamentos, strings e funções

| Arquivo | Assunto |
| --- | --- |
| `def.py` | Função que soma dois valores |
| `def2.py` | Função para calcular o IMC |
| `len.py` | Índices, tamanho e construção de strings |
| `inverso.py` | Inversão de algarismos e soma dos números |
| `num.py`, `num1.py` | Separação de algarismos e inversão de um número |
| `Untitled-1.py` | Retorno de múltiplos valores em uma função |
| `email.py` | Verificação simples de texto e extração de domínio |

### Condições e regras de negócio

| Arquivo | Assunto |
| --- | --- |
| `ex1.py` | Verificação de número dentro de um intervalo |
| `ex2.py` | Cálculo de remuneração conforme turno e horas |
| `ex3.py` | Desconto em uma compra |
| `ex4.py` | Comparação entre salário e contas |
| `exercicio1.py` | Classificação de condição eleitoral por idade |
| `exercicio2.py` | Raízes de uma equação do segundo grau |
| `exercicio3.py` | Preço de venda com margem conforme custo |
| `exercicio4.py` | Operações aritméticas escolhidas pelo usuário |
| `freq.py`, `media.py` | Aprovação por frequência ou média |
| `maiordeidade.py` | Verificação de maioridade |
| `num123.py`, `tresvalores.py` | Comparação entre três números |
| `parouimpar.py` | Identificação de número par ou ímpar |
| `parcela.py` | Cálculo de compra parcelada e acréscimos |
| `placa.py` | Restrição de circulação conforme final da placa |
| `td.py` | Cálculo de diária por tipo de acomodação |
| `prestacao.py` | Cálculo de prestação em atraso |
| `biblioteca.py`, `biblioteca2.py` | Menu para cadastrar, consultar e emprestar livros em memória |

### Repetição e sequências

| Arquivo | Assunto |
| --- | --- |
| `exemplo1.py` | Percorrer listas e exibir tamanhos de strings |
| `exemplo2.py` | Percorrer os caracteres de uma palavra |
| `exemplo3.py` | Uso de `range` com diferentes intervalos |
| `exemplo4.py` | Tabuada com laço `for` |
| `exemplo5.py` | Leitura e soma de vários valores |
| `exemplo6.py` | Conversão de número binário para decimal |
| `exemplo7.py` | Cálculo de médias em um laço `while` |
| `exemplo8.py` | Leitura contínua de valores e cálculo de média |

### Matemática e geometria

| Arquivo | Assunto |
| --- | --- |
| `raiz.py`, `raiz2.py`, `calcularraiz.py` | Cálculo de raiz quadrada por diferentes abordagens |
| `raiz3.py` | Funções matemáticas: valor absoluto, truncamento, raiz e fatorial |
| `circunferencia.py` | Comprimento e área de um círculo |
| `sen,cos,tan.py` | Funções trigonométricas |
| `predio.py` | Estimativa de altura a partir de sombra e ângulo |
| `volume da piramide.py` | Volume de um tronco de pirâmide quadrada |
| `horas pra minutos.py` | Conversão de horas para minutos |
| `idade em dias.py` | Estimativa de idade em dias |
| `imc.py` | Cálculo e classificação de IMC |

## Como executar

É necessário ter Python 3 instalado. Cada arquivo pode ser executado separadamente no terminal, a partir da pasta do repositório:

```bash
python parouimpar.py
```

No Windows, também é possível usar o inicializador `py`:

```powershell
py parouimpar.py
```

Os programas interativos solicitarão os dados durante a execução. Para executar um arquivo cujo nome contém espaços ou vírgulas, coloque o nome entre aspas, por exemplo:

```powershell
py "volume da piramide.py"
py "sen,cos,tan.py"
```

Os exemplos usam recursos nativos do Python; os scripts que fazem cálculos matemáticos importam o módulo padrão `math`. Não há dependências externas nem uma suíte de testes configurada.

## Observações

- O foco é didático: os arquivos ilustram conceitos isolados e não seguem necessariamente uma estrutura comum de aplicação.
- `biblioteca.py` e `biblioteca2.py` são versões muito semelhantes; os dados cadastrados ficam apenas na memória durante a execução.
- `tempCodeRunnerFile.py` é um arquivo temporário de editor e contém somente um fragmento incompleto; não é um exercício pronto para execução.
- Alguns scripts podem exigir entradas em formatos específicos ou conter limitações de exercícios iniciais. Revise e teste cada exemplo antes de reutilizá-lo em outro contexto.
