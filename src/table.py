from tkinter import *

class Table:
	def __init__(self, root, table, component):
		self.root = Tk()
		
		i = 1
		for j in table:
			i2 = 1
			Label(self.root, text=component).grid(row=0, columnspan=10)
			Label(self.root, text=j).grid(row=i, column=0)
			for k in table[j]:
				self.entry = Label(self.root, text=k).grid(row=i, column=i2)
				i2 += 1
			i += 1

		self.root.mainloop()

