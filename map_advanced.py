#############################
###                       ###
###          MAP          ###
###  ----map_advanced---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

class Info :
    
    from files.info import GetVersion
    version = GetVersion.version
    del GetVersion
    
    import pygame.version as py_version
    
    main_path = __file__.removesuffix("/map_advanced.py")

class Console :
    
    from files.info.console_info import C, A
    
    animation = []
    animation_step = 0
    animation_max_step = 0
    
    def cmd(command_line : str) -> None :
        from os import system
        system(command_line)
    
    def log(text : str, *, start : str = "", end : str = "\n", delete = False, sleep : int | float = 0) -> None :
        from time import sleep as slp
        if delete :
            Console.delete_last_line()
        print(f"{start}{text}" ,end = end)
        slp(sleep)
    
    def color(text : str, color_code : tuple[int, int] = C.INFO, title : str = "") -> str :
        if 0 <= color_code[0] <= 108 and 0 <= color_code[1] <= 108 :
            if title == "" :
                return f"\033[{color_code[1]}m{text}\033[0m"
            else :
                return f"\033[{color_code[0]}m{title}\033[0m\033[{color_code[1]}m : {text}\033[0m"
        else :
            return f"\033[{C.ERROR[0]}mERROR\033[{C.ERROR[1]}m : color code must be between 0 and 108 (current color_code is {color_code[0]} and {color_code[1]})\033[0m"
    
    def animate() -> str :
        Console.animation_step += 1
        if Console.animation_step > Console.animation_max_step :
            Console.animation_step = 0
        return Console.color(Console.animation[Console.animation_step - 1], Console.C.VALID)
    
    def open_animation(animation : list[str]) :
        Console.animation = animation
        Console.animation_step = 0
        Console.animation_max_step = len(animation) - 1
    
    def clear() -> None :
        from os import system
        system("cls")
    
    def delete_last_line() -> None :
        import sys
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    
    clear()

class Generator :
    
    Console.open_animation(Console.A.FILL_R)
    Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.ERROR, "CLASS - GENERATOR"))
    
    from files.generator import Setting
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - data importation", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    is_file_open = False
    opened_file = None
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - create fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def create(low : float = 0.0, high : float = 1.0, size : tuple[int, int] = (4, 4)) -> None :
        from files.generator import NoiseMap
        Generator.opened_file = NoiseMap(low, high, size)
        Generator.is_file_open = True
        return
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - float2bool fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def float2bool(limit : int | float = 0.5) -> None :
        if Generator.is_file_open :
            Generator.opened_file.boolean(limit)
        return
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - float2bin fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def float2bin(limit : int | float = 0.5) -> None :
        if Generator.is_file_open :
            Generator.opened_file.binary(limit)
        return
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - float2string fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def float2string(limit : int | float = 0.5, str1 : str = "-", str2 : str = "#") -> None :
        if Generator.is_file_open :
            Generator.opened_file.string(limit, str1, str2)
        return
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - save fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def save() -> None :
        if Generator.is_file_open :
            Generator.opened_file.compile()
            Generator.opened_file.save()
        return
    
    Console.animation_step = Console.animation_max_step
    Console.log(Console.animate() + " <=> " + Console.color("Init - Finish", Console.C.VALID, "CLASS - GENERATOR"), delete = True)

class Viewer :
    
    Console.open_animation(Console.A.FILL_R)
    Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.ERROR, "CLASS - VIEWER"))
    
    from files.viewer import Setting
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - data importation", Console.C.WARNING, "CLASS - VIEWER"), delete = True)
    
    is_file_open = False
    opened_file = None
    
    Console.animation_step = 7
    Console.log(Console.animate() + " <=> " + Console.color("Init - open fonction", Console.C.WARNING, "CLASS - VIEWER"), delete = True)
    
    def open(path : None | str = None) -> None :
        from files.viewer import File
        Viewer.opened_file = File.open(path)
        if type(Viewer.opened_file) in [object, File] :
            Viewer.is_file_open = True
        else :
            Console.log(Console.color("file failed to open", Console.C.ERROR, "ERROR"))
        return
    
    Console.animation_step = 9
    Console.log(Console.animate() + " <=> " + Console.color("Init - show fonction", Console.C.WARNING, "CLASS - VIEWER"), delete = True)
    
    def show(size : tuple[int, int] = (600, 600)) -> None :
        if Viewer.is_file_open :
            Viewer.opened_file.show(size)
        else :
            Console.log(Console.color("you can't view a file when none is opened", Console.C.WARNING, "Warning"))
        return
    
    Console.animation_step = Console.animation_max_step
    Console.log(Console.animate() + " <=> " + Console.color("Init - Finish", Console.C.VALID, "CLASS - VIEWER"), delete = True)

