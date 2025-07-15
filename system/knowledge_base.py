TIPOS_CONDUTA = [
    "I - Improbidade acadêmica",
    "II - Prestação de informação falsa",
    "III - Inutilização ou retirada de documentos",
    "IV - Retirada de objetos/documentos sem permissão",
    "V - Dano ao patrimônio",
    "VI - Perturbação ou falta de urbanidade",
    "VII - Agressão física ou moral",
    "VIII - Infração considerada ilícito penal"
]

MAPEAMENTO_CONDUTAS = {
    "I - Improbidade acadêmica": {
        "tipo": "improbidade_academica",
        "agravantes_possiveis": ["reincidencia"],
        "descricao_detalhada": "Improbidade na execução dos trabalhos acadêmicos",
        "artigo_base": "Art. 219, I"
    },
    "II - Prestação de informação falsa": {
        "tipo": "informacao_falsa",
        "agravantes_possiveis": ["reincidencia"],
        "descricao_detalhada": "Prestação de informação falsa nos processos seletivos ou em outros processos no âmbito da Universidade",
        "artigo_base": "Art. 219, II"
    },
    "III - Inutilização ou retirada de documentos": {
        "tipo": "inutilizacao_documentos",
        "agravantes_possiveis": ["reincidencia"],
        "descricao_detalhada": "Inutilização, adulteração ou falsificação de documentos de órgãos da Universidade",
        "artigo_base": "Art. 219, III"
    },
    "IV - Retirada de objetos/documentos sem permissão": {
        "tipo": "retirada_sem_permissao",
        "agravantes_possiveis": ["reincidencia"],
        "descricao_detalhada": "Retirada, sem prévia permissão da autoridade competente, de objeto ou documento da Universidade ou de órgãos complementares",
        "artigo_base": "Art. 219, IV"
    },
    "V - Dano ao patrimônio": {
        "tipo": "dano_patrimonio",
        "agravantes_possiveis": ["reincidencia", "violencia_ou_ameaca_grave"],
        "descricao_detalhada": "Dano ao patrimônio científico, cultural e material da Universidade ou de órgãos complementares",
        "artigo_base": "Art. 219, V"
    },
    "VI - Perturbação ou falta de urbanidade": {
        "tipo": "perturbacao",
        "agravantes_possiveis": ["reincidencia", "violencia_ou_ameaca_grave"],
        "descricao_detalhada": "Perturbação dos trabalhos escolares, das atividades científicas ou do convívio no âmbito universitário",
        "artigo_base": "Art. 219, VI"
    },
    "VII - Agressão física ou moral": {
        "tipo": "agressao",
        "agravantes_possiveis": ["violencia_ou_ameaca_grave", "reincidencia_grave"],
        "descricao_detalhada": "Agressão física ou moral a qualquer membro da comunidade universitária",
        "artigo_base": "Art. 219, VII"
    },
    "VIII - Infração considerada ilícito penal": {
        "tipo": "ilicito_penal",
        "agravantes_possiveis": ["reincidencia", "violencia_ou_ameaca_grave"],
        "descricao_detalhada": "Prática de atos definidos como infração pelas leis penais, salvo quando cobertos por causa excludente de ilicitude, ou de atos incompatíveis com a dignidade e o decoro da vida universitária",
        "artigo_base": "Art. 219, VIII"
    }
}

AGRAVANTES = {
    "reincidencia": {
        "nome": "Reincidência",
        "artigo": "Art. 219 §3º",
        "descricao": "Reincidência na mesma falta disciplinar"
    },
    "reincidencia_grave": {
        "nome": "Reincidência em falta grave",
        "artigo": "Art. 219 §5º",
        "descricao": "Reincidência em agressão física ou moral"
    },
    "violencia_ou_ameaca_grave": {
        "nome": "Violência ou grave ameaça",
        "artigo": "Art. 221, I",
        "descricao": "Cometimento de infração mediante violência ou grave ameaça, com emprego de arma ou com substância inflamável, explosiva ou intoxicante"
    }
}

