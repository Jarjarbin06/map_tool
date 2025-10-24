#############################
###                       ###
###          MAP          ###
###     ----viewer----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

class Setting :
    
    """
        Import modules and set initial settings values
    """

    import sys
    import os
    import socket
    import tkinter as tk
    from tkinter import filedialog
    import pygame as pg
    import numpy as np
    main_path = __file__.removesuffix("/viewer.py")

class File :
    
    """
        generator.NoiseMap File
    """

    def __init__(self : object, path : str) -> None :
        
        """
            Open File

            Parameters:
                - self (object) : File
                - path (str) : full path to file
        """
        
        self.contain_error = False
        try :
            with open(path, "r") as file :
                file_list = file.readlines()
            file.close()
        except FileNotFoundError :
            print("no file named {path} was found")
            self.contain_error = True
        self.info = file_list.pop(0).removesuffix("\n")
        self.compiled_arr = []
        self.type = None
        self.path = path
        for line in file_list :
            if not self.type :
                self.type = type(line.removeprefix("[").removesuffix("]\n").split(", ")[0])
            self.compiled_arr.append(line.removeprefix("[").removesuffix("]\n").split(", "))
        self.arr = Setting.np.array(self.compiled_arr, dtype=self.type)
        return

    def __str__(self : object) -> str :
        
        """
            Return string of info

            Parameters:
                - self (object) : File

            Returns:
                - str : string of File info + string of array
        """
        
        if self.contain_error :
            return
        ret_str = f"{self.info.split('*')}\n"
        for line in self.compiled_arr :
            ret_str += str(line) + "\n"
        return ret_str

    def open(path : None | str = None) -> object :
        
        """
            Return new File

            Parameters:
                - path (None | str) : full path to file

            Returns:
                - object : File
        """
        
        while not path :
            path = Setting.filedialog.askopenfilename(defaultextension="txt", initialdir=Setting.main_path + "/generated_maps")
        return File(path)

    def show(self : object, size : tuple[int, int] = (600, 600)) -> None :
        
        """
            Show file in a window

            Parameters:
                - self (object) : File
                - size (tuple[int, int]) = (600, 600) : size of the window
        """
        
        if self.contain_error :
            return
        Setting.pg.init()
        screen = Setting.pg.display.set_mode(size)
        Setting.pg.display.set_caption(f"MAP by JARJARBIN'S STUDIO | VIEWER | {self.path}")
        icon = Setting.pg.image.load("files/images/logo_little_simple.png")
        Setting.pg.display.set_icon(icon)
        size_x, size_y = size
        gap_increment = size_x / len(self.compiled_arr)
        screen.fill((255, 255, 255))
        y = 0
        color = (255, 0, 0)
        for line in self.compiled_arr :
            x = 0
            for case in line :
                if case == '0' or case == 'False' :
                    color = (0, 0, 0)
                elif case == '1' or case == 'True' :
                    color = (255, 255, 255)
                else :
                    new_case = float(case)
                    if float(case) >= 1 :
                        new_case = 1.0
                    if float(case) <= 0 :
                        new_case = 0.0
                    color = (int(round(255 * new_case, 0)), int(round(255 * new_case, 0)), int(round(255 * new_case, 0)))
                Setting.pg.draw.rect(screen, color, Setting.pg.Rect(x, y, gap_increment, gap_increment))
                x += gap_increment
            Setting.pg.display.flip()
            y += gap_increment
        Setting.pg.display.flip()
        do_exit = False
        while not do_exit:
            for event in Setting.pg.event.get():
                if event.type == Setting.pg.QUIT:
                    return
                if event.type == 768 :
                    self.show(size)
                    Setting.pg.quit()
                    return
        Setting.pg.quit()
        return