class GUI :
    
    Console.open_animation(Console.A.FILL_R)
    Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.ERROR, "CLASS - GUI"))
    
    font32 = None
    font25 = None
    font16 = None
    info_font = None
    credit_font = None
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - reload_font fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def reload_font() -> None :
        from pygame import font
        font.init()
        GUI.font32 = font.Font('freesansbold.ttf', 32)
        GUI.font25 = font.Font('freesansbold.ttf', 25)
        GUI.font16 = font.Font('freesansbold.ttf', 16)
        GUI.info_font = font.Font('freesansbold.ttf', 10)
        GUI.credit_font = font.Font('freesansbold.ttf', 10)
        GUI.credit_font.italic = True
        
        Console.log(Console.color("reloaded", Console.C.INFO, "FONT"), start = "\n")
    
    def add_credit(SCREEN : object) -> None :
        import pygame as pg
        GUI.reload_font()
        size_x, size_y = SCREEN.get_size()
        pg.draw.line(SCREEN, (50, 50, 50), (0, size_y - 40), (size_x, size_y - 40), 5)
        credit = GUI.credit_font.render("MAP by JARJARBIN", True, (50, 50, 50))
        info = GUI.info_font.render(f"v{Info.version}", True, (50, 50, 50))
        logo = pg.image.load("files/images/logo_little_advanced.png")
        creditRect = credit.get_rect()
        creditRect.x = 40
        creditRect.y = size_y - creditRect.height - 10
        pg.Surface.blit(SCREEN, credit, creditRect)
        infoRect = info.get_rect()
        infoRect.x = size_x - infoRect.width - 10
        infoRect.y = size_y - infoRect.height - 10
        pg.Surface.blit(SCREEN, info, infoRect)
        logo = pg.transform.scale(logo, (20, 20))
        pg.Surface.blit(SCREEN, logo, (10, size_y - 30))
        pg.display.flip()
        
        Console.log(Console.color("added", Console.C.INFO, "credit"), start = "\n")
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - start fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def start() -> None :
        
        Console.log(Console.color("======================================================================================================", Console.C.INFO))
        
        #Console.cmd('%CMDOW% "MAP - Launcher (advanced)" /hid')
        
        GUI.reload_font()
        next_screen = "exit"
        while True :
            
            Console.log(Console.color("switching screen", Console.C.INFO, "SCREEN"), start = "\n", end = " | ")
            
            GUI.reload_font()
            if next_screen == "exit" :
                from pygame import quit
                quit()
                
                #Console.cmd('%CMDOW% "MAP - Launcher (advanced)" /vis')
                
                Console.log(Console.color("Program stopped", Console.C.ERROR), start = "\n\n", sleep = 2)
                
                return

GUI.start()

"""
#Console.cmd('%CMDOW% "MAP - Launcher (advanced)" /vis')

Console.open_animation(Console.A.FULL)
Console.log(Console.animate() + " <=> " + Console.color("Program closing in 3 (press escape for a second to cancel)", Console.C.ERROR))
Console.open_animation(Console.A.EMPTY_L)

n = 3
escape = False
while n != 0 and not(escape) :
    for _ in range(4) :
        Console.log(Console.color(f"Program closing in {n} (press escape for a second to cancel)", Console.C.ERROR) + " <=> " + Console.animate(), delete = True, sleep = 0.2)
        if is_pressed('escape') :
            escape = True
            break
    n -= 1

if not(escape) :
    for _ in range(2) :
        Console.log(Console.color("Program closing in 0", Console.C.ERROR) + " <=> " + Console.animate(), delete = True, sleep = 0.2)
    Console.log(Console.color("Program closing", Console.C.ERROR) + " <=> " + Console.animate(), delete = True)
else :
    Console.log(Console.color("Program closing cancel (press escape again to close program)", Console.C.ERROR), delete = True)
    while is_pressed('escape') :
        pass
    while not(is_pressed('escape')) :
        pass
"""
