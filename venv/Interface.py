import tkinter as tk
from tkinter import ttk, messagebox
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


class Janela(tk.Tk):
    '''
    Classe utilizada para instanciar cada janela da aplicação.
    !Atenção! Suas instâncias não devem ser adicionadas na lista principal de execução do script
    '''
    def __init__(self, titulo, altura, largura, pos_x, pos_y, modo_abertura, redimensiona_x, redimensiona_y, icone):
        '''
        Método construtor
        :param titulo: Título da janela. Espera-se uma string
        :param altura: Altura da janela. Espera-se um inteiro ou uma string do tipo '500'
        :param largura: Largura da janela. Espera-se um inteiro ou uma string do tipo '500'
        :param pos_x: Posição da janela a partir da esquerda da tela. Espera-se um inteiro ou uma string do tipo '500'
        :param pos_y: Posição da janela a partir do topo da tela. Espera-se um inteiro ou uma string do tipo '500'
        :param modo_abertura: Modo de abertura. Espera-se as seguintes strings: 'normal', 'iconic' ou 'zoomed'
        :param redimensiona_x: Permite ou não o redimensionamento da largura. Espera-se True ou False
        :param redimensiona_y: Permite ou não o redimensionamento da altura. Espera-se True ou False
        :param icone: Ícone da janela. Espera-se um caminho para um arquivo do tipo .ico
        '''
        self.titulo = titulo
        self.altura = altura
        self.largura = largura
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.modo_abertura = modo_abertura
        self.redimensiona_x = redimensiona_x
        self.redimensiona_y = redimensiona_y
        self.icone = icone
        # Gera a janela e altera seus atributos
        self.widget = tk.Tk()
        self.widget.title(self.titulo)
        self.widget.geometry(str(self.largura) + 'x' + str(self.altura) + '+' + str(self.pos_x) + '+' + str(self.pos_y))
        self.widget.state(self.modo_abertura)
        self.widget.resizable(self.redimensiona_x, self.redimensiona_y)
        self.widget.iconbitmap(self.icone)


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
                if tupla == (False, False, False, False, False):
                    self.widget.add_separator()
        # Renderiza o menu
        self.widget.place(x=self.pos_x, y=self.pos_y, height=self.altura, width=self.largura)
        return None


class MenuCascata(Elemento):
    '''
    Classe utilizada para instanciar cada menu cascata (widget Menu) da aplicação
    !Atenção! O método renderizar dessa classe não faz nada,
    pois seus elementos serão renderizados no método renderizar da classe BarraDeMenus
    '''
    def __init__(self, master, altura, largura, pos_x, pos_y, lista_submenus):
        '''
        Método construtor
        :param lista_elementos: (rótulo, comando, ícone, status, submenu):
                                espera-se uma lista de tuplas com 5 elementos,
                                onde os primeiros elementos de cada tupla
                                serão os rótulos de cada submenu, os segundos elementos de cada tupla
                                serão os comandos de cada submenu (espera-se um método),
                                os terceiros elementos serão os ícones de cada submenu (False quando não for utilizar)
                                os quartos elementos serão o status de cada submenu (True or False)
                                e os quintos elementos serão submenus (False quando não tiver,
                                ou objeto menu do tkinter quando tiver).
                                Em caso de separadores, utilizar (False, False, False, False, False)
                                na tupla correspondente
        '''
        self.lista_menus = lista_submenus
        super().__init__(master, altura, largura, pos_x, pos_y)
        # Criação do menu cascata
        self.menu = tk.Menu(master=self.master, tearoff=False)
        for elemento in self.lista_submenus:
            if elemento:
                self.menu.add_command(label = elemento[0],
                                      command = elemento[1],
                                      image = elemento[2],
                                      compound = 'left' if elemento[2] else 'none',
                                      state = 'active' if elemento[3] else 'disabled',
                                      menu = elemento[4])
            elif elemento == (False, False, False, False, False):
                self.menu.add_separator()
            else:
                raise AttributeError('Atributos do submenu passados de forma errada')

    def renderizar(self):
        '''
        Método necessário para que a execução do laço que renderiza no método main da aplicação não quebre
        :return: None
        '''
        return None


class BoxDeMensagem():
    '''
    Classe utilizada para instanciar cada box de mensagem (widget messagebox) da aplicação.
    Suas instâncias não devem ser adicionadas na lista principal de execução do script
    '''
    def __init__(self, tipo, titulo, texto):
        '''
        Método construtor
        :param tipo: recebe o tipo do box de mensagem. Pode ser 'I' (informação), 'A' (atenção),
                     'E' (erro), 'OC' (ok/cancela), 'TC' (tentar novamente/cancela),
                     'SN' (sim/não), 'SNC' (sim/não/cancela).
                     Qualquer valor além desses vai retornar um erro no momento de chamar o elemento.
                     Espera-se uma string.
        :param titulo: Título do box de mensagem, espera-se um string
        :param texto: Texto/pergunta do box de mensagem, espera-se uma string
        '''
        self.tipo = tipo
        self.titulo = titulo
        self.texto = texto

    def chamar_box(self):
        '''
        Método que chama os box de mensagens na tela
        :return: A resposta de cada mensagem (True, False, None, 'ok')
        '''
        # Testa os tipos de box de mensagens de acordo com self.tipo
        if self.tipo == 'I':
            return messagebox.showinfo(title=self.titulo, message=self.texto)
        elif self.tipo == 'A':
            return messagebox.showwarning(title=self.titulo, message=self.texto)
        elif self.tipo == 'E':
            return messagebox.showerror(title=self.titulo, message=self.texto)
        elif self.tipo == 'OC':
            return messagebox.askokcancel(title=self.titulo, message=self.texto)
        elif self.tipo == 'TC':
            return messagebox.askretrycancel(title=self.titulo, message=self.texto)
        elif self.tipo == 'SN':
            return messagebox.askyesno(title=self.titulo, message=self.texto)
        elif self.tipo == 'SNC':
            return messagebox.askyesnocancel(title=self.titulo, message=self.texto)
        else:
            raise AttributeError(f'Atributo {self.tipo} não é um tipo válido')


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
        self.imagem = tk.PhotoImage(file=caminho)
        self.widget = tk.Label(master = self.master,
                               height = self.altura,
                               width = self.largura,
                               image = self.imagem)

    def renderizar(self):
        '''
        Renderiza o elemento na tela de acordo com seus atributos
        :return: None
        '''
        self.widget.place(x=self.pos_x, y=self.pos_y)
        return None


janela = tk.Tk()
janela.geometry('800x800')
lista = []
for i in range(3):
    lista.append(Botao(janela, 2, 20, 50 + 10*(i + 1) + i*150, 40, f'Botão {i + 1}', janela.quit))

for i in range(3):
    lista.append(Texto(janela, 2, 20, 50 + 10*(i + 1) + i*150, 100, f'Texto {i + 1}'))
label1 = LabelFrame(janela, 300, 550, 25, 150, 'Sou lindo!')
lista.append(label1)
tabela = Tabela(label1.widget, 1, 1, 0, 0)
lista.append(tabela)
lista.append(Imagem(janela, 256, 256, 25, 500, 'icon.png'))

for elemento in lista: elemento.renderizar()

df = pd.read_csv('titanic.csv')
tabela.renderizar_tabela(df)

janela.mainloop()

