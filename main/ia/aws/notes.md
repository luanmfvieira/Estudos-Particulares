Amazon Inspector é um serviço automatizado de avaliação de segurança da AWS. Ele:

Faz varredura de vulnerabilidades em instâncias do Amazon EC2.

Avalia imagens armazenadas no Amazon Elastic Container Registry (ECR) em busca de falhas de segurança conhecidas.

Gera recomendações de correção para reduzir riscos.

---------------------------------------------------------------------------------------------------------------------

Engenharia de atributos (Feature Engineering):

Consiste em criar novas variáveis (atributos) a partir dos dados existentes, transformando ou combinando colunas para enriquecer o conjunto de treinamento.

Exemplo: extrair "dia da semana" a partir de uma data, ou criar uma variável "IMC" a partir de peso e altura.

Coleta de dados:

Ao coletar mais dados, é possível incluir novas variáveis que antes não existiam no conjunto.

Isso aumenta a diversidade e a representatividade do dataset, melhorando o desempenho do modelo.


---------------------------------------------------------------------------------------------------------------------

Amazon Transcribe é o serviço da AWS para converter fala em texto.

Ele permite criar um modelo de linguagem personalizado (Custom Language Model), que é treinado com vocabulário específico de um domínio ou setor (ex.: financeiro, médico, jurídico, call center etc.).

Isso melhora a precisão da transcrição porque o modelo aprende termos técnicos, nomes de produtos, siglas e expressões típicas da empresa.

---------------------------------------------------------------------------------------------------------------------

AWS IAM

O IAM é responsável por autenticação e autorização (quem pode acessar o quê).

Barreiras de Proteção para Amazon Bedrock 

Bedrock permite configurar guardrails para bloquear certos tópicos (ex.: violência, política, etc.).

Na AWS, Guardrail (barreira de proteção) é um conjunto de regras e controles pré-definidos que servem para limitar, monitorar e orientar o comportamento de um serviço ou aplicação, garantindo segurança, conformidade e uso adequado.

---------------------------------------------------------------------------------------------------------------------

GCP significa Google Cloud Platform.

É a plataforma de computação em nuvem do Google, que oferece vários serviços para empresas e desenvolvedores, como:

Computação: máquinas virtuais (Compute Engine), Kubernetes (GKE), funções serverless (Cloud Functions).

Armazenamento: bancos de dados SQL, NoSQL (Firestore, Bigtable), armazenamento de arquivos (Cloud Storage).

Redes: balanceadores de carga, CDN, VPCs.

IA e Machine Learning: APIs de visão, tradução, modelos de IA generativa (Vertex AI).

Ferramentas de dados: BigQuery (análise de dados), Dataflow, Pub/Sub.

---------------------------------------------------------------------------------------------------------------------

ITIL (Information Technology Infrastructure Library) é um conjunto de boas práticas para gestão de serviços de TI.
Ele ajuda empresas a organizarem processos de suporte, incidentes, mudanças, entregas e melhorias contínuas.

Principais pontos:

Service Desk: central de atendimento.

Gestão de Incidentes: resolver falhas rapidamente.

Gestão de Problemas: identificar causa raiz.

Gestão de Mudanças: controlar alterações em sistemas.

Gestão de Configuração e Ativos: mapear recursos de TI.

👉 Em resumo: ITIL é um guia de como gerir TI de forma eficiente e organizada.

---------------------------------------------------------------------------------------------------------------------

Quando uma empresa treina ou personaliza um modelo de base (FM) do zero usando seus próprios dados:

Custos mais altos (D):

Treinar modelos grandes exige muita infraestrutura computacional, armazenamento e energia.

Manutenção contínua do modelo também aumenta os custos.

Maior complexidade de implementação (E):

É necessário lidar com pré-processamento de dados, ajustes de hiperparâmetros, validação, pipelines de treinamento e escalabilidade.

O processo é mais técnico e trabalhoso do que apenas usar um FM pré-treinado.

---------------------------------------------------------------------------------------------------------------------
Cartões de modelo do SageMaker (Model Cards) são documentos estruturados que permitem registrar informações importantes sobre cada modelo de ML, como:

Uso pretendido do modelo

Classificações de risco

Detalhes do treinamento (conjuntos de dados, algoritmos, parâmetros)

Resultados de avaliação e métricas

Isso ajuda proprietários e equipes de ML a manter transparência, rastreabilidade e conformidade ao gerenciar modelos.

---------------------------------------------------------------------------------------------------------------------

opções de inferência do Amazon SageMaker AI e ordene-as da MENOR à MAIOR latência.

Inferência em tempo real:

Projetada para responder imediatamente a solicitações de predição.

Latência é muito baixa, pois o endpoint está sempre ativo.

