# main.py
import tkinter as tk
from view.view import MainView
from controller.controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(None)
    view = MainView(root, controller)
    controller.view = view  # Conectar a view ao controlador
    root.geometry("300x200")
    root.mainloop()
