import threading
import tkinter as tk
from tkinter import font as tkfont
from tkinter.messagebox import showerror
from client_socket import ClientSocket


class ChatApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x400")

        self.title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.base_font = tkfont.Font(family='Helvetica', size=14)

        self.client_socket = ClientSocket()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=5)
        container.grid_columnconfigure(0, weight=5)

        self.frames = {}
        for F in (LoginPage, ChatPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):

    def login_user(self):
        res = self.controller.client_socket.login_user(self.input_login.get())
        if res is None:
            self.controller.show_frame("ChatPage")
            self.controller.frames["ChatPage"].show_messages_start()
        else:
            showerror('Server Error', res)
            self.input_login.delete(0, tk.END)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter your nickname:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.input_login = tk.Entry(self, font=controller.base_font)
        self.input_login.pack(side="top", fill="x", pady=10, padx=50)

        button_login = tk.Button(self, text="Enter Chat", font=controller.base_font,
                                 command=self.login_user)
        button_login.pack(side="top", fill="x", pady=10, padx=50)


class ChatPage(tk.Frame):

    def messages_updater(self):
        while True:
            if len(self.controller.client_socket.new_messages) != 0:
                for i in self.controller.client_socket.new_messages:
                    self.messages_listbox.insert(tk.END, i)
                    self.controller.client_socket.messages.append(i)
                self.controller.client_socket.new_messages.clear()

    def show_messages_start(self):
        for i in self.controller.client_socket.messages:
            self.messages_listbox.insert(tk.END, str(i))

        threading.Thread(target=self.messages_updater, daemon=True).start()

    def send_message(self):
        message = self.input_message.get()

        if message != '' or message is not None or message != ' ':
            self.controller.client_socket.send_message(message)
            self.input_message.delete(0, tk.END)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Chat", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        frm_messages = tk.Frame(self)
        scrollbar = tk.Scrollbar(frm_messages)
        self.messages_listbox = tk.Listbox(
            frm_messages,
            yscrollcommand=scrollbar.set,
            font=controller.base_font
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        self.messages_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        frm_messages.pack(side="top", fill="x", pady=10, padx=50)

        self.input_message = tk.Entry(self, font=controller.base_font)
        self.input_message.pack(side="top", fill="x", pady=10, padx=50)

        button = tk.Button(self, text="Send message", font=controller.base_font,
                           command=self.send_message)
        button.pack(side="top", fill="x", pady=10, padx=50)


if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
