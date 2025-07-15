from experta import Rule, OR, AND, NOT
from .facts import Conduta, Agravante, Penalidade
from .knowledge_base import PENALIDADES

class DisciplinaryRules:    
    @Rule(
        Conduta(tipo="improbidade_academica"),
        NOT(Agravante(tipo="reincidencia")),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")),
        salience=50 
    )
    def regra_improbidade_academica_base(self):
        self.penalidades.append(PENALIDADES["advertencia_com_prejuizo_nota"])
        self.artigos_aplicados.append("Art. 219, I")
        self.artigos_aplicados.append("Art. 219 §1º")
        
        explanation = "Foi aplicada a penalidade de advertência devido à improbidade na execução dos trabalhos acadêmicos, conforme Art. 219, I. Além disso, fica prejudicada a nota ou conceito para fins didáticos (Art. 219 §1º)."
        self.add_explanation(explanation, "regra_improbidade_academica_base")
        self.declare(Penalidade(tipo="advertencia", gravidade=1))

    @Rule(
        Conduta(tipo="dano_patrimonio"),
        NOT(Agravante(tipo="reincidencia")),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")),
        salience=50
    )
    def regra_dano_patrimonio_base(self):
        self.penalidades.append(PENALIDADES["advertencia_com_indenizacao"])
        self.artigos_aplicados.append("Art. 219, V")
        self.artigos_aplicados.append("Art. 219 §2º")
        
        explanation = "Foi aplicada a penalidade de advertência cumulada com indenização pelo dano causado, conforme Art. 219, V e §2º."
        self.add_explanation(explanation, "regra_dano_patrimonio_base")
        self.declare(Penalidade(tipo="advertencia", gravidade=1))
    
    @Rule(
        OR(
            Conduta(tipo="informacao_falsa"),
            Conduta(tipo="inutilizacao_documentos"),
            Conduta(tipo="retirada_sem_permissao"),
            Conduta(tipo="perturbacao")
        ),
        NOT(Agravante(tipo="reincidencia")),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")),
        salience=50
    )
    def regra_infracoes_leves_base(self):
        self.penalidades.append(PENALIDADES["advertencia"])
        self.artigos_aplicados.append("Art. 219")
        
        explanation = "Foi aplicada a penalidade de advertência devido à infração considerada leve, conforme Art. 219 (incisos II, III, IV ou VI)."
        self.add_explanation(explanation, "regra_infracoes_leves_base")
        self.declare(Penalidade(tipo="advertencia", gravidade=1))
    
    @Rule(
        OR(
            Conduta(tipo="agressao"),
            Conduta(tipo="ilicito_penal")
        ),
        NOT(Agravante(tipo="reincidencia")),
        NOT(Agravante(tipo="reincidencia_grave")),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")),
        salience=50
    )
    def regra_infracoes_graves_base(self):
        self.penalidades.append(PENALIDADES["suspensao_grave"])
        self.artigos_aplicados.append("Art. 219 §4º")
        
        explanation = "Foi aplicada a penalidade de suspensão de 16 a 90 dias devido à infração considerada grave, conforme Art. 219 (incisos VII ou VIII) e §4º."
        self.add_explanation(explanation, "regra_infracoes_graves_base")
        self.declare(Penalidade(tipo="suspensao", gravidade=3))
    
    @Rule(
        Agravante(tipo="violencia_ou_ameaca_grave"),
        salience=200 
    )
    def regra_violencia_desligamento(self):
        self.penalidades.append(PENALIDADES["desligamento"])
        self.artigos_aplicados.append("Art. 221, I")
        self.artigos_aplicados.append("Art. 220")
        
        explanation = ("Foi aplicada a penalidade de desligamento devido à circunstância "
                      "agravante de violência ou grave ameaça, conforme Art. 221, I. "
                      "Este agravante, considerado de extrema gravidade segundo o Art. 220, "
                      "justifica a aplicação da penalidade máxima independentemente da infração original.")
        
        self.add_explanation(explanation, "regra_violencia_desligamento")
        self.declare(Penalidade(tipo="desligamento", gravidade=4))
    
    @Rule(
        AND(
            OR(
                Conduta(tipo="improbidade_academica"),
                Conduta(tipo="informacao_falsa"),
                Conduta(tipo="inutilizacao_documentos"),
                Conduta(tipo="retirada_sem_permissao"),
                Conduta(tipo="dano_patrimonio"),
                Conduta(tipo="perturbacao")
            ),
            Agravante(tipo="reincidencia")
        ),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")),  
        salience=150
    )
    def regra_reincidencia_leve(self):
        self.penalidades.append(PENALIDADES["suspensao_leve"])
        self.artigos_aplicados.append("Art. 219 §3º")
        
        explanation = "Foi aplicada a penalidade de suspensão de 3 a 15 dias devido à reincidência em infração considerada leve, conforme Art. 219 §3º."
        self.add_explanation(explanation, "regra_reincidencia_leve")
        self.declare(Penalidade(tipo="suspensao", gravidade=2))
    
    @Rule(
        AND(
            OR(
                Conduta(tipo="agressao"),
                Conduta(tipo="ilicito_penal")
            ),
            Agravante(tipo="reincidencia")
        ),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")),
        NOT(Agravante(tipo="reincidencia_grave")),  
        salience=150
    )
    def regra_reincidencia_grave(self):
        self.penalidades.append(PENALIDADES["desligamento"])
        self.artigos_aplicados.append("Art. 219 §5º")
        
        explanation = "Foi aplicada a penalidade de desligamento devido à reincidência em infração grave, conforme interpretação do Art. 219 §5º."
        self.add_explanation(explanation, "regra_reincidencia_grave")
        self.declare(Penalidade(tipo="desligamento", gravidade=4))
    
    @Rule(
        AND(
            Conduta(tipo="agressao"),
            Agravante(tipo="reincidencia_grave")
        ),
        NOT(Agravante(tipo="violencia_ou_ameaca_grave")), 
        salience=175
    )
    def regra_reincidencia_agressao(self):
        self.penalidades.append(PENALIDADES["desligamento"])
        self.artigos_aplicados.append("Art. 219 §5º")
        
        explanation = "Foi aplicada a penalidade de desligamento devido à reincidência específica em agressão física ou moral, conforme Art. 219 §5º."
        self.add_explanation(explanation, "regra_reincidencia_agressao")
        self.declare(Penalidade(tipo="desligamento", gravidade=4))
    
    @Rule(
        OR(
            Penalidade(tipo="suspensao"),
            Penalidade(tipo="desligamento")
        ),
        salience=0
    )
    def regra_penalidade_alternativa(self):
        if all(p['nome'] != PENALIDADES["penalidade_alternativa"]['nome'] for p in self.penalidades):
            self.penalidades.append(PENALIDADES["penalidade_alternativa"])
            self.artigos_aplicados.append("Art. 217")
            
            explanation = "Foi adicionada a penalidade alternativa de impossibilidade de concorrer a bolsas acadêmicas pelo período de 1 ano, conforme Art. 217."
            self.add_explanation(explanation, "regra_penalidade_alternativa")