Inferência assíncrona:

Processa solicitações que não precisam de resposta imediata.

Latência é maior que a em tempo real, pois o job é enfileirado e processado conforme recursos ficam disponíveis.

Transformação em lote (Batch Transform):

Executa predições em grandes volumes de dados de uma vez.

Não é para respostas imediatas → latência é a maior, pois processa dados em lote, de forma offline.



---------------------------------------------------------------------------------------------------------------------


Few-shot prompting: você fornece ao modelo alguns exemplos de como a tarefa deve ser realizada (ex.: descrições de produtos bem escritas no estilo do site).

O modelo aprende o padrão a partir desses exemplos e gera novos textos de forma consistente com o estilo e tom desejados.

É a técnica com menor esforço operacional porque:

Não exige treinar ou ajustar o modelo (como no fine-tuning).

Basta fornecer exemplos diretamente no prompt.

---------------------------------------------------------------------------------------------------------------------

ML significa Machine Learning, ou Aprendizado de Máquina em português.

É uma área da inteligência artificial onde computadores aprendem padrões a partir de dados e fazem previsões ou decisões sem serem explicitamente programados para cada regra.

Como funciona basicamente:

Coleta de dados: textos, imagens, números, áudio, etc.

Treinamento do modelo: o computador aprende padrões e relações nos dados.

Teste e validação: verifica se o modelo consegue fazer boas previsões com dados novos.

Inferência: o modelo já treinado é usado para fazer previsões ou tomar decisões.

Exemplos de ML no dia a dia:

Recomendação de filmes na Netflix.

Previsão do tempo.

Detecção de fraudes em cartões de crédito.

Tradução automática de idiomas.

Reconhecimento de fala e imagem.

---------------------------------------------------------------------------------------------------------------------

Amazon Bedrock permite usar modelos de IA generativa pré-treinados sem precisar:

Treinar ou ajustar modelos (ou seja, sem fine-tuning).

Gerenciar infraestrutura de ML.

Ele oferece modelos de texto, imagem e multimídia de fornecedores como AI21, Anthropic, Stability AI, etc.

No caso da empresa de turismo: basta chamar o modelo via API para gerar imagens de fundo para marketing.

---------------------------------------------------------------------------------------------------------------------

FM significa Foundation Models (Modelos de Fundação) no contexto de IA e ML.

São modelos de grande escala treinados em enormes volumes de dados que servem como base para muitas tarefas diferentes, como texto, imagem, áudio ou multimídia.

Características principais:

Pré-treinados em larga escala:

Aprendem padrões gerais de linguagem, imagens ou som a partir de enormes datasets.

Versáteis:

Podem ser usados diretamente para tarefas diversas (zero-shot ou few-shot) ou personalizados para domínios específicos.

Exemplos:

GPT (texto)

BERT (texto)

DALL·E, Stable Diffusion (imagens)

Diferença entre FM e modelos tradicionais:

Modelos tradicionais são treinados para uma tarefa específica (ex.: prever preço de casas).

FMs são genéricos e podem ser adaptados para várias tarefas com menos esforço de treinamento.

---------------------------------------------------------------------------------------------------------------------

Limitação principal da IA generativa:

Mesmo sendo poderosa para criar texto, imagens ou áudio, os modelos podem gerar conteúdos incorretos, enviesados ou inapropriados.

Por isso, sempre é necessária revisão humana antes de publicar conteúdo em um site.

---------------------------------------------------------------------------------------------------------------------

Amazon Rekognition Custom Labels:

Permite criar modelos de visão computacional personalizados para classificar imagens em categorias específicas.

Ideal para identificar rótulos personalizados de produtos com base em imagens históricas.

Fornecer imagens rotuladas:

O modelo precisa de exemplos de treinamento com categorias definidas para aprender a classificar corretamente novas imagens.

Apenas imagens não rotuladas não permitem treinar o modelo de forma supervisionada.

---------------------------------------------------------------------------------------------------------------------

Ajuste fino baseado em instruções (instruction fine-tuning) é uma técnica usada para ensinar um modelo de linguagem a responder de forma desejada a determinados prompts ou perguntas.

Para isso, o modelo precisa de pares de entrada e saída de texto:

Prompt (entrada): a instrução ou pergunta que você quer que o modelo entenda.

Resposta (saída): o texto que o modelo deve gerar ao receber aquele prompt.

{"prompt": "Explique o que é machine learning.", "response": "Machine learning é uma área da inteligência artificial onde computadores aprendem padrões a partir de dados."}

---------------------------------------------------------------------------------------------------------------------

Amazon Textract é um serviço da AWS especializado em extrair texto e dados de documentos, incluindo:

