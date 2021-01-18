import tkinter as tk
from tkinter import ttk
import pandas as pd

# Construções de classes
class Elemento():
    '''
    Classe pai de cada elemento na tela.
    Todas as outras classes de elementos vão herdar o método construtor dessa classe
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y):
        '''
        Método construtor.
        :param master: nome do frame master que vai conter cada instância criada
        :param altura: altura em pixels (unidades de texto para alguns elementos), espera-se um inteiro
        :param largura: largura em pixels, espera-se um inteiro
        :param pos_x: posição no eixo x em pixels, espera-se um inteiro
        :param pos_y: posição no eixo y em pixels, espera-se um inteiro
        '''
        self.master = master
        self.altura = altura
        self.largura = largura
        self.pos_x = pos_x
        self.pos_y = pos_y

class Botao(Elemento):
    '''
    Classe utilizada para instanciar cada botão (widget Button) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, texto, comando, imagem=False, ativo=True):
        '''
        Método construtor.
        :param texto: vai receber o texto que cada instância vai apresentar, espera-se uma string
        :param comando: vai receber o comando que cada botâo irá executar quando clicado, espera-se uma função
        :param imagem: vai receber uma imagem para o botão. False por padrão. Espera-se um widget PhotoImage.
        :param ativo: definido como True por padrão, quando a instância ficar inativa, espera-se False
        '''
        self.texto = texto
        self.comando = comando
        self.imagem = imagem
        self.ativo = ativo
        super().__init__(master, altura, largura, pos_x, pos_y)
        # Cria o widget de acordo com os atributos texto e imagem
        if self.imagem and self.texto: # Quando for passado texto e imagem
            self.widget = tk.Button(master = self.master,
                              height = self.altura,
                              width = self.largura,
                              takefocus = True,
                              compound = 'left',
                              text = self.texto,
                              image = self.imagem,
                              state = 'normal' if self.ativo else 'disabled',
                              command = lambda: self.comando())
        elif self.imagem and (self.texto == False): # Quando for passado apenas imagem
            self.widget = tk.Button(master = self.master,
                              height = self.altura,
                              width = self.largura,
                              takefocus = True,
                              state = 'normal' if self.ativo else 'disabled',
                              image = self.imagem,
                              command = lambda: self.comando())
        elif (self.imagem == False) and self.texto: # Quando for passado apenas texto
            self.widget = tk.Button(master = self.master,
                              height = self.altura,
                              width = self.largura,
                              takefocus = True,
                              text = self.texto,
                              state = 'normal' if self.ativo else 'disabled',
                              command = lambda: self.comando())
        else: self.widget = None # Quando não for passado texto nem imagem, vai gerar um erro na renderização

    def renderizar(self):
        '''
        Renderiza o elemento na tela de acordo com seus atributos
        :return: None
        '''
        if self.widget:
            self.widget.place(x=self.pos_x, y=self.pos_y)
            return None
        else:
            raise AttributeError('Nenhum texto e nenhuma imagem foram passados para o botão')

class Texto(Elemento):
    '''
    Classe utilizada para instanciar cada texto (widget Label) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y,
                 texto, tam_fonte=12):
        '''
        Método construtor
        :param texto: vai receber o texto que cada instância vai apresentar, espera-se uma string
        :param tam_fonte: Define o tamanho da fonte, definido como 12 por padrão. Espera-se um inteiro
        '''
        self.texto = texto
        self.tam_fonte = tam_fonte
        super().__init__(master, altura, largura, pos_x, pos_y)
        self.widget = tk.Label(master = self.master,
                         height = self.altura,
                         width = self.largura,
                         text = self.texto)


    def renderizar(self):
        '''
        Renderiza o elemento na tela de acordo com seus atributos
        :return: None
        '''
        self.widget.place(x=self.pos_x, y=self.pos_y)
        return None


class LabelFrame(Elemento):
    '''
    Classe utilizada para instanciar cada label frame (widget LabelFrame) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, rotulo=None):
        '''
        Método construtor
        :param rótulo: Rótulo que cada instância vai apresentar, recebe None (sem rótulo) por padrão
        '''
        self.rotulo = rotulo
        super().__init__(master, altura, largura, pos_x, pos_y)
        self.widget = tk.LabelFrame(master=self.master,
                                   height=self.altura,
                                   width=self.largura,
                                   text=self.rotulo)
        self.widget.pack_propagate(False) # Define que o tamanho da LabelFrame não irá se moldar aos seus elementos

    def renderizar(self):
        '''
        Renderiza o elemento na tela de acordo com seus atributos
        :return: None
        '''
        self.widget.place(x=self.pos_x, y=self.pos_y)
        return None

