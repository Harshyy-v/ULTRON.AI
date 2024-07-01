import tkinter as tk
import threading
import subprocess


class UltronGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ULTRON.AI")
        self.master.geometry("639x317+0+0")  # Set window size and position

        # Textbox to display output and take input
        self.textbox = tk.Text(self.master, bg="black", fg="white", insertbackground="white")
        self.textbox.pack(expand=True, fill=tk.BOTH)

        # Insert a prompt symbol for user input
        self.textbox.insert(tk.END, "> ")

        # Bind the Return key to the process_input function
        self.textbox.bind("<Return>", self.process_input)

        # Prevent user from modifying the text box except for input
        self.textbox.bind("<Key>", self.disable_input, add="+")

        # Create a subprocess and start a thread to read its output
        self.process = subprocess.Popen(
            ["python", "C:\\Users\\Harsham Vashisht\\OneDrive\\Desktop\\ULTRON.AI\\func\\main.py"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        self.thread = threading.Thread(target=self.read_output)
        self.thread.daemon = True
        self.thread.start()

    def disable_input(self, event):
        # Allow input only in the last line
        if self.textbox.index(tk.INSERT).split('.')[0] != str(int(self.textbox.index(tk.END).split('.')[0]) - 1):
            return "break"

    def read_output(self):
        while True:
            line = self.process.stdout.readline()
            if line:
                self.textbox.insert(tk.END, line)
                self.textbox.insert(tk.END, "> ")  # Add a prompt for the next input
                self.textbox.see(tk.END)  # Auto-scroll to the end
            else:
                break

    def process_input(self, event):
        # Get the input from the last line
        input_start = self.textbox.index(tk.INSERT).split('.')[0] + ".0"
        input_text = self.textbox.get(input_start, tk.END).strip("> ").strip()
        if input_text:  # Check if there is any input text
            # Check if the input contains any of the specified phrases to stop execution
            if any(keyword in input_text.lower() for keyword in ["stop", "no thanks", "nothing", "can go"]):
                print("Execution stopped...")
                # Optionally, you can inform the user in the GUI
                # speak("Execution stopped..")
                # Close the GUI window
            else:
                self.process.stdin.write(input_text + "\n")
                self.process.stdin.flush()
                self.textbox.insert(tk.END, "\n")  # Move to a new line after input
                self.textbox.insert(tk.END, "> ")  # Insert prompt for next input
                self.textbox.see(tk.END)  # Auto-scroll to the end
        return "break"  # Prevent the default behavior of the Return key

    def terminate(self):
        self.process.terminate()  # Terminate the subprocess
        self.master.destroy()


root = tk.Tk()
my_gui = UltronGUI(root)
root.mainloop()