Faturas, recibos, contratos, formulários.

Suporta texto digitado e manuscrito.

Funciona com documentos em imagens (PNG, JPEG) ou PDFs.

Ele vai além do OCR tradicional porque também consegue identificar tabelas, campos de formulário e relacionamentos entre dados.

---------------------------------------------------------------------------------------------------------------------

Sobreajuste ocorre quando um modelo aprende demais os detalhes e ruídos dos dados de treinamento, ao ponto de:

Ter alta acurácia nos dados de treinamento.

Ter baixa acurácia em dados novos ou de teste, porque não generaliza bem.

É um problema comum em modelos muito complexos ou quando há poucos dados de treinamento.

O sobreajuste ocorre quando um modelo aprende com os dados de treinamento e não consegue ter um bom desempenho quando recebe novos dados. Esse fator explica por que o modelo tem alta acurácia nos dados de treinamento e baixa acurácia nos dados de teste.

---------------------------------------------------------------------------------------------------------------------

LLM significa Large Language Model (Modelo de Linguagem de Grande Escala).

É um modelo de inteligência artificial treinado para entender e gerar texto em linguagem natural.

Características principais:

Treinado em grandes volumes de dados textuais

Pode ser textos da internet, livros, artigos, códigos, etc.

Gera respostas coerentes e contextualizadas

Pode escrever textos, resumir conteúdos, responder perguntas, traduzir idiomas, criar diálogos e até gerar código.

Capaz de generalizar

Mesmo sem ser treinado especificamente para uma tarefa, consegue realizar diversas funções (zero-shot ou few-shot).

Exemplos de LLMs:

GPT (OpenAI)

BERT (Google)

Claude (Anthropic)

LLaMA (Meta)

Resumo prático:
Um LLM é um modelo de IA que entende e cria texto, usando aprendizado em larga escala para responder perguntas, gerar conteúdo ou realizar tarefas de linguagem natural.



---------------------------------------------------------------------------------------------------------------------

RAG (Retrieval-Augmented Generation) é uma técnica que permite ao modelo de linguagem acessar informações externas (bases de conhecimento, documentos, FAQs, bancos de dados) para gerar respostas mais precisas e consistentes.

Como funciona:

O modelo recebe uma pergunta ou prompt.

Busca em fontes externas documentos ou trechos relevantes.

Usa essas informações para gerar a resposta final.

Vantagem:

Requer pouco esforço de desenvolvimento, porque você não precisa treinar ou ajustar o modelo, apenas conecta ele a uma base de dados ou sistema de recuperação.

---------------------------------------------------------------------------------------------------------------------
ROUGE é uma métrica de avaliação automática de texto gerado.

É usada para comparar o texto gerado pelo modelo com textos de referência ou respostas corretas, medindo sobreposição de n-gramas, palavras ou frases.

Muito utilizada em tarefas de resumo automático, tradução e geração de texto.

---------------------------------------------------------------------------------------------------------------------

Amazon SageMaker JumpStart oferece modelos de base (FM) de código aberto prontos para uso, incluindo modelos de linguagem, visão computacional e mais.

Permite avaliar, ajustar ou implantar modelos rapidamente sem precisar treinar do zero.

No caso da empresa: é possível usar um FM de linguagem para avaliar contratos e identificar conformidade com regras e políticas.

SageMaker JumpStart é um recurso do SageMaker AI que fornece modelos de código aberto pré-treinados para você usar. O SageMaker JumpStart oferece FMs que podem ser usados para casos de uso de resumo.

---------------------------------------------------------------------------------------------------------------------

Você pode usar o IAM para controlar o acesso a recursos da AWS por meio de usuários, perfis e políticas. Você pode usar o IAM para controlar quais usuários ou serviços têm acesso ao Amazon Bedrock. Você pode usar o IAM para controlar quais ações o usuário ou serviço pode realizar. Você pode usar o IAM para proteger o acesso ao Amazon Bedrock.

---------------------------------------------------------------------------------------------------------------------


AWS CloudTrail é o serviço da AWS responsável por registrar todas as chamadas de API feitas nos serviços da AWS.

Ele fornece logs detalhados que incluem:

Qual API foi chamada

Quem (usuário ou função) fez a chamada

Quando a chamada ocorreu

Eventualmente detalhes adicionais sobre parâmetros e respostas

Esses logs são essenciais para:

Auditoria e conformidade

Rastreamento de problemas de segurança

Monitoramento de uso e operações

É possível usar o CloudTrail para monitorar e registrar em log as chamadas de API em contas da AWS. Os registros do CloudTrail contêm o evento da API, o usuário que fez a chamada de API e a hora em que a chamada foi feita.

---------------------------------------------------------------------------------------------------------------------






















