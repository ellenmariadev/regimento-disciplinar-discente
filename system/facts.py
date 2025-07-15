from experta import Fact, Field

class Conduta(Fact):
    tipo = Field(str, mandatory=True)
    artigo = Field(str, mandatory=True)

class Agravante(Fact):
    tipo = Field(str, mandatory=True)
    artigo = Field(str, mandatory=True)

class Penalidade(Fact):
    tipo = Field(str, mandatory=True)
    gravidade = Field(int, mandatory=True)