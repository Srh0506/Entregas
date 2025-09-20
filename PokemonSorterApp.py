# PokemonSorterApp.py
import tkinter as tk
from tkinter import ttk
from ApiRequest import ApiRequest

from bubbleSort import BubbleSort
from quickSort import QuickSort
from mergeSort import MergeSort
from insertionSort import InsertionSort
from selectionSort import SelectionSort
from heapSort import HeapSort
from countingSort import CountingSort
from radixSort import RadixSort
from bucketSort import BucketSort

from pokemonSorter import PokemonSorter

class PokemonSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon-Dongo")
        self.root.configure(bg="#282c34")

        # Fetch data from API
        self.api_client = ApiRequest()
        self.data = self.api_client.fetch_data()

        # Columnas numéricas
        self.columns = ["HP", "Ataque", "Defensa"]
        self.col_map = {"HP": "hp", "Ataque": "attack", "Defensa": "defense"}

        # Estrategias de ordenamiento
        self.algorithms = {
            "Bubble Sort": BubbleSort(),
            "Quick Sort": QuickSort(),
            "Merge Sort": MergeSort(),
            "Insertion Sort": InsertionSort(),
            "Selection Sort": SelectionSort(),
            "Heap Sort": HeapSort(),
            "Counting Sort": CountingSort(),
            "Radix Sort": RadixSort(),
            "Bucket Sort": BucketSort()
        }

        # UI Elements
        self.sort_label = tk.Label(root, text="Seleccione el método de ordenamiento:", bg="#282c34", fg="white", font=("Helvetica", 12))
        self.sort_label.pack(pady=5)

        self.sort_method = ttk.Combobox(root, values=list(self.algorithms.keys()), state="readonly")
        self.sort_method.pack(pady=5)

        self.column_label = tk.Label(root, text="Seleccione la columna:", bg="#282c34", fg="white", font=("Helvetica", 12))
        self.column_label.pack(pady=5)

        self.column_choice = ttk.Combobox(root, values=self.columns, state="readonly")
        self.column_choice.pack(pady=5)

        self.sort_button = tk.Button(root, text="Ordenar", command=self.sort_data, bg="#61afef", fg="white", font=("Helvetica", 10, "bold"), relief="flat")
        self.sort_button.pack(pady=10)

        # Treeview
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings", height=15)
        for col in self.columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        # Mostrar datos originales
        self.display_data(self.data)

    def display_data(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for pokemon in data:
            self.tree.insert("", tk.END, values=(pokemon['hp'], pokemon['attack'], pokemon['defense']))

    def sort_data(self):
        method = self.sort_method.get()
        column = self.column_choice.get()

        if method and column:
            strategy = self.algorithms[method]
            col_key = self.col_map[column]
            sorter = PokemonSorter(self.data)
            sorted_data = sorter.sort(strategy, col_key, ascending=True)
            self.display_data(sorted_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonSorterApp(root)
    root.mainloop()
