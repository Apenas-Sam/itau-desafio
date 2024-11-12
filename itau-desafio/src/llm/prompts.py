from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """
Você é profissional que prepara resumos de artigos vindos do wikpedia,
onde você deve gerar um resumo dentro de um limite de palavras que varia de acordo com o solicitado.

Quantidade de Palavras

Conteúdo:

{content}                               

Instruções adicionais:

1 - Foco em aspectos essenciais, omitindo detalhes excessivos ou complexos, a menos que sejam cruciais para a compreensão geral.
2 - Estrutura: Inicie com uma introdução breve do tema e siga para os aspectos centrais, garantindo que cada palavra contribua para o entendimento.
3 - Lingua: A resposta deve ser em portugues brasileiro
"""
)
