import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class Conexoes(object):
    """
    Classe a ser instanciada para criar o dataframe a ser usado na geração da rede.
    """
    
    def __init__(self):
        """
        Cria novo dataframe.
        """
        self.conexoes = pd.DataFrame(columns=['usuario_1', 'usuario_2'])        

    def cadastrar_usuario(self, nome):
        """
        Metodo usado para cadastrar novo usuario.        
        Parâmetros
        __________
        nome: str
            Nome a ser cadastrado.              
        """        
        novo_cadastro = {'usuario_1': nome, 'usuario_2': ""}
        self.conexoes['usuario_1'] = [nome]
    
    def criar_conexao(self, usuario, amigo):       
        """
        Metodo usado para criar nova conexão.        
        Parâmetros
        __________
        usuario: str
            Nome do usuario.  
        amigo: str
            Nome de amigo.        
        """        
        nova_conexao = {'usuario_1': usuario, 'usuario_2': amigo}
        self.conexoes = pd.concat([self.conexoes, pd.DataFrame(nova_conexao, index=[1])]).reset_index(drop=True)
            
    def cadastrar_usuario_e_conexoes(self, nome: str, amigos: list):
        """
        Metodo usado para cadastrar novo usuario com conexões.        
        Parâmetros
        __________
        nome: str
            Nome a ser cadastrado.        
        amigos: list
            Nomes das pessoas a serem cadastradas como amigos.        
        """    
        output = []          
        for pessoa in amigos:
            if pessoa in list(set(list(self.conexoes['usuario_1'])+list(self.conexoes['usuario_2']))):
                nova_conexao = {'usuario_1': nome, 'usuario_2': pessoa}
                self.conexoes = pd.concat([self.conexoes, pd.DataFrame(nova_conexao, index=[1])]).reset_index(drop=True)                
                msg= (f'A conexão "{nome} -> {pessoa}" foi cadastrada com sucesso! \n')
                output.append(msg)
            else:
                msg=(f'{pessoa} não faz parte da rede. \n')
                output.append(msg)
        return output

    def frame(self):
        """
        Metodo usado para retornar o dataframe.        
        """          
        return self.conexoes

def mostrar_total_vertices(conexoes: Conexoes) -> list:
    """
    Retorna todos os nomes da rede (vértices).    
    Parâmetros
    __________
    conexoes: objeto da classe Conexoes.    
    """
    graph=nx.from_pandas_edgelist(conexoes.frame(), 'usuario_1', 'usuario_2', create_using=nx.Graph())
    return list(graph)

def mostrar_amigos(conexoes: Conexoes, node: str) -> list:
    """
    Retorna os nomes dos amigos (vértices) - Nível 1.    
    Parâmetros
    __________
    conexoes: objeto da classe Conexoes.
    node: str
        Nome a ser analisado (vértice).
    """    
    graph=nx.from_pandas_edgelist(conexoes.frame(), 'usuario_1', 'usuario_2', create_using=nx.Graph())
    try:
        return [n for n in graph.neighbors(node)]
    except:
        print(f'{node} não faz parte da rede')

def mostrar_amigos_de_amigos(conexoes: Conexoes, node: str) -> list:
    """
    Retorna os nomes dos amigos de vértices amigos - Nível 2.
    Parâmetros
    __________
    conexoes: objeto da classe Conexoes.
    node: str
        Nome a ser analisado (vértice).
    """ 
    graph=nx.from_pandas_edgelist(conexoes.frame(), 'usuario_1', 'usuario_2', create_using=nx.Graph())
    try:
        amigos = [n for n in graph.neighbors(node)]
        resultado = [mostrar_amigos(conexoes, amigo) for amigo in amigos] # Cria lista de sublistas
        resultado = list(set([amigo for sublist in resultado for amigo in sublist])) # Convierte as sublistas em uma lista e elimina os nomes repetidos
        resultado = [amigo for amigo in resultado if amigo not in amigos] # Mostra os nomes que não são amigos diretos
        resultado.remove(node)    
        return resultado
    except: 
        print(f'{node} não faz parte da rede')

def mostrar_grafo(conexoes: Conexoes):
    """
    Retorna o grafo disponibilizado.    
    Parâmetros
    __________
    conexoes: objeto da classe Conexoes.   
    """
    graph=nx.from_pandas_edgelist(conexoes.frame(), 'usuario_1', 'usuario_2', create_using=nx.Graph())
    pos = nx.circular_layout(graph)
    labels = {x:'knows' for x in list(zip(conexoes.frame()['usuario_1'], conexoes.frame()['usuario_2']))}
    fig = plt.figure()
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=7, verticalalignment='baseline', label_pos=0.5)
    nx.draw(graph, with_labels=True, pos= pos, node_color='skyblue', node_size=2000, edgecolors='#0083ca', edge_color='black') 
    return fig