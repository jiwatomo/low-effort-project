import tkinter as tk
from functools import partial
from func import *

# Global Variable
app_mode = 0


def main():
	windw = tk.Tk()
	windw.title("Menu")
	
	# Top
	top_area = tk.Frame()
	top_area.pack()
	dlabel = tk.Label(master=top_area, text="Welcome!, select the mode first")
	dlabel.pack(side=tk.LEFT)
	tfr = tk.Frame(master=top_area, width="33")
	tfr.pack(side=tk.LEFT, fill=tk.X)
	btn_mode = tk.Button(master=top_area, text="Change mode")
	btn_mode.pack(side=tk.RIGHT)
	
	
	# Mid
	mid_area = tk.Frame(relief=tk.SUNKEN, borderwidth=4)
	mid_area.pack()
	#  dlabel_mid = tk.Label(master=mid_area, text="Mid Area")
	#  dlabel_mid.pack()
	
	# Side left
	left_side =tk.Frame(master=mid_area, borderwidth=3)
	left_side.pack(fill=tk.Y, side=tk.LEFT)
	
	btn_perform = tk.Button(master=left_side, text="Performance")
	btn_perform.pack(fill=tk.X)
	btn_ExplorerON = tk.Button(master=left_side, text="ExplorerON")
	btn_ExplorerON.pack(fill=tk.X)
	btn_ExplorerOFF = tk.Button(master=left_side, text="ExplorerOFF")
	btn_ExplorerOFF.pack(fill=tk.X)
	
	frame_kosong_config = {
		"widtha": 20,
		"heighta": 1
	}
	
	frame_kosong = tk.Frame(master=mid_area, width=frame_kosong_config["widtha"], height=frame_kosong_config["heighta"])
	frame_kosong.pack(side=tk.LEFT,fill=tk.X)
	
	# Center
	center_side = tk.Frame(master=mid_area, borderwidth=3)
	center_side.pack(fill=tk.Y, side=tk.LEFT)
	
	btn_list_row1 = ["test1", "test2", "test3"]
	btn_list_row2 = ["test4", "test5", "test6"]
	btn_list_row3 = ["test7", "test8", "test9"]
	for i in range(3):
		if i == 0:
			inc = 0
			for j in btn_list_row1:
				btnframe = tk.Frame(master=center_side, relief=tk.RAISED, borderwidth=1)
				btnframe.grid(row=i, column=inc)
				btn_mid = tk.Button(master=btnframe, text=j, command=partial(mid_button_handler, j))
				btn_mid.pack()
				inc += 1
		elif i == 1:
			inc = 0
			for j in btn_list_row2:
				btnframe = tk.Frame(master=center_side, borderwidth=1)
				btnframe.grid(row=i, column=inc)
				btn_mid = tk.Button(master=btnframe, text=j, command=partial(mid_button_handler, j))
				btn_mid.pack()
				inc += 1
		elif i == 2:
			inc = 0
			for j in btn_list_row3:
				btnframe = tk.Frame(master=center_side, borderwidth=1)
				btnframe.grid(row=i, column=inc)
				btn_mid = tk.Button(master=btnframe, text=j, command=partial(mid_button_handler, j))
				btn_mid.pack()
				inc += 1
		
	frame_kosong = tk.Frame(master=mid_area, width=frame_kosong_config["widtha"], height=frame_kosong_config["heighta"])
	frame_kosong.pack(side=tk.LEFT,fill=tk.X)
				
	# Side right
	left_side = tk.Frame(master=mid_area, borderwidth=3)
	left_side.pack(fill=tk.Y, side=tk.RIGHT)
	
	btn_command = tk.Button(master=left_side, text="cmd")
	btn_command.pack(fill=tk.X)
	btn_kill = tk.Button(master=left_side, text="Kill")
	btn_kill.pack(fill=tk.X)
	btn_exit = tk.Button(master=left_side, text="Exit")
	btn_exit.pack(fill=tk.X)
	
	
	# Bottom
	bottom_area = tk.Frame()
	bottom_area.pack()
	dlabel_bottom = tk.Label(master=bottom_area, text="Bottom Area")
	dlabel_bottom.pack()
	
	
	windw.mainloop()
	
	
	
	
if __name__ == "__main__":
	main()
	
