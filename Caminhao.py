class Caminhao:
    def __init__(self, bairro):
        self.bairro = bairro
        self.num_funcionarios = 0
        self.capacidade_total = 100
        self.capacidade_restante = 100
        self.ponto_atual = 0
        self.tempo_gasto = 0


    def coletar_lixo(self):
        if self.capacidade_restante >= self.ponto_atual.quantidade_lixo: 
            tempo = self.ponto_atual.quantidade_lixo / self.num_funcionarios
            self.capacidade_restante -= self.ponto_atual.quantidade_lixo
            self.ponto_atual.quantidade_lixo = 0
        else:
            tempo = self.capacidade_restante / self.num_funcionarios
            self.capacidade_restante = 0
            self.ponto_atual.quantidade_lixo -= self.capacidade_restante
        if self.ponto_atual.lixo_espalhado:
            tempo *= 2
        self.tempo_gasto += tempo
        

    def retornar_ao_centro(self):
        self.capacidade_restante = self.capacidade_total


    def sessao_de_coleta(self):
        while self.capacidade_restante > 0 and self.bairro.tem_pontos_sujos:
            self.proximo_ponto_de_coleta()
            self.coletar_lixo()
        self.retornar()


    def proximo_ponto_de_coleta(self):
        pontos_sujos = []
        for ponto in self.bairro:
            if ponto.quantidade_lixo > 0:
                pontos_sujos.append(ponto)

        min_caminho = djikstra(self.ponto_atual, pontos_sujos[0])
        ponto_mais_proximo = pontos_sujos[0]
        for ponto in pontos_sujos:
            if djikstra(self.ponto_atual, ponto) < min_caminho:
                min_caminho = djikstra(self.ponto_atual, ponto)
                ponto_mais_proximo = ponto

        self.ponto_atual = ponto_mais_proximo
        self.tempo_gasto += min_caminho

        

            


        


