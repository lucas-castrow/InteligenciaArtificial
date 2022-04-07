def retorna_h(destino, node):
    def h(n):
        def caminhar(pos, visitados, distancia):
            caminhos = node[pos]
            distancias = []
            visitados.add(pos)
            if pos == destino:
                return distancia
            distancia += 1
            for novo_pos in caminhos:
                if novo_pos == destino:
                    return distancia
                if not novo_pos in visitados:
                    try:
                        distancias.append(caminhar(novo_pos, set(visitados), distancia))
                    except:
                        pass
            return min(distancias)

        try:
            return caminhar(n, set(), 0)
        except:
            return None

    return h

def busca_melhor_caminho2(destino, node, meu_h):
    def meu_f(n):
        def calculo_f(pos, g_anterior):
            valor = meu_h(pos)
            if not valor:
                raise Exception('Não há caminho para determinado destino')
            return g_anterior + valor
        pos = n
        g = 0
        path = [pos]
        try:
            while True:
                menor = 999999
                idx_menor = -1
                _caminhos = node[pos]
                for caminho in _caminhos:
                    if caminho == destino:
                        path.append(caminho)
                        # break # >>>>>> bug
                        return path  # >>>> bug fix
                    if caminho in path:
                        continue
                    heuristica = calculo_f(caminho, g + 1)
                    if heuristica < menor:
                        menor = heuristica
                        idx_menor = caminho
                if idx_menor != -1:
                    pos = idx_menor
                    path.append(idx_menor)
                    g += 1
                    continue
                else:
                    break
        except:
            return []
        return path
    return meu_f


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

    def busca_geral(self, meu_h):
        no = Nó(self.estado_inicial, 0)
        nos = [no]
        self.todas_acoes(estado_inicial)
        for acao in self.retorna_acoes(no.estado):
            if len(nos) == 0:
                return "Falha"
            no = nos.pop(0)
            if teste_objetivo == no.estado:
                return no
            filho = no.gera_filho(acao)
            nos.append(filho)


    def busca_melhor_primeiro(self, meu_h):
        return self.busca_geral(meu_h)

    def busca_estrela(self):
        no = Nó(self.estado_inicial, 0)
        meu_h = retorna_h(self.teste_objetivo, no)
        busca_melhor_caminho2(self.teste_objetivo, no, meu_h)

    def busca_gulosa(self):
        no = Nó(self.estado_inicial, 0)
        meu_h = retorna_h(self.teste_objetivo, no)
        return self.busca_melhor_primeiro(meu_h)
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
