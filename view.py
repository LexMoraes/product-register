from abc import ABC, abstractmethod

from msilib.schema import Component
from tkinter import Tk, Button, Frame, Label, Entry
from tkinter.ttk import Treeview
from types import SimpleNamespace

list_component = []


class BaseView(ABC):
    def __init__(self, title, width, height):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(False, False)

        self._center_window(width=width, height=height)

    def _center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculates coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Sets the size and position of the window
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    @abstractmethod
    def window_setup(self):
        pass

    def run_view(self):
        self.root.mainloop()


class CadastroView(BaseView):
    def __init__(self):
        super().__init__(title='Cadastro', width=300, height=250)

        self._btn_new_component = Button(self.root, text="New component")
        self._btn_list = Button(self.root, text="List")
        self._btn_exit = Button(self.root, text="Exit")

        self.window_setup()

    def window_setup(self):
        self._btn_new_component.grid(column=0, row=0, padx=10, pady=3)
        self._btn_new_component['width'] = 30
        self._btn_new_component['height'] = 4
        self._btn_new_component['font'] = ("Verdana", "10", "italic", "bold")
        self._btn_new_component['command'] = self._command_new_component
        self._btn_list.grid(column=0, row=1, padx=10, pady=3)
        self._btn_list['width'] = 30
        self._btn_list['height'] = 4
        self._btn_list['font'] = ("Verdana", "10", "italic", "bold")
        self._btn_list['command'] = self._command_list

        # settings widgets button _btn_exit
        self._btn_exit.grid(column=0, row=2, padx=10, pady=3)
        self._btn_exit['width'] = 30
        self._btn_exit['height'] = 4
        self._btn_exit['font'] = ("Verdana", 10, "italic", "bold")
        self._btn_exit['command'] = self.root.quit

    @staticmethod
    def _command_new_component():
        new_component = AddNewComponentView()
        new_component.run_view()

    @staticmethod
    def _command_list():
        component = ComponentListView()
        component.run_view()


class AddNewComponentView(BaseView):
    def __init__(self, component=None):
        super().__init__(title='New component', width=700, height=400)
        self._component = component
        self._pan_main = Frame(self.root)

        self._lbl_name = Label(self._pan_main, text='Name:')
        self._txt_name = Entry(self._pan_main)

        self._lbl_price = Label(self._pan_main, text='Price:')
        self._txt_price = Entry(self._pan_main)

        self._lbl_code = Label(self._pan_main, text='Code:')
        self._txt_code = Entry(self._pan_main)

        self._lbl_material = Label(self._pan_main, text='Material:')
        self._txt_material = Entry(self._pan_main)

        self._lbl_imported = Label(self._pan_main, text='Imported:')
        self._txt_imported = Entry(self._pan_main)

        self._btn_save = Button(self._pan_main, text="Save")

        self.window_setup()

    def window_setup(self):
        # settings container _pan_main
        self._pan_main['bd'] = 2
        self._pan_main['bg'] = 'lightgrey'
        self._pan_main.pack(pady=20, padx=20, fill="both", expand=True)

        # settings widgets label _lbl_name
        self._lbl_name.place(x=10, y=10)
        self._lbl_name['width'] = 16
        self._lbl_name['height'] = 2
        self._lbl_name['font'] = ("Verdana", 10)

        # settings widgets entry _txt_name
        self._txt_name.place(x=160, y=10)
        self._txt_name['width'] = 30
        self._txt_name['font'] = ("Verdana", 19)

        # settings widgets label _lbl_price
        self._lbl_price.place(x=10, y=60)
        self._lbl_price['width'] = 16
        self._lbl_price['height'] = 2
        self._lbl_price['font'] = ("Verdana", 10)

        # settings widgets entry _txt_price
        self._txt_price.place(x=160, y=60)
        self._txt_price['width'] = 30
        self._txt_price['font'] = ("Verdana", 19)

        # settings widgets label _lbl_code
        self._lbl_code.place(x=10, y=110)
        self._lbl_code['width'] = 16
        self._lbl_code['height'] = 2
        self._lbl_code['font'] = ("Verdana", 10)

        # settings widgets entry _txt_code
        self._txt_code.place(x=160, y=110)
        self._txt_code['width'] = 30
        self._txt_code['font'] = ("Verdana", 19)

        # settings widgets label _lbl_material
        self._lbl_material.place(x=10, y=160)
        self._lbl_material['width'] = 16
        self._lbl_material['height'] = 2
        self._lbl_material['font'] = ("Verdana", 10)

        # settings widgets entry _txt_material
        self._txt_material.place(x=160, y=160)
        self._txt_material['width'] = 30
        self._txt_material['font'] = ("Verdana", 19)

        # settings widgets label _lbl_imported
        self._lbl_imported.place(x=10, y=210)
        self._lbl_imported['width'] = 16
        self._lbl_imported['height'] = 2
        self._lbl_imported['font'] = ("Verdana", 10)

        # settings widgets entry _txt_imported
        self._txt_imported.place(x=160, y=210)
        self._txt_imported['width'] = 30
        self._txt_imported['font'] = ("Verdana", 19)

        self._btn_save.place(x=300, y=300)
        self._btn_save['width'] = 16
        self._btn_save['height'] = 2
        self._btn_save['command'] = self._command_save

    def _command_save(self):
        component = Component
        component.name = self._txt_name.get()
        component.price = self._txt_price.get()
        component.code = self._txt_code.get()
        component.material = self._txt_material.get()
        component.imported = self._txt_imported.get()

        list_component.append(component)

        self.root.quit()


class ComponentListView(BaseView):

    def __init__(self):
        super().__init__(title='List Component', width=500, height=500)
        self._tree_table = Treeview(self.root)
        self._columns = ('name', 'price', 'code', 'material', 'imported')
        self.window_setup()
        self._list_components()

    def window_setup(self):
        self._tree_table['columns'] = self._columns

        self._tree_table.heading('name', text='Name')
        self._tree_table.heading('price', text='Price')
        self._tree_table.heading('code', text='Code')
        self._tree_table.heading('material', text='Material')
        self._tree_table.heading('imported', text='Imported')

        self._tree_table.column('name', width=50)
        self._tree_table.column('price', width=50)
        self._tree_table.column('code', width=20)
        self._tree_table.column('material', width=20)
        self._tree_table.column('imported', width=40)

        # self._tree_table.bind('<ButtonRelease-1>', self._command_get_selected_item)

        self._tree_table['show'] = 'headings'
        self._tree_table.pack(expand=True, fill='both')

    def _list_components(self):
        for item in list_component:
            self._tree_table.insert('', 'end', values=(
                item.name,
                item.price,
                item.code,
                item.material,
                item.imported
            ))
            self._tree_table.pack(pady=10, padx=10)

    def _command_get_selected_item(self):
        item = self._tree_table.selection()[0]
        print(item)
        values = self._tree_table.item(item, 'values')
        print(values)

        item_dict = dict(zip(self._columns, values))
        print(item_dict)
        component = SimpleNamespace(**item_dict)

        add_new_component = AddNewComponentView(component)
        add_new_component.run_view()

# class ProdutoAcabado(Produto):
#     def __init__(self, nome, preco, codigoLegado, garantia, quantidadePalete):
#         Produto.__init__(self, nome, preco, codigoLegado)
#         self.garantia = garantia
#         self.quantidadePalete = quantidadePalete
