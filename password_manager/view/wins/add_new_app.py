import tkinter as tk
from password_manager.view.wins import wins_config

class addNewApp(tk.Tk):
    def __init__(self):
        super().__init__()

        conf = wins_config.ADD_NEW_APP_WIN_CONF

        # win confs
        self.geometry("620x315+600+300")
        #self.resizable(False, False)
        self.title(conf['win_title'])

        # app frame
        self.app_frame = tk.Frame(self, width=400, height=400)
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
        self.gen_password_frame = tk.Frame(self, width=200, height=400)
        self.gen_password_frame.grid(column=2, row=1, padx=5, pady=5)

        # radiobutton
        self.radiobtn_var = tk.IntVar().set(0)
        self.gen_password_radiobtn = tk.Radiobutton(self.gen_password_frame, text=conf['gen_password_radiobtn'], variable=self.radiobtn_var, value=0)
        self.gen_password_radiobtn.grid(padx=5, pady=5, row=1, sticky='w')

        # checkbtn with numbs
        self.numbs_checkbtn_var = tk.IntVar().set(0)
        self.numbs_checkbtn = tk.Checkbutton(self.gen_password_frame, text=conf['numbs_checkbox'], variable=self.numbs_checkbtn_var, onvalue=1, offvalue=0)
        self.numbs_checkbtn.grid(padx=5, pady=5, row=2, sticky='w')

        # checkbtn with ALPH
        self.ALPH_checkbtn_var = tk.IntVar().set(0)
        self.ALPH_checkbtn = tk.Checkbutton(self.gen_password_frame, text=conf['ALPH_checkbtn'], variable=self.ALPH_checkbtn_var, onvalue=1, offvalue=0)
        self.ALPH_checkbtn.grid(padx=5, pady=5, row=3, sticky='w')

        # checkbtn with alph
        self.alph_checkbtn_var = tk.IntVar().set(0)
        self.alph_checkbtn = tk.Checkbutton(self.gen_password_frame, text=conf['alph_checkbtn'], variable=self.alph_checkbtn_var, onvalue=1, offvalue=0)
        self.alph_checkbtn.grid(padx=5, pady=5, row=4, sticky='w')

        # checkbtn with spec_symbs
        self.spec_symbs_checkbtn_var = tk.IntVar().set(0)
        self.spec_symbs_checkbtn = tk.Checkbutton(self.gen_password_frame, text=conf['spec_symbs_checkbtn'], variable=self.spec_symbs_checkbtn_var, onvalue=1, offvalue=0)
        self.spec_symbs_checkbtn.grid(padx=5, pady=5, row=5, sticky='w')

        # password len spinbox
        self.spinbox_label = tk.Label(self.gen_password_frame, text=conf['password_len_spinbox'])
        self.spinbox_label.grid(padx=5, pady=5, row=6, sticky='w')
        self.password_len_spinbox = tk.Spinbox(self.gen_password_frame, from_=8, to=20)
        self.password_len_spinbox.grid(padx=5, pady=5, row=7, sticky='w')

        # gen password btn
        self.gen_password_btn = tk.Button(self.gen_password_frame, text=conf['gen_password_btn'])
        self.gen_password_btn.grid(padx=5, pady=5, row=8, sticky='ew')