class Tabela(Elemento):
    '''
    Classe utilizada para instanciar cada tabela (widget Treeview) da aplicação.
    Para melhor organização, usar um FrameLabel como master.
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y):
        '''
        Método construtor
        '''
        super().__init__(master, altura, largura, pos_x, pos_y)
        self.widget = ttk.Treeview(master=self.master)

    def renderizar(self):
        '''
        Renderiza o elemento na tela de acordo com seus atributos
        :return: None
        '''
        self.widget.place(relheight=self.altura, relwidth=self.largura)
        # Insere as barras de rolagem na tabela
        treescrollx = tk.Scrollbar(self.master, orient='horizontal', command=self.widget.xview)
        treescrolly = tk.Scrollbar(self.master, orient='vertical', command=self.widget.yview)
        self.widget.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side='bottom', fill='x')
        treescrolly.pack(side='right', fill='y')
        return None

    def renderizar_tabela(self, data_frame):
        '''
        Renderiza a tabela dentro da instância (Treeview).
        :param data_frame: deve ser um dataframe (objeto da biblioteca pandas)
        :return: None
        '''
        self.widget.delete(*self.widget.get_children()) # limpa todos os dados pre-existentes na tabela
        self.widget['columns'] = list(data_frame.columns)
        self.widget['show'] = 'headings'
        for coluna in self.widget['columns']:
            self.widget.heading(coluna, text=coluna)
        linhas = data_frame.to_numpy().tolist()
        for linha in linhas:
            self.widget.insert('', 'end', values=linha)
        return None


class BarraDeMenus(Elemento):
    '''
    Classe utilizada para instanciar cada barra de menu (widget Menu) da aplicação
    !ATENÇÃO! Utilizar somente para instanciar barras de menu, nunca menus cascata!
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, *lista_menus):
        '''
        Método construtor
        :param lista_menus: esperam-se listas de tuplas (tantas quantas forem as cascatas),
                            onde os primeiros elementos de cada tupla serão os rótulos de cada menu,
                            e os segundos elementos de cada tupla serão objetos do tipo menu (widget Menu)
        '''
        self.lista_menus = (*lista_menus,)
        super().__init__(master, altura, largura, pos_x, pos_y)
        self.widget = tk.Menu(master=self.master)

    def renderizar(self):
        '''
        Renderiza o elemento na tela de acordo com seus atributos
        :return: None
        '''
        # Adiciona cada elemento ao menu, caso a tupla da lista seja (False, False, False), adiciona um separador
        for menu_cascata in self.lista_menus: # Laço que percorre cada menu cascata da lista_menus
            for tupla in menu_cascata: # Laço que percorre cada tupla de parâmetros de cada menu cascata
                if tupla:
                    self.widget.add_command(label=item[0],comand=lambda: item[1]())
                if tupla == (False, False, False):
                    self.widget.add_separator()
        # Renderiza o menu
        self.widget.place(x=self.pos_x, y=self.pos_y, height=self.altura, width=self.largura)
        return None

class MenuCascata(Elemento):
    '''
    Classe utilizada para instanciar cada menu cascata (widget Menu) da aplicação
    !Atenção! Essa classe não tem método renderizar,
    pois seus elementos serão renderizados no método renderizar da classe BarraDeMenus
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, lista_submenus):
        '''
        Método construtor
        :param lista_elementos: espera-se uma lista de tuplas , onde os primeiros elementos de cada tupla
                                serão os rótulos de cada submenu, os segundos elementos de cada tupla
                                serão os comandos de cada submenu (espera-se um método)
                                e os terceiros elementos serão os ícones de cada submenu.
                                Caso não se utilize ícone, definir o terceiro elemento da tupla como None.
                                Em caso de separadores, utilizar (False, False, False) na tupla correspondente
        '''
        self.lista_submenus = lista_submenus
        super().__init__(master, altura, largura, pos_x, pos_y)

class BoxDeMensagem(Elemento):
    '''
    Classe utilizada para instanciar cada box de mensagem (widget messagebox) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, tipo, titulo, texto):
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
        super().__init__(master, altura, largura, pos_x, pos_y)

class Imagem(Elemento):
    '''
    Classe utilizada para instanciar imagens (widget PhotoImage) da aplicação
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, caminho):
        '''
        Método construtor
        :param caminho:
        '''
        self.caminho = caminho
        super().__init__(master, altura, largura, pos_x, pos_y)

'''janela = tk.Tk()
janela.geometry('600x600')
lista = []
for i in range(3):
    lista.append(Botao(janela, 2, 20, 50 + 10*(i + 1) + i*150, 40, f'Botão {i + 1}', janela.quit))

for i in range(3):
    lista.append(Texto(janela, 2, 20, 50 + 10*(i + 1) + i*150, 100, f'Texto {i + 1}'))
label1 = LabelFrame(janela, 300, 550, 25, 150, 'Sou lindo!')
lista.append(label1)
tabela = Tabela(label1.widget, 1, 1, 0, 0)
lista.append(tabela)

for elemento in lista: elemento.renderizar()

df = pd.read_csv('titanic.csv')
tabela.renderizar_tabela(df)

janela.mainloop()
'''
