import tkinter as tk
from password_manager.view import wins_config
    

class mainWin(tk.Tk):
    '''
    password storage main win
    '''
    def __init__(self):
        super().__init__()

        conf = wins_config.MAIN_WIN_CONF

        # win confs
        self.geometry("600x305+600+300")
        self.resizable(False, False)
        self.title(conf['win_title'])

        # menu
        self.menu = tk.Menu(self, tearoff=0)
        self.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label=conf['open_storage'])
        file_menu.add_command(label=conf['new_storage'])
        file_menu.add_command(label=conf['save_storage'])

        self.menu.add_cascade(label=conf['file_menu'], menu=file_menu)

        self.menu.add_command(label=conf['about_prog'])

        # listbox with apps
        self.apps_listBox = tk.Listbox(self, width=70, height=18)
        self.apps_listBox.grid(column=1, row=1, padx=5, pady=5)

        self.btns_frame = tk.Frame(self, width=50, height=4)
        self.btns_frame.grid(column=2, row=1, padx=5, pady=5)

        # btns
        self.check_btn = tk.Button(self.btns_frame, text=conf['view_btn_caption'], width=20, height=2)
        self.check_btn.grid(row=1, pady=5)

        self.add_btn = tk.Button(self.btns_frame, text=conf['add_btn_caption'], width=20, height=2)
        self.add_btn.grid(row=2, pady=5)

        self.change_btn = tk.Button(self.btns_frame, text=conf['change_btn_caption'], width=20, height=2)
        self.change_btn.grid(row=3, pady=5)

        self.del_btn = tk.Button(self.btns_frame, text=conf['del_btn_caption'], width=20, height=2)
        self.del_btn.grid(row=4, pady=5)


class checkWin(tk.Tk):
    def __init__(self, 
                 login: str, 
                 password: str,
                 data: str
                 ):
        super().__init__()

        conf = wins_config.CHECK_WIN_CONF

        # win confs
        self.geometry("400x210+600+300")
        self.resizable(False, False)
        self.title(conf['win_title'])

        # storage info label
        self.label = tk.Label(self, text=data, width=39, height=13)
        self.label.grid(column=1, row=1, padx=5, pady=5)

        # btns frame
        self.btns_frame = tk.Frame(self, width=100, height=200)
        self.btns_frame.grid(column=2, row=1, padx=5, pady=5)

        # btns
        self.login_btn = tk.Button(self.btns_frame, text=conf['copy_login_btn_caption'],
                                    width=13, height=2)
        self.login_btn.grid(row=1, pady=5)

        self.password_btn = tk.Button(self.btns_frame, text=conf['copy_password_btn_caption'],
                                       width=13, height=2)
        self.password_btn.grid(row=2, pady=5)

class addNewApp(tk.Tk):
    def __init__(self):
        super().__init__()

        conf = wins_config.ADD_NEW_APP_WIN_CONF

        # win confs
        self.geometry("620x415+600+300")
        #self.resizable(False, False)
        self.title(conf['win_title'])

        # app frame
        self.app_frame = tk.Frame(self, width=400, height=400, background='red')
        self.app_frame.grid(column=1, row=1, padx=5, pady=5)

        # app name
        self.app_textbox = tk.Text(self.app_frame, width=40, height=2)
        self.app_textbox.grid(column=1, row=1, pady=5)

        self.app_label = tk.Label(self.app_frame, text=conf['app_label'], width=10, height=2)
        self.app_label.grid(column=2, row=1, padx=5, pady=5)

        # app login
        self.login_textbox = tk.Text(self.app_frame, width=40, height=2)
        self.login_textbox.grid(column=1, row=2, pady=5)

        self.login_label = tk.Label(self.app_frame, text=conf['login_label'], width=10, height=2)
        self.login_label.grid(column=2, row=2, pady=5, padx=5)

        # app password
        self.password_textbox = tk.Text(self.app_frame, width=40, height=2)
        self.password_textbox.grid(column=1, row=3, pady=5)

        self.password_label = tk.Label(self.app_frame, text=conf['password_label'], width=10, height=2)
        self.password_label.grid(column=2, row=3, padx=5, pady=5)

        # app add info
        self.add_info_textbox = tk.Text(self.app_frame, width=40, height=5)
        self.add_info_textbox.grid(column=1, row=4, pady=5)

        self.add_info_label = tk.Label(self.app_frame, text=conf['add_info_label'], width=10, height=5)
        self.add_info_label.grid(column=2, row=4, padx=5, pady=5)

        # gen password frame
        self.gen_password_frame = tk.Frame(self, width=200, height=400, background='black')
        self.gen_password_frame.grid(column=2, row=1, padx=5, pady=5)