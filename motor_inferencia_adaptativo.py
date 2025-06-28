# motor_inferencia_adaptativo.py
import json
from collections import defaultdict

from experta import MATCH, TEST, DefFacts, Fact, KnowledgeEngine, Rule


class RegraDiscente(KnowledgeEngine):
    @DefFacts()
    def _inicio(self):
        yield Fact(inicio=True)

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["improbidade", "fraude", "cola", "plágio"])))
    def advertencia_fraude(self, c):
        self.declare(Fact(
            classificacao="Infração Leve",
            penalidade="Advertência escrita",
            fundamento="Art. XX, I — Improbidade na execução dos trabalhos acadêmicos.",
            tipo_regra="advertencia",
            reincidencia=True
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["vandalismo", "quebrou", "pichou", "destruiu"])))
    def desligamento_vandalismo(self, c):
        self.declare(Fact(
            classificacao="Infração Gravíssima",
            penalidade="Desligamento da universidade",
            fundamento="Art. 193 — Vandalismo ou destruição do patrimônio público.",
            tipo_regra="desligamento",
            reincidencia=False
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["mentiu", "falsidade", "informação falsa"])))
    def advertencia_mentira(self, c):
        self.declare(Fact(
            classificacao="Infração Leve",
            penalidade="Advertência escrita",
            fundamento="Art. XX, II — Informação falsa nos processos seletivos.",
            tipo_regra="advertencia",
            reincidencia=True
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["agressão", "agrediu", "bateu", "violência"])))
    def desligamento_agressao(self, c):
        self.declare(Fact(
            classificacao="Infração Gravíssima",
            penalidade="Desligamento da universidade",
            fundamento="Art. 193 — Agressão física ou violência no ambiente acadêmico.",
            tipo_regra="desligamento",
            reincidencia=False
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["arma", "drogas", "entorpecentes", "porte ilegal"])))
    def desligamento_drogas_armas(self, c):
        self.declare(Fact(
            classificacao="Infração Gravíssima",
            penalidade="Desligamento da universidade",
            fundamento="Art. 193 — Porte de arma ou substância ilícita no ambiente acadêmico.",
            tipo_regra="desligamento",
            reincidencia=False
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["falsificação", "falsificou documento", "documento falso"])))
    def desligamento_falsificacao(self, c):
        self.declare(Fact(
            classificacao="Infração Gravíssima",
            penalidade="Desligamento da universidade",
            fundamento="Art. 193 — Falsificação de documentos oficiais.",
            tipo_regra="desligamento",
            reincidencia=False
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["perturbação", "gritaria", "bagunça contínua"])))
    def advertencia_perturbacao(self, c):
        self.declare(Fact(
            classificacao="Infração Leve",
            penalidade="Advertência escrita (suspensão se reincidente)",
            fundamento="Art. XX — Perturbação reiterada do ambiente acadêmico.",
            tipo_regra="advertencia",
            reincidencia=True
        ))

    @Rule(Fact(inicio=True), Fact(conduta=MATCH.c), TEST(lambda c: any(w in c for w in ["uso indevido", "uso irregular", "abuso de sistema"])))
    def advertencia_uso_indevido(self, c):
        self.declare(Fact(
            classificacao="Infração Leve",
            penalidade="Advertência escrita (suspensão em caso de reincidência)",
            fundamento="Art. XX — Uso indevido de recursos acadêmicos.",
            tipo_regra="advertencia",
            reincidencia=True
        ))

    @Rule(Fact(classificacao=MATCH.cls, penalidade=MATCH.pen, fundamento=MATCH.art, tipo_regra=MATCH.tp, reincidencia=MATCH.rn))
    def resultado(self, cls, pen, art, tp, rn):
        self.resultado = {
            "classificacao": cls,
            "penalidade": pen,
            "fundamento": art,
            "tipo_regra": tp,
            "reincidencia": rn
        }

class MotorInferenciaAdaptativo:
    def __init__(self, caminho_historico):
        self.historico_path = caminho_historico
        self._carregar_historico()

    def _carregar_historico(self):
        try:
            with open(self.historico_path, encoding="utf-8") as f:
                self.historico = json.load(f)
        except FileNotFoundError:
            self.historico = []

    def _salvar_historico(self):
        with open(self.historico_path, "w", encoding="utf-8") as f:
            json.dump(self.historico, f, indent=4, ensure_ascii=False)

    def inferir(self, texto_usuario):
        texto_usuario = texto_usuario.lower()
        engine = RegraDiscente()
        engine.reset()
        engine.declare(Fact(conduta=texto_usuario))
        engine.run()

        if hasattr(engine, 'resultado'):
            return engine.resultado
        else:
            return {
                "classificacao": "Conduta não identificada",
                "penalidade": "Nenhuma penalidade prevista",
                "fundamento": "Nenhuma regra foi acionada.",
                "tipo_regra": "nenhuma",
                "reincidencia": False
            }

    def registrar_feedback(self, descricao, resultado, acertou):
        self.historico.append({
            "descricao": descricao,
            "classificacao": resultado["classificacao"],
            "penalidade": resultado["penalidade"],
            "acertou": acertou,
            "tipo_regra": resultado["tipo_regra"],
            "reincidencia": resultado.get("reincidencia", False)
        })
        self._salvar_historico()

    def sugestao_melhorias(self):
        contagem = defaultdict(int)
        for entrada in self.historico:
            if not entrada["acertou"]:
                for palavra in entrada["descricao"].lower().split():
                    contagem[palavra] += 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def regras_desligamento(self):
        return [h for h in self.historico if h["tipo_regra"] == "desligamento"]