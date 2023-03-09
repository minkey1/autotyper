from keyboard import write, press_and_release
import time
from time import sleep
import tkinter as tk


def removeComments(input_str):
    lines = input_str.strip().split('\n')
    output_lines = []
    for line in lines:
        if not '//' in line:
            output_lines.append(line)

    output_str = '\n'.join(output_lines)
    return output_str


def holdDelete():
    start_time = time.time()

    while time.time() - start_time < 1:
        press_and_release('delete')
        pass


def typeInput():
    sleep(5)
    a = text.get('1.0', 'end-1c')
    notabs = a.replace("    ", "")  # Removes all the tabs in the code
    nocomments = removeComments(notabs)

    for i in nocomments:

        write(i)
        sleep(0.02)
    holdDelete()


def clearText():
    text.delete('1.0', tk.END)


root = tk.Tk()
root.title('elab Autotyper by Minkey')

text = tk.Text(root,)
text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

instructions = '''
Instructions:
1. Use Crl+V to paste your answer here and click print
2. Switch to your elab window and click on the typing window where you 
   want the answer pasted
3. After 6 seconds the answer will be typed automatically in which ever 
   window you clicked

Note:
Wait for 2 seconds even after it looks like the autotyper is done working
Press 'Clear' to clear this text


'''

text.insert('1.0', instructions)

printButton = tk.Button(root, height=2, text='Print',
                        command=lambda: typeInput())
printButton.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)


clear = tk.Button(root, height=2, text='Clear',
                  command=lambda: clearText())
clear.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=5)


root.mainloop()
