import tkinter as tk
from password_manager.view import wins_config
    

class mainWin(tk.Tk):
    def __init__(self, apps_list: list):
        if not isinstance(apps_list, list):
            raise ValueError('arg apps_list must be a list type')

        super().__init__()

        self.__conf = wins_config.MAIN_WIN_CONF

        # win confs
        self.geometry("600x300+600+300")
        self.resizable(False, False)
        self.title(self.__conf['win_title'])
        
        # listbox with apps
        self.apps_listBox = tk.Listbox(self, width=70, height=18)
        self.apps_listBox.grid(column=1, row=1, padx=5, pady=5)
        for item in apps_list:
            self.apps_listBox.insert(tk.END, item)
        
        self.btns_frame = tk.Frame(self, width=50, height=4)
        self.btns_frame.grid(column=2, row=1, padx=5, pady=5)
        
        # btns
        self.check_btn = tk.Button(self.btns_frame, text=self.__conf['view_btn_caption'], width=20, height=2)
        self.check_btn.grid(row=1, pady=5)

        self.add_btn = tk.Button(self.btns_frame, text=self.__conf['add_btn_caption'], width=20, height=2)
        self.add_btn.grid(row=2, pady=5)
