import tkinter as tk
import tkinter.ttk as ttk
import File
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Statistics import Statistics

# Main with GUI
class App:
    def __init__(self, master):
        self.error_log = tk.StringVar()

        # Main frame
        frame = tk.Frame(master)
        frame.pack()

        # Text fields space
        fields_frame = tk.Frame(frame)
        fields_frame.grid(row=0, column=1)

        # path name
        self._path = tk.StringVar()
        self._path.set("Status: No file opened")
        path_space = tk.Label(fields_frame, textvariable=self._path)
        path_space.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        self.txt_space = tk.Text(fields_frame, bg="#dcdfe3")
        self.txt_space.grid(row=1, column=0, sticky="nsew", padx=5)

        # Buttons Left Panel space
        buttons_frame = tk.Frame(frame, bg="lightgray")
        buttons_frame.grid(row=0, column=0, sticky="ns")

        # actions label
        self.actions_label = tk.Label(buttons_frame, textvariable=self.error_log, bg="lightgray")
        self.actions_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # button for opening a file
        btn_open = tk.Button(buttons_frame, text="Open", command=self.open_file)
        btn_open.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        # button for computing
        btn_compute = tk.Button(buttons_frame, text="Compute", command=self.compute_data)
        btn_compute.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        # button for saving
        btn_save = tk.Button(buttons_frame, text="Save", command=self.save_file)
        btn_save.grid(row=3, column=0, sticky="ew", padx=5)

    def format_dataset(self, dataset):
        # dataset is taken as string from txt_space
        # splitting data between \n
        splitted_ = dataset.split('\n')
        # filter blank spaces
        filtered_ = list(filter(('').__ne__, splitted_))
        string_dataset = []

        # filtering alphanumeric 
        for i in filtered_ :
            current = ""
            for j in i:
                if not j.isalnum():
                    continue
                elif j.isalpha():
                    continue
                else:
                    current += j
            string_dataset.append(current)  

        # cast to integer
        final_dataset = [int(numeric_str) for numeric_str in string_dataset]
        return final_dataset

    def compute_data(self):
        # end-1c because it deletes 1 character (newline character)
        dataset = self.txt_space.get("1.0", 'end-1c')
        # using Statistics class to generate ECDF, MEAN, VARIANCE and STD
        stats = Statistics(self.format_dataset(dataset))
        stats.plot_data("INFO")
        stats.cdf()
        

    def save_file(self):
        # getting path
        filepath = self._path.get()
        if len(filepath) == 0:
            # saving file procedure
            filepath = asksaveasfilename(
                defaultextension="txt",
                filetypes=[("Text files", "*.txt")]
            )

        if not filepath:
            return

        # get data from file and put it into txt_space
        writer = File.File(filepath)
        text = self.txt_space.get("1.0", tk.END)
        writer.save_data(text)
        return

    def get_data_from_(self, dtype, path_name):
        # you can select type of source to get data
        # for now only txt is supported
        reader = File.File(path_name)
        if dtype == 'txt':
            data = reader.get_data()
            for d in data:
                self.txt_space.insert(tk.END, str(d))

    def open_file(self):
        # Importing file
        filepath = askopenfilename(
            filetypes=[("TXT files", "*.txt")]
        )
        if not filepath:
            return
        # erase previous content
        self.txt_space.delete('1.0', tk.END)
        # update opened file path
        self._path.set(filepath)
        # data type cases (FOR NOW IT SUPPORTS TXT FILES ONLY)
        if filepath.endswith('.txt'):
            # getting data from txt file and write it on text space
            self.get_data_from_('txt', filepath)


def main():
    # Main root
    root = tk.Tk(className='OmniStatsPy')
    root.geometry("700x400")
    # fixed size window
    root.resizable(0, 0)
    # first row config
    root.rowconfigure(0, minsize=600, weight=1)
    # second row config
    root.columnconfigure(1, minsize=600, weight=1)
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
