import tkinter as tk
from password_manager.view.wins import wins_config


class checAppDatakWin(tk.Tk):
    def __init__(self, data: dict):
        super().__init__()

        conf = wins_config.CHECK_WIN_CONF

        text = f'''
        app: {data['app']}
        login: {data['login']}
        password: {data['password']}
        add_info: {data['add_info']}
        '''
        
        # win confs
        self.geometry("400x210+600+300")
        self.resizable(False, False)
        self.title(conf['win_title'])

        # storage info label
        self.label = tk.Label(self, text=text, width=39, height=13)
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