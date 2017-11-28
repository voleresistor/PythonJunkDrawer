# Testing building GUI windows with tkinter module in Py 3.5
# Minimal Application from: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# 05/26/17

import tkinter as tk

class Application(tk.Frame):
    '''
    Sample application class
    '''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''
        Generate buttons in window
        '''
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid()

MY_APP = Application()
MY_APP.master.title('Sample Application')
MY_APP.mainloop()
