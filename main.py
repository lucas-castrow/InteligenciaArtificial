


class Nó:

    def __init__(self, estado, custo):
        self.estado = estado
        self.no_pai = None
        self.operador = 0
        self.profundidade = 0
        self.custo = custo

    def gera_filho(self, acao):
        filho = Nó(self.estado, self.custo + 1)
        self.no_pai = filho
        aux_m = self.estado.copy()
        aux_0_l = []
        for indice_l, linha in enumerate(self.estado):
            if 0 in linha:
                aux_0_l = [indice_l, linha.index(0)]
                break

        aux_value = self.estado[acao[0]][acao[1]]

        aux_m[acao[0]][acao[1]] = 0
        aux_m[aux_0_l[0]][aux_0_l[1]] = aux_value

        filho.estado = aux_m

        return filho


class Problema:

    def __init__(self, estado_inicial, teste_objetivo):
        self.estado_inicial = estado_inicial
        self.teste_objetivo = teste_objetivo
        self.acoes = {}

    # retornar uma lista de acoes de acordo com o estado.
    # ex {"vazio": [0,2,3,4,5]} CASAS VAZIAS

    def retorna_acoes(self, estado):
        return self.acoes[str(estado)]

    def todas_acoes(self, estado):
        acoes = {}
        indice_l = 0
        indice_c = 0

        for indice, linha in enumerate(estado):
            if 0 in linha:
                indice_l = indice
                indice_c = linha.index(0)
                break

        lista_acoes = []
        tam_coluna = len(estado[0]) - 1

        if indice_l == len(estado) - 1:
            if indice_c == tam_coluna:
                lista_acoes.append((indice_l - 1, indice_c))
                lista_acoes.append((indice_l, indice_c - 1))
            elif indice_c == 0:
                lista_acoes.append((indice_l - 1, indice_c))
                lista_acoes.append((indice_l, indice_c + 1))

        elif indice_l == 0:
            if indice_c == 0:
                lista_acoes.append((indice_l + 1, indice_c))
                lista_acoes.append((indice_l, indice_c + 1))
            elif indice_c == 0:
                lista_acoes.append((indice_l + 1, indice_c))
                lista_acoes.append((indice_l, indice_c - 1))

        elif indice_l == 1 and indice_c == tam_coluna:
            lista_acoes.append((indice_l + 1, indice_c))
            lista_acoes.append((indice_l - 1, indice_c))
            lista_acoes.append((indice_l, indice_c - 1))
        elif indice_l == 1 and indice_c == 0:
            lista_acoes.append((indice_l + 1, indice_c))
            lista_acoes.append((indice_l - 1, indice_c))
            lista_acoes.append((indice_l, indice_c + 1))
        elif indice_l == len(estado) - 1 and indice_c == 1:
            lista_acoes.append((indice_l, indice_c + 1))
            lista_acoes.append((indice_l, indice_c - 1))
            lista_acoes.append((indice_l-1, indice_c))
        elif indice_l == 0 and indice_c == 1:
            lista_acoes.append((indice_l, indice_c + 1))
            lista_acoes.append((indice_l, indice_c - 1))
            lista_acoes.append((indice_l+1, indice_c))
        else:
            lista_acoes.append((indice_l, indice_c - 1))
            lista_acoes.append((indice_l, indice_c + 1))
            lista_acoes.append((indice_l - 1, indice_c))
            lista_acoes.append((indice_l + 1, indice_c))

        if str(estado) in acoes:
            self.acoes[str(estado)].extend(lista_acoes)
        else:
            self.acoes[str(estado)] = lista_acoes

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
            self.todas_acoes(no.estado)
            lista_aux = self.retorna_acoes(no.estado)
            for acao in lista_aux:
                filho = no.gera_filho(acao)
                print(filho.estado)

                if filho.estado not in explorados or filho not in fronteira:
                    if self.teste_objetivo == filho.estado:
                        return filho
                    fronteira.append(filho)

    def DLS_recursivo(self, no, limite):
        if self.teste_objetivo == no.estado:
            return no
        elif limite == 0:
            return "corte"
        else:
            ocorreu_corte = False
            self.todas_acoes(no.estado)
            lista_aux = self.retorna_acoes(no.estado)
            for acao in lista_aux:
                filho = no.gera_filho(acao)
                resultado = self.DLS_recursivo(filho, limite - 1)
                if resultado == "corte":
                    ocorreu_corte = True
                elif resultado != "falha":
                    return resultado
            if ocorreu_corte:
                return "corte"
            else:
                return 'falha'

    def busca_profundidade_limitada(self, limite):
        no = Nó(self.estado_inicial, 0)
        return self.DLS_recursivo(no, limite)

    def busca_aprofundamento_iterativo(self):
        profundidade = 0
        while True:
            self.busca_profundidade_limitada(profundidade)
            profundidade += 1

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



# estado_inicial = [[3, 1],
#                   [2, 0]]
#
# teste_objetivo = [[0, 2],
#                   [3, 1]]
estado_inicial = [[7, 2, 4],
                  [5, 0, 6],
                  [8, 3, 1]]

teste_objetivo = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
p = Problema(estado_inicial, teste_objetivo)
p.todas_acoes(estado_inicial)
x = p.busca_em_largura()
print(p.acoes)
print()
print(x.estado)
