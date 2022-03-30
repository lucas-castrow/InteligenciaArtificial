def DLS_recursivo(no, problema, limite):
    if problema.teste_objetivo == no.estado:
        return no
    elif limite == 0:
        return "corte"
    else:
        ocorreu_corte = False
        for acao in problema.retorna_acoes(no.estado):
            filho = no.filho
            resultado = problema.DLS_recursivo(filho, problema, limite - 1)
            if resultado == "corte":
                ocorreu_corte = True
            elif resultado != "falha":
                return resultado
        if ocorreu_corte:
            return "corte"
        else:
            return 'falha'

class Nó:

    def __init__(self, estado, custo):
        self.estado = estado
        self.no_pai = None
        self.operador = 0
        self.profundidade = 0
        self.custo = custo

    def adiciona_filho(self, filho):
        self.filho = filho

class Problema:

    def __init__(self, estado_inicial, teste_objetivo):
        self.estado_inicial = estado_inicial
        self.teste_objetivo = teste_objetivo
        self.acoes = {}

    #retornar uma lista de acoes de acordo com o estado.
    # ex {"vazio": [0,2,3,4,5]} CASAS VAZIAS

    def retorna_acoes(self, estado):
        return self.acoes[estado]

    def busca_em_largura(self):
        no = Nó(self.estado_inicial, 0)
        if self.teste_objetivo == no:
            return "SOLUCAO"

        fronteira = [no]
        explorados = []

        while True:
            if len(fronteira) == 0:
                return 'FALHA'
            no = fronteira.pop()
            explorados.append(no.estado)
            for acao in self.acoes:
                filho = no.filho
                if filho.estado not in explorados or filho not in fronteira:
                    if self.teste_objetivo == filho.estado:
                        return filho
                    fronteira.append(filho)

    def busca_custo_uniforme(self):
        no = Nó(self.estado_inicial, 0)
        fronteira = [no]
        explorados = []
        while True:
            if len(fronteira) == 0:
                return 'FALHA'
            fronteira.sort(key=lambda x: x.name)
            no = fronteira.pop()
            explorados.append(no.estado)
            for acao in self.retorna_acoes(no.estado):
                filho = no.filho

                if filho.estado not in explorados or filho not in fronteira:
                    fronteira.append(filho)
                    fronteira.sort(key=lambda x: x.name)
                elif filho in fronteira and fronteira[0] == filho:
                    no = filho


