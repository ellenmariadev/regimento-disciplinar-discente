from experta import KnowledgeEngine
from .facts import Conduta, Agravante
from .rules import DisciplinaryRules
from .knowledge_base import MAPEAMENTO_CONDUTAS, AGRAVANTES

class InfractionAnalysisEngine(KnowledgeEngine, DisciplinaryRules):    
    def __init__(self):
        super().__init__()
        self.inference_trace = []
        self.penalidades = []
        self.artigos_aplicados = []
        self.explicacao = []
    
    def declare_with_trace(self, fact, source):
        self.declare(fact)
        self.inference_trace.append({
            'type': 'fact_declared',
            'fact': str(fact),
            'source': source,
            'step': len(self.inference_trace) + 1
        })
    
    def add_explanation(self, explanation, rule_name):
        self.inference_trace.append({
            'type': 'rule_applied',
            'rule': rule_name,
            'explanation': explanation,
            'step': len(self.inference_trace) + 1
        })
        self.explicacao.append(explanation)


def analisar_conduta(conduta_selecionada, agravantes_selecionados, reincidente=False, reincidente_grave=False):
    engine = InfractionAnalysisEngine()
    engine.reset()
    
    tipo_conduta = MAPEAMENTO_CONDUTAS[conduta_selecionada]["tipo"]
    artigo_conduta = MAPEAMENTO_CONDUTAS[conduta_selecionada]["artigo_base"]
    
    engine.declare_with_trace(Conduta(tipo=tipo_conduta, artigo=artigo_conduta), "user")
    
    if reincidente:
        engine.declare_with_trace(Agravante(
            tipo="reincidencia", 
            artigo=AGRAVANTES["reincidencia"]["artigo"]
        ), "user")
    
    if reincidente_grave and tipo_conduta == "agressao":
        engine.declare_with_trace(Agravante(
            tipo="reincidencia_grave",
            artigo=AGRAVANTES["reincidencia_grave"]["artigo"]
        ), "user")
    
    for agravante in agravantes_selecionados:
        if agravante == "violencia_ou_ameaca_grave":
            engine.declare_with_trace(Agravante(
                tipo=agravante,
                artigo=AGRAVANTES[agravante]["artigo"]
            ), "user")
    
    engine.run()
    
    return {
        'penalidades': engine.penalidades,
        'artigos': engine.artigos_aplicados,
        'explicacao': engine.explicacao,
        'trace': engine.inference_trace
    }