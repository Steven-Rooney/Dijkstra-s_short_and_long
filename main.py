import tkinter as tk
import subprocess

#import ShortestSearch

#maybe
#test = {'x': {'G': 5, 'A': 1, 'C': 2}}
#ShortestSearch.graph.update(test)
#print(ShortestSearch.graph)


top = tk.Tk()
top.geometry('200x200')

B1 = tk.Button(top, text="Dijkstra's Shortest Search", command=lambda: ShortSearch())
B1.place(x=25, y=50)
B2 = tk.Button(top, text="Dijkstra's Longest Search", command=lambda: LongSearch())
B2.place(x=25, y=100)
lbl1 = tk.Label(top, text='')
lbl1.pack()



def ShortSearch():
    cmd1 = 'python C:\\Users\\Steven\\PycharmProjects\\Djikstra_Project\\ShortestSearch.py'
    try:
        output = subprocess.check_output(cmd1, shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    lbl1['text'] = output.strip()

def LongSearch():
    cmd2 = 'python C:\\Users\\Steven\\PycharmProjects\\Djikstra_Project\\LongestSearch.py'

    try:
        output = subprocess.check_output(cmd2, shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    lbl1['text'] = output.strip()

top.mainloop()