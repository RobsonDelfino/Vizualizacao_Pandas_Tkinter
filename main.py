'''
Este  script vai criar uma interface gráfica para vizualização de arquivos .csv
Um tutorial está sendo seguido de acordo com o vídeo
"https://www.youtube.com/watch?v=PgLjwl6Br0k&list=WL&index=100&ab_channel=RamonWilliams"
O objetivo, no futuro, é criar um manipulador de arquivo .csv usando Pandas, totalmente interfaceado.
Dessa forma, quem não domina Pandas, poderá se beneficiar dessa biblioteca para tratar seus dados.
'''

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

# Funções
def file_dialog():
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Selecione um arquivo',
                                          filetype=(('Arquivos CSV', '*.csv'),('Todos os arquivos', '*.*')))
    label_file['text'] = filename
    return None


def load_csv_data():
    file_path = label_file['text']
    try:
        csv_filename = r'{}'.format(file_path)
        df = pd.read_csv(csv_filename)
    except ValueError:
        tk.messagebox.showerror('Atenção', 'O arquivo que você escolheu é inválido!')
        return None
    except FileNotFoundError:
        tk.messagebox.showerror('Atenção', f'O arquivo {file_path} não existe!')
        return None

    clear_data()
    tv1['columns'] = list(df.columns)
    tv1['show'] = 'headings'
    for column in tv1['columns']:
        tv1.heading(column, text=column)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert('', 'end', values=row)

    return None

def clear_data():
    tv1.delete(*tv1.get_children())



root = tk.Tk()
root.title('Vizualizador CSV')
root.geometry('500x500')
root.pack_propagate(False)
root.resizable(False, False)

# LabelFrame para Treeviews
frame1 = tk.LabelFrame(root, text='Dados CSV')
frame1.place(height=250, width=500)

# Treeview
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient='vertical', command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient='horizontal', command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrolly.pack(side='right', fill='y')
treescrollx.pack(side='bottom', fill='x')

# Frame para abrir arquivos
file_frame = frame1 = tk.LabelFrame(root, text='Abrir arquivo')
file_frame.place(height=100, width=500, rely=0.65, relx=0)

# Botões e Label
button1 = tk.Button(file_frame, text='Escolher um arquivo', command=lambda: file_dialog())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame, text='Carregar', command=lambda: load_csv_data())
button2.place(rely=0.65, relx=0.3)

label_file = tk.Label(file_frame, text='Nenhum Arquivo Selecionado')
label_file.place(rely=0, relx=0)

root.mainloop()