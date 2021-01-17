import tkinter as tk
from tkinter.ttk import Treeview
import pandas as pd

# Construções de classes
class Elemento():
    '''
    Classe pai de cada elemento na tela.
    Todas as outras classes de elementos vão herdar o método construtor dessa classe
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, visivel=True):
        '''
        Método construtor.
        :param master: nome do frame master que vai conter cada instância criada
        :param altura: altura em pixels, espera-se um inteiro
        :param largura: largura em pixels, espera-se um inteiro
        :param pos_x: posição no eixo x em pixels, espera-se um inteiro
        :param pos_y: posição no eixo y em pixels, espera-se um inteiro
        :param visivel: definido True por padrão, quando a instância ficar invisível, espera-se False
        '''
        self.master = master
        self.altura = altura
        self.largura = largura
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.visivel = visivel

class Botao(Elemento):
    '''
    Classe utilizada para instanciar cada botão (widget Button) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, texto, comando, ativo=True, visivel=True):
        '''
        Método construtor.
        :param texto: vai receber o texto que cada instância vai apresentar, espera-se uma string
        :param comando: vai receber o comando que cada botâo irá executar quando clicado, espera-se uma função
        :param ativo: definido como True por padrão, quando a instância ficar inativa, espera-se False
        '''
        self.texto = texto
        self.comando = comando
        self.ativo = ativo
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)

class Texto(Elemento):
    '''
    Classe utilizada para instanciar cada texto (widget Label) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y,
                 texto, negrito=False, italico=False, sublinhado=False, tam_fonte=12, visivel=True):
        '''
        Método construtor
        :param texto: vai receber o texto que cada instância vai apresentar, espera-se uma string
        :param negrito: Define se o texto será negrito, por padrão False
        :param italico: Define se o texto será itálico, por padrão False
        :param sublinhado: Define se o texto será sublinhado, por padrão False
        :param tam_fonte: Define o tamanho da fonte, definido como 12 por padrão. Espera-se um inteiro
        '''
        self.texto = texto
        self.negrito = negrito
        self.italico = italico
        self.sublinhado = sublinhado
        self.tam_fonte = tam_fonte
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)

class LabelFrame(Elemento):
    '''
    Classe utilizada para instanciar cada label frame (widget LabelFrame) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, rotulo=None, visivel=True):
        '''
        Método construtor
        :param rótulo: Rótulo que cada instância vai apresentar, recebe None (sem rótulo) por padrão
        '''
        self.rotulo = rotulo
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)

class Treeview(Elemento):
    '''
    Classe utilizada para instanciar cada tabela (widget Treeview) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, data_frame=None, visivel=True):
        '''
        Método construtor
        :param data_frame: recebe om objeto do tipo DataFrame, oriundo da biblioteca pandas,
                           recebe None (vazio) por padrão
        '''
        self.data_frame = data_frame
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)

class BarraDeMenus(Elemento):
    '''
    Classe utilizada para instanciar cada barra de menu (widget Menu) da aplicação
    !ATENÇÃO! Utilizar somente para instanciar barras de menu, nunca menus cascata!
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, lista_menus, visivel=True):
        '''
        Método construtor
        :param lista_menus: espera-se um dicionário , onde as chaves serão os rótulos de cada menu,
                            e os valores serão objetos do tipo menu (widget Menu)
        '''
        self.lista_menus = lista_menus
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)

class MenuCascata(Elemento):
    '''
    Classe utilizada para instanciar cada menu cascata (widget Menu) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, lista_submenus, visivel=True):
        '''
        Método construtor
        :param lista_elementos: espera-se um dicionário , onde as chaves serão os rótulos de cada submenu,
                                e os valores serão os comandos de cada submenu (espera-se um método)
        '''
        self.lista_submenus = lista_submenus
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)

class BoxDeMensagem(Elemento):
    '''
    Classe utilizada para instanciar cada box de mensagem (widget messagebox) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, tipo, titulo, texto, visivel=True):
        '''
        Método construtor
        :param tipo: recebe o tipo do box de mensagem. Pode ser 'I' (informação), 'A' (atenção),
                     'E' (erro), 'OC' (ok/cancela), 'TC' (tentar novamente/cancela),
                     'SN' (sim/não), 'SNC' (sim/nãocancela).
                     Qualquer valor além desses vai retornar um erro no momento da renderização em tela.
                     Espera-se uma string.
        :param titulo: Título do box de mensagem
        :param texto: Texto/pergunta do box de mensagem
        '''
        self.tipo = tipo
        self.titulo = titulo
        self.texto = texto
        super().__init__(master, altura, largura, pos_x, pos_y, visivel)
