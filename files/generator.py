#############################
###                       ###
###          MAP          ###
###   ----generator----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

class Setting :
    
    """
        Import modules and set initial settings values
    """
    
    import scipy.ndimage.interpolation as inter
    import numpy as np
    import sys
    import os
    import socket
    import tkinter as tk
    from tkinter import filedialog
    from datetime import datetime
    user = os.getlogin()
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    main_path = __file__.removesuffix("\\generator.py").replace("\\", "/")

class Transform :
    
    """
        Manipulate NoiseMap array (parent is Noisemap)
    """

    def boolean(self : object, limit : float = 0.5) -> None :
        
        """
            Convert float values in the array in boolean values

            Parameters:
                - self (object) : NoiseMap
                - limit (float) = 0.5 : limit when the value pass from False to True
        """
        
        if self.is_bin or self.is_str :
            return
        self.arr = self.arr > limit
        self.is_bool = True
        return
    
    def binary(self : object, limit : float = 0.5) -> None :
        
        """
            Convert float values in the array in binary values

            Parameters:
                - self (object) : NoiseMap
                - limit (float) = 0.5 : limit when the value pass from 0 to 1
        """
        
        if self.is_bool or self.is_str :
            return
        self.boolean(limit)
        self.arr = Setting.np.where(self.arr, 0, 1)
        self.is_bin = True
        return
    
    def string(self : object, limit : float = 0.5, str1 : str = "-", str2 : str = "#") -> None :
        
        """
            Convert float values in the array in boolean values

            Parameters:
                - self (object) : NoiseMap
                - limit (float) = 0.5 : limit when the value pass from str1 to str2
                - str1 (str) = "-" : string to replace array value when under the limit
                - str2 (str) = "#" : string to replace array value when above the limit
        """
        
        if self.is_bool or self.is_bin :
            return
        self.boolean(limit)
        self.arr = Setting.np.where(self.arr, str1, str2)
        self.is_str = True
        return
    
    def smooth(self : object, full_around : bool = False) -> None :
        arr_copy = self.arr.tolist()
        for y in range(len(arr_copy)) :
            for x in range(len(arr_copy[y])) :
                cases = [arr_copy[y][x]]
                try :
                    cases.append(arr_copy[y-1][x])
                except IndexError :
                    pass
                try :
                    cases.append(arr_copy[y][x-1])
                except IndexError :
                    pass
                try :
                    cases.append(arr_copy[y+1][x])
                except IndexError :
                    pass
                try :
                    cases.append(arr_copy[y][x+1])
                except IndexError :
                    pass
                if full_around :
                    try :
                        cases.append(arr_copy[y-1][x-1])
                    except IndexError :
                        pass
                    try :
                        cases.append(arr_copy[y+1][x-1])
                    except IndexError :
                        pass
                    try :
                        cases.append(arr_copy[y+1][x+1])
                    except IndexError :
                        pass
                    try :
                        cases.append(arr_copy[y-1][x+1])
                    except IndexError :
                        pass
                av_case = 0
                for case in cases :
                    av_case += case
                av_case = av_case/len(cases)
                self.arr[y][x] = Setting.np.float64(av_case)
        Setting.np.float64(0.1)
    
    def de_amplify(self : object) -> None :
        return #de-amplify array values

class File :
    
    """
        Manipulate Noisemap file (parent is NoiseMap)
    """
    
    def __init__(self : object, data_info : list, data_compiled : list, *, file_name : str = "") -> None :
        
        """
            Create File

            Parameters:
                - self (object) : File
                - data_info (list) : information about the NoiseMap (format : "[date] [time]*[username]*[ip]*[hostname]")
                - data_compiled (list) : NoiseMap array converted into 2d list
                - file_name (str, optional) = "" : File name ( if file_name is "", File name is choosen automaticaly)
        """
        
        self.data = [f"{Setting.datetime.now()}*{data_info}"] + data_compiled
        if file_name == "" :
            file_name = data_info.split("*")[0].replace(".", "_")
        self.path = ""
        root = Setting.tk.Tk()
        root.withdraw()
        self.path = Setting.filedialog.askdirectory(initialdir=Setting.main_path + "/generated_maps")
        self.name = file_name
        return
    
    def __str__(self : object) -> str :
        
        """
            Return string of info

            Parameters:
                - self (object) : File

            Returns:
                - str : (format : "[file_name] by [username] the [date] [time]")
        """
        
        date = self.data[0].split("*")[0]
        data = self.data[0].split("*")[1]
        return f"{self.name} by {data} the {date}"
    
    def compile(self : object) -> None :
        
        """
            Convert NoiseMap array to 2d list and create a File from it

            Parameters:
                - self (object) : NoiseMap
        """
        
        data_info = f"{Setting.user}*{Setting.IPAddr}*{Setting.hostname}"
        data_compiled = self.arr.tolist()
        self.file = File(data_info, data_compiled)
        return
    
    def save(self : object) -> None :
        
        """
            Save File on computer

            Parameters:
                - self (object) : NoiseMap
        """
        
        while not self.file.path :
            self.file.path = Setting.filedialog.askdirectory(initialdir=Setting.main_path + "/generated_maps")
        file_list = Setting.os.listdir(self.file.path)
        if f"{self.file.name}.txt" in file_list :
            count = 1
            while f"{self.file.name}({count}).txt" in file_list :
                count += 1
            self.file.name = f"{self.file.name}({count})"
        try :
            with open(f"{self.file.path}/{self.file.name}.txt", "x") as new_file:
                for line in self.file.data :
                    new_file.write(f"{line}\n")
            new_file.close()
        except FileExistsError :
            print(f"fail to save {self.file.name} in {self.file.path}")
        return        

class NoiseMap(Transform, File) :
    
    """
        Noisemap file (parent of Transorm and File)
    """
    
    def __init__(self : object, low : float = 0.0, high : float = 1.0, size : tuple[int, int] = (20, 20)) -> None :
        
        """
            Create NoiseMap

            Parameters:
                - self (object) : NoiseMap
                - low (float) = 0.0 : lowest possible value in array
                - high (float) = 1.0 : highest possible value in array
                - size (tuple[int, int]) = (20, 20) : size of the array
        """
        
        Setting.np.set_printoptions(threshold=Setting.sys.maxsize)
        self.arr = Setting.np.random.uniform(low, high, size)
        self.file = None
        self.is_bool = False
        self.is_bin = False
        self.is_str = False
        return
    
    def __str__(self : object) -> str :
        
        """
            Return string of array

            Parameters:
                - self (object) : NoiseMap

            Returns:
                - str : string of array
        """
        
        arr_str = Setting.np.array_str(self.arr, max_line_width=500)
        return arr_str
