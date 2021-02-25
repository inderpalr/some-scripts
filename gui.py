#!/usr/bin/python
import tkinter as tk
from logic import create_ec2, stop_ec2
from instances import get_instances

# Main container
gui_container = tk.Tk()
gui_container.minsize(width=400, height=450)
gui_container.title('Infrastruture Script')

# Introduction

label = tk.Label(text='This is a utility for an engineer. It contains some common use case scripts.')
label.pack()


button_aws = tk.Button(gui_container,text = 'AWS Provisioning', command = create_ec2, fg = 'green')
button_aws.place(x=35,y=370)
button_aws = tk.Button(gui_container,text = 'Stop Instance', fg = 'red', command = stop_ec2)
button_aws.place(x=35,y=400)
button_gcp = tk.Button(gui_container,text = 'GCP Provisioning', fg = 'green')
button_gcp.place(x=265,y=370)
button_aws = tk.Button(gui_container,text = 'Stop Instance', fg = 'red')
button_aws.place(x=265,y=400)
button_exit = tk.Button(gui_container,text = 'Exit', fg ='red', command = gui_container.destroy)
button_exit.place(x=355,y=20)
button_instances = tk.Button(gui_container, text = 'List Instances', command = get_instances)
button_instances.place(x=200,y=200)


gui_container.mainloop()