import tkinter as tk
import tkinter.filedialog as fd
from password_manager.model.core import passwordStorage
from password_manager.view.wins import wins_config
from password_manager.view.wins.check_app_data import checAppDatakWin


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
        file_menu.add_command(label=conf['open_storage'], command=self.__open_storage)
        file_menu.add_command(label=conf['new_storage'], state='disabled')
        file_menu.add_command(label=conf['save_storage'], state='disabled')

        self.menu.add_cascade(label=conf['file_menu'], menu=file_menu)

        self.menu.add_command(label=conf['about_prog'], state='disabled')

        # listbox with apps
        self.apps_listBox = tk.Listbox(self, width=70, height=18, selectmode='SINGLE')
        self.apps_listBox.grid(column=1, row=1, padx=5, pady=5)

        self.btns_frame = tk.Frame(self, width=50, height=4)
        self.btns_frame.grid(column=2, row=1, padx=5, pady=5)

        # btns
        self.check_btn = tk.Button(self.btns_frame, text=conf['view_btn_caption'], width=20, height=2, command=self.__app_btn_click)
        self.check_btn.grid(row=1, pady=5)

        self.add_btn = tk.Button(self.btns_frame, text=conf['add_btn_caption'], width=20, height=2)
        self.add_btn.grid(row=2, pady=5)

        self.change_btn = tk.Button(self.btns_frame, text=conf['change_btn_caption'], width=20, height=2)
        self.change_btn.grid(row=3, pady=5)

        self.del_btn = tk.Button(self.btns_frame, text=conf['del_btn_caption'], width=20, height=2)
        self.del_btn.grid(row=4, pady=5)

    def __update_apps_listBox(self, apps_list: list):
        'update listbox'
        self.apps_listBox.delete(0, self.apps_listBox.size())

        for i in range(len(apps_list)):
            item = apps_list[i]
            if not isinstance(item, str):
                raise TypeError(f'all items in apps_list must be str type, not {type(item)}')
            self.apps_listBox.insert(i, item)

    def __open_storage(self):
        'get storage path, check, send to listbox with apps'
        storage_path = fd.askopenfile(filetypes=([("Json", '*.json')])).name
        self.storage = passwordStorage(storage_path)
        self.apps_list = list(self.storage.get_storage().keys())
        self.__update_apps_listBox(self.apps_list)

    def __app_btn_click(self):
        'action at the click of a check app btn'
        select_app_ind = self.apps_listBox.curselection()[0]
        storage = self.storage.get_storage()
        apps_names = list(storage.keys())
        
        data = storage[apps_names[select_app_ind]]
        check_app_data_win = checAppDatakWin(data)
        check_app_data_win.grab_set()
