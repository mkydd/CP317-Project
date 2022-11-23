import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from FileReader import FileReader
from FileErrorHandling import FileErrorHandling

class GUI():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1000x500")
        self.window.title("File Reader")

        self.NameFile = ""
        self.CourseFile = ""

        self.GradeFileDirectory = ""

        self.label_note = Label(self.window, 
                                    text = "For Most Seamless Experience Complete\nEach Action In Order (top-down)",
                                    wraplength=250,
                                    height=5)

        self.button_NameFile = Button(self.window,
						text = "Select the NameFile",
                        width = 30,
                        height = 3,
                        activebackground = 'red',
						command = self.browseFiles_NameFile)

        self.button_CourseFile = Button(self.window,
                                text = "Select the CourseFile",
                                width = 30,
                                height = 3,
                                command = self.browseFiles_CourseFile)                    

        self.button_exit = Button(self.window,
                            text = "Exit",
                            width = 30,
                            height = 3,
                            command = self.exit)

        self.button_gradefile_directory = Button(self.window,
                                text = "Select Where you Want the GradeFile",
                                width = 30,
                                height = 3,
                                command = self.chooseDirectory)
        
        self.button_generate_gradefile = Button(self.window,
                                            text = "Generate a Grade File",
                                            width = 30,
                                            height = 3,
                                            command = self.generateGradeFile)
        
        # adds buttons to window
        self.buttons()

        # show the window
        self.main()

    def exit(self):
        self.window.destroy()

    def chooseDirectory(self):
        directory = filedialog.askdirectory()
        
        self.GradeFileDirectory = directory


    def validFiles(self):
        FEH = FileErrorHandling(self.NameFile, self.CourseFile, self.GradeFileDirectory)

        # check if a nameFile is selected
        if (not self.NameFile):
            messagebox.showerror("showerror", "Please select a valid NameFile")
            return False

        # check if a courseFile is selected
        elif (not self.CourseFile):
            messagebox.showerror("showerror", "Please select a valid CourseFile")
            return False

        # check if either file is empty
        elif (FEH.isEmpty() == True):
            messagebox.showerror("showerror", "One or both of the files you selected did not contain text. Please select appropriate files and try again")
            return False

        # check if gradeFileDirectory selected
        elif (FEH.validGradeFileDirectory() == False):
            messagebox.showerror("showerror", "You did not select a GradeFile directory. Please select a directory and try again")
            return False

        return True

    def generateGradeFile(self):
        if (not self.validFiles()):
            return
             
        fr = FileReader()

        fr.fileReader(self.NameFile, self.CourseFile, self.GradeFileDirectory)

    def browseFiles_NameFile(self):
        expected_name = "NameFile.txt"

        filename = filedialog.askopenfilename(initialdir = "/Users/michaelkydd/Documents/University/Project",
                                            title = "Select the NameFile",
                                            filetypes = (("Text files",
                                                            "*.txt"),
                                                        ("all files",
                                                            "*.*")))


        input_name = filename.split("/")[-1]

        if (input_name == expected_name):
            self.NameFile = filename
            print(filename)
            return
        if (filename):
            print(filename)
            self.wrongFileSelected(expected_name)

        return

    def browseFiles_CourseFile(self):
        expected_name = "CourseFile.txt"

        filename = filedialog.askopenfilename(initialdir = "/Users/michaelkydd/Documents/University/Project",
                                            title = "Select the CourseFile",
                                            filetypes = (("Text files",
                                                            "*.txt"),
                                                        ("all files",
                                                            "*.*")))


        input_name = filename.split("/")[-1]

        if (input_name == expected_name):
            self.CourseFile = filename
            print(filename)
            return

        if (filename):
            print(filename)
            self.wrongFileSelected(expected_name)

        return

    def wrongFileSelected(self, expected_name):
        messagebox.showinfo("showinfo", "Please Select a File Named {}".format(expected_name))

    def buttons(self):
        self.label_note.pack(side=TOP)

        self.button_NameFile.pack(side=TOP)
        self.button_CourseFile.pack(side=TOP)

        self.button_gradefile_directory.pack(side=TOP)
        self.button_generate_gradefile.pack(side=TOP)


        self.button_exit.pack(side=TOP)
        
    def main(self):
        self.window.mainloop()