PENALIDADES = {
    "advertencia": {
        "nome": "Advertência",
        "artigo": "Art. 216, I",
        "descricao": "Penalidade aplicada para infrações de menor gravidade (itens I a VI do Art. 219)",
        "gravidade": 1
    },
    "advertencia_com_indenizacao": {
        "nome": "Advertência com Indenização",
        "artigo": "Art. 216, I e Art. 219 § 2º",
        "descricao": "Penalidade aplicada para danos ao patrimônio, obrigando o discente a indenizar o dano causado",
        "gravidade": 1
    },
    "advertencia_com_prejuizo_nota": {
        "nome": "Advertência com Prejuízo de Nota",
        "artigo": "Art. 216, I e Art. 219 § 1º",
        "descricao": "Penalidade aplicada para improbidade acadêmica, ficando prejudicada a nota ou conceito para fins didáticos",
        "gravidade": 1
    },
    "suspensao_leve": {
        "nome": "Suspensão (3 a 15 dias)",
        "artigo": "Art. 216, II e Art. 219 § 3º",
        "descricao": "Penalidade aplicada para reincidência em infrações leves (itens I a VI)",
        "gravidade": 2
    },
    "suspensao_grave": {
        "nome": "Suspensão (16 a 90 dias)",
        "artigo": "Art. 216, II e Art. 219 § 4º",
        "descricao": "Penalidade aplicada para infrações com agravante.",
        "gravidade": 3
    },
    "desligamento": {
        "nome": "Desligamento",
        "artigo": "Art. 216, III",
        "descricao": "Penalidade aplicada para infrações graves com agravantes ou reincidência em infrações graves",
        "gravidade": 4
    },
    "penalidade_alternativa": {
        "nome": "Impossibilidade de concorrer a bolsas",
        "artigo": "Art. 217",
        "descricao": "Penalidade alternativa que pode ser aplicada isolada ou cumulativamente pelo período de 1 ano",
        "gravidade": 0
    }
}

ARTIGOS_REGIMENTO = {
    "Art. 215": "As faltas disciplinares dos discentes da UFAPE serão apuradas mediante processo administrativo disciplinar discente.",
    "Art. 216": "As penalidades disciplinares abrangem: I - advertência; II - suspensão; III - desligamento.",
    "Art. 217": "A depender da gravidade da falta, poderão ser aplicadas, isolada ou cumulativamente, a penalidade alternativa de impossibilidade de concorrer a bolsas acadêmicas, exceto os benefícios e serviços de assistência estudantil, pelo período de 1 (um) ano.",
    "Art. 219": "Incorrerão nas penas descritas neste Regimento discentes que cometerem as seguintes faltas: [lista de infrações I a VIII]",
    "Art. 219 §1º": "Fica prejudicada a nota ou conceito, para fins didáticos, no caso do inciso I deste artigo.",
    "Art. 219 §2º": "Para as faltas configuradas no inciso V, a pena de advertência será cumulada com a indenização pelo dano causado, com base na exigível avaliação, sem prejuízo de aplicação de outras sanções cabíveis.",
    "Art. 219 §3º": "A reincidência nas faltas configuradas nos itens I a VI importa na pena de suspensão de 03 (três) a 15 (quinze) dias.",
    "Art. 219 §4º": "As infrações especificadas nos incisos VII e VIII acarretarão a suspensão de 16 (dezesseis) a 90 (noventa) dias, salvo se a infração for considerada de maior gravidade, quando poderá ser aplicada a penalidade de desligamento em consonância ao disposto no art. 268.",
    "Art. 219 §5º": "A reincidência nas faltas enumeradas no inciso VII acarretará a pena de desligamento, assim como a infração especificada no item VIII, na hipótese de infração que incompatibilize o discente com a vida universitária.",
    "Art. 220": "Na aplicação das penas disciplinares serão levados em consideração a natureza e a gravidade da infração cometida, os antecedentes do discente, bem como as circunstâncias atenuantes ou agravantes, dolo ou culpa, valor e utilidade dos bens atingidos.",
    "Art. 221": "São circunstâncias agravantes: I - cometimento de infração mediante violência ou grave ameaça, com emprego de arma ou com substância inflamável, explosiva ou intoxicante; II - cometimento de infração por discente que se utiliza de falsificação de documento público, pessoal ou acadêmico, para obter vantagem para si ou para outrem.",
    "Art. 222": "As sanções aplicadas a membros do corpo discente não constarão em seu histórico escolar, fazendo-se apenas o registro em assentamentos pessoais.",
    "Art. 223": "A combinação das penas de advertência, suspensão e desligamento compete ao Reitor."
}