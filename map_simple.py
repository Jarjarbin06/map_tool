#############################
###                       ###
###          MAP          ###
###   ----map_simple----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

class Info :
    
    from files.info import GetVersion
    version = GetVersion.version
    del GetVersion
    
    import pygame.version as py_version
    
    main_path = __file__.removesuffix("\map_simple.py")
    log_path = f"{main_path}\\files\\info\\logs"

class Console :
    
    from files.info.console_info import C, A
    from files.info.logs import logger_program as LOG
    
    status_list = ["test.", "info.", "warn.", "error", "crit.", "user."]
    title_list = ["  test  ", "function", " class  ", " module ", "  file  ", "  user  ", "unknown "]
    
    LOG.init(Info.log_path)
    LOG.log(status_list[1], title_list[3], "logger_program started", Info.log_path)
    
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
    Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "CLASS - GENERATOR"))
    
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
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - smooth fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def smooth(full_around : bool = False) -> None :
        if Generator.is_file_open :
            Generator.opened_file.smooth(full_around)
        return
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - save fonction", Console.C.WARNING, "CLASS - GENERATOR"), delete = True)
    
    def save() -> None :
        if Generator.is_file_open :
            Generator.opened_file.compile()
            Generator.opened_file.save()
        return
    
    Console.animation_step = Console.animation_max_step
    Console.log(Console.animate() + " <=> " + Console.color("Init - Finish", Console.C.VALID, "CLASS - GENERATOR"), delete = True)
    Console.LOG.log(Console.status_list[1], Console.title_list[2], "GENERATOR initialized", Info.log_path)

class Viewer :
    
    Console.open_animation(Console.A.FILL_R)
    Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "CLASS - VIEWER"))
    
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
    Console.LOG.log(Console.status_list[1], Console.title_list[2], "VIEWER initialized", Info.log_path)

class GUI :
    
    Console.open_animation(Console.A.FILL_R)
    Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "CLASS - GUI"))
    
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
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - add_credit fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def add_credit(SCREEN : object) -> None :
        import pygame as pg
        GUI.reload_font()
        size_x, size_y = SCREEN.get_size()
        pg.draw.line(SCREEN, (50, 50, 50), (0, size_y - 40), (size_x, size_y - 40), 5)
        credit = GUI.credit_font.render("MAP by JARJARBIN", True, (50, 50, 50))
        info = GUI.info_font.render(f"v{Info.version}", True, (50, 50, 50))
        logo = pg.image.load("files\\images\\logo_little_simple.png")
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
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - start fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def start() -> None :
        
        Console.log(Console.color("======================================================================================================", Console.C.INFO))
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "GUI started", Info.log_path)
        
        Console.cmd('%CMDOW% "MAP - Launcher" /hid')
        
        GUI.reload_font()
        next_screen = "welcome screen"
        while True :
            
            Console.log(Console.color("switching screen", Console.C.INFO, "SCREEN"), start = "\n", end = " | ")
            
            GUI.reload_font()
            if next_screen == "welcome screen" :
                next_screen = GUI.welcome()
            elif next_screen == "home" :
                next_screen = GUI.home()
            elif next_screen == "generate" :
                next_screen = GUI.generator()
            elif next_screen == "view" :
                next_screen = GUI.view()
            elif next_screen == "credit" :
                next_screen = GUI.credit()
            if next_screen == "exit" :
                from pygame import quit
                quit()
                
                Console.cmd('%CMDOW% "MAP - Launcher" /vis')
                
                Console.log(Console.color("Program stopped", Console.C.ERROR), start = "\n\n", sleep = 2)
                Console.LOG.log(Console.status_list[1], Console.title_list[1], "GUI stopped", Info.log_path)
                
                return
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - welcome fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def welcome() -> str :
        
        Console.open_animation(Console.A.FILL_R)
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "SCREEN - welcome"))
        
        import pygame as pg
        
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules initialization", Console.C.WARNING, "SCREEN - welcome"), delete = True)
        
        pg.init()
        
        Console.animation_step = 4
        Console.log(Console.animate() + " <=> " + Console.color("Window - creation", Console.C.WARNING, "SCREEN - welcome"), delete = True)
        
        size = (500, 300)
        WELCOME = pg.display.set_mode(size)
        pg.display.set_caption("MAP | WELCOME")
        pg.display.set_allow_screensaver(False)
        icon = pg.image.load("files\\images\\logo_little_simple.png")
        pg.display.set_icon(icon)
        size_x, size_y = size
        WELCOME.fill((255, 255, 255))
        pg.display.flip()
        do_exit = False
        x = 50
        y = 50
        
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements creation", Console.C.WARNING, "SCREEN - welcome"), delete = True)
        
        pg.draw.rect(WELCOME, (110, 110, 110), pg.Rect(x - 10, y - 10, 420, 170))
        pg.draw.rect(WELCOME, (130, 130, 130), pg.Rect(x, y, 400, 150))
        pg.draw.line(WELCOME, (110, 110, 110), (x, y + 75), (x + 400, y + 75), 10)
        pg.draw.line(WELCOME, (110, 110, 110), (x + 300, y), (x + 300, y + 150), 10)
        pg.draw.line(WELCOME, (50, 50, 50), (0, size_y - 40), (size_x, size_y - 40), 5)
        text1 = GUI.font32.render("Welcome to MAP", True, (50, 50, 50))
        text2 = GUI.font25.render("A NOISE MAP TOOL", True, (50, 50, 50))
        text3 = GUI.font16.render("press any key to continue", True, (50, 50, 50))
        image = pg.image.load("files\\images\\logo_big_simple.png")
        
        Console.animation_step = 8
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements placement", Console.C.WARNING, "SCREEN - welcome"), delete = True)
        
        text1Rect = text1.get_rect()
        text1Rect.x = x + 10
        text1Rect.y = y + 20
        pg.Surface.blit(WELCOME, text1, text1Rect)
        text2Rect = text2.get_rect()
        text2Rect.x = x + 20
        text2Rect.y = y + 105
        pg.Surface.blit(WELCOME, text2, text2Rect)
        text3Rect = text3.get_rect()
        text3Rect.x = x + 90
        text3Rect.y = y + 170
        pg.Surface.blit(WELCOME, text3, text3Rect)
        image = pg.transform.scale(image, (95, 152))
        pg.Surface.blit(WELCOME, image, (x + 305, y))
        pg.display.flip()
        GUI.add_credit(WELCOME)
        
        Console.animation_step = Console.animation_max_step
        Console.log(Console.animate() + " <=> " + Console.color("Window - ready", Console.C.VALID, "SCREEN - welcome"), delete = True)
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "welcome window opened", Info.log_path)
        
        Console.cmd('%CMDOW% "MAP | WELCOME" /ena /res')
        
        while not do_exit :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "exit"
                if event.type == pg.KEYDOWN :
                    do_exit = True
        
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "welcome window closed", Info.log_path)
        
        return "home"
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - credit fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def credit() -> str :
        
        Console.open_animation(Console.A.FILL_R)
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "SCREEN - credit"), )
        
        import pygame as pg
        
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules initialization", Console.C.WARNING, "SCREEN - credit"), delete = True)
        
        pg.init()
        
        Console.animation_step = 4
        Console.log(Console.animate() + " <=> " + Console.color("Window - creation", Console.C.WARNING, "SCREEN - credit"), delete = True)
        
        size = (500, 300)
        CREDIT = pg.display.set_mode(size)
        pg.display.set_caption("MAP | CREDIT")
        pg.display.set_allow_screensaver(False)
        icon = pg.image.load("files\\images\\logo_little_simple.png")
        pg.display.set_icon(icon)
        size_x, size_y = size
        CREDIT.fill((255, 255, 255))
        pg.display.flip()
        do_exit = False
        x = 10
        y = 10
        
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements creation", Console.C.WARNING, "SCREEN - credit"), delete = True)
        
        pg.draw.line(CREDIT, (50, 50, 50), (0, y + 30), (size_x, y + 30), 5)
        pg.draw.line(CREDIT, (50, 50, 50), (0, size_y - 40), (size_x, size_y - 40), 5)
        text1 = GUI.font16.render("press any key to continue", True, (50, 50, 50))
        credit = GUI.credit_font.render("MAP by JARJARBIN", True, (50, 50, 50))
        credit1 = GUI.font25.render("program by JARJARBIN", True, (50, 50, 50))
        credit2 = GUI.font25.render("logo by JARJARBIN", True, (50, 50, 50))
        credit3 = GUI.font25.render("GUI by JARJARBIN", True, (50, 50, 50))
        credit4 = GUI.font32.render("EVERYTHING BY JARJARBIN", True, (200, 50, 50))
        info = GUI.info_font.render(f"v{Info.version}", True, (50, 50, 50))
        logo = pg.image.load("files\\images\\logo_little_simple.png")
        
        Console.animation_step = 8
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements placement", Console.C.WARNING, "SCREEN - welcome"), delete = True)
        
        text1Rect = text1.get_rect()
        text1Rect.x = (size_x - text1Rect.width) / 2
        text1Rect.y = y
        pg.Surface.blit(CREDIT, text1, text1Rect)
        creditRect = credit.get_rect()
        creditRect.x = 40
        creditRect.y = size_y - creditRect.height - 10
        pg.Surface.blit(CREDIT, credit, creditRect)
        pg.display.flip()
        credit1Rect = credit1.get_rect()
        credit1Rect.x = (size_x - credit1Rect.width) / 2
        credit1Rect.y = y + 40
        pg.Surface.blit(CREDIT, credit1, credit1Rect)
        pg.draw.line(CREDIT, (200, 200, 200), (size_x / 2 - 100, credit1Rect.y + 30), (size_x / 2 + 100, credit1Rect.y + 30), 4)
        credit2Rect = credit2.get_rect()
        credit2Rect.x = (size_x - credit2Rect.width) / 2
        credit2Rect.y = y + 80
        pg.Surface.blit(CREDIT, credit2, credit2Rect)
        pg.draw.line(CREDIT, (200, 200, 200), (size_x / 2 - 100, credit2Rect.y + 30), (size_x / 2 + 100, credit2Rect.y + 30), 4)
        credit3Rect = credit3.get_rect()
        credit3Rect.x = (size_x - credit3Rect.width) / 2
        credit3Rect.y = y + 120
        pg.Surface.blit(CREDIT, credit3, credit3Rect)
        pg.draw.line(CREDIT, (200, 200, 200), (size_x / 2 - 100, credit3Rect.y + 30), (size_x / 2 + 100, credit3Rect.y + 30), 4)
        credit4Rect = credit4.get_rect()
        credit4Rect.x = (size_x - credit4Rect.width) / 2
        credit4Rect.y = y + 180
        pg.Surface.blit(CREDIT, credit4, credit4Rect)
        pg.display.flip()
        infoRect = info.get_rect()
        infoRect.x = size_x - infoRect.width - 10
        infoRect.y = size_y - infoRect.height - 10
        pg.Surface.blit(CREDIT, info, infoRect)
        logo = pg.transform.scale(logo, (20, 20))
        pg.Surface.blit(CREDIT, logo, (10, size_y - 30))
        pg.display.flip()
        
        Console.animation_step = Console.animation_max_step
        Console.log(Console.animate() + " <=> " + Console.color("Window - ready", Console.C.VALID, "SCREEN - credit"), delete = True)
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "credit window opened", Info.log_path)
        
        Console.cmd('%CMDOW% "MAP | CREDIT" /ena /res')
        
        while not do_exit :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "exit"
                if event.type == pg.KEYDOWN :
                    do_exit = True
        
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "credit window closed", Info.log_path)
        
        return "home"
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - home fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def home() -> str :
        
        Console.open_animation(Console.A.FILL_R)
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "SCREEN - home"), )
        
        import pygame as pg
        
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules initialization", Console.C.WARNING, "SCREEN - home"), delete = True)
        
        pg.init()
        
        Console.animation_step = 4
        Console.log(Console.animate() + " <=> " + Console.color("Window - creation", Console.C.WARNING, "SCREEN - home"), delete = True)
        
        buttons = ["generate", "view", "welcome screen", "credit", "exit"]
        selected_button = 0
        buttons_info = {
            "generate" : {"selected?" : True, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
            "view" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
            "welcome screen" : {"selected?" : False, "color" : (100, 100, 100), "bg1" : (80, 80, 80), "bg2" : (0, 0, 0)},
            "credit" : {"selected?" : False, "color" : (100, 100, 100), "bg1" : (80, 80, 80), "bg2" : (0, 0, 0)},
            "exit" : {"selected?" : False, "color" : (200, 150, 150), "bg1" : (200, 110, 110), "bg2" : (100, 50, 50)}
                  }
        do_exit = False
        is_up_pressed = False
        is_down_pressed = False
        is_enter_pressed = False
        update = True
        choosen = False
        size = (520, (100 * len(buttons)) + 80)
        size_x, size_y = size
        HOME = pg.display.set_mode(size)
        HOME.fill((255, 255, 255))
        pg.display.set_caption("MAP | HOME")
        pg.display.set_allow_screensaver(False)
        icon = pg.image.load("files\\images\\logo_little_simple.png")
        pg.display.set_icon(icon)
        
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements creation", Console.C.WARNING, "SCREEN - home"), delete = True)
        
        loading = GUI.font16.render("Loading ...", True, (150, 150, 150))
        
        Console.animation_step = 8
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements placement", Console.C.WARNING, "SCREEN - home"), delete = True)
        
        loadingRect = loading.get_rect()
        loadingRect.x = (size_x - loadingRect.width) / 2
        loadingRect.y = (size_y - loadingRect.height) / 2
        pg.Surface.blit(HOME, loading, loadingRect)
        pg.display.flip()
        GUI.add_credit(HOME)
        
        Console.animation_step = Console.animation_max_step
        Console.log(Console.animate() + " <=> " + Console.color("Window - ready", Console.C.VALID, "SCREEN - home"), delete = True)
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "home window opened", Info.log_path)
        
        Console.cmd('%CMDOW% "MAP | HOME" /ena /res')
        
        while not do_exit :
            if selected_button < 0 :
                selected_button = len(buttons) - 1
            if selected_button > len(buttons) - 1 :
                selected_button = 0
            if update :
                if choosen :
                    if buttons[selected_button] == "exit" :
                        pg.quit()
                    do_exit = True
                    choosen = False
                else :
                    x = 100
                    y = 20
                    for button in buttons :
                        if button == buttons[selected_button] :
                            pg.draw.rect(HOME, buttons_info[button]["bg2"], pg.Rect(x - 30, y, 350, 80))
                            text = GUI.font32.render(button, True, buttons_info[button]["bg2"])
                        else :
                            pg.draw.rect(HOME, (255, 255, 255), pg.Rect(x - 30, y, 350, 80))
                            pg.draw.rect(HOME, buttons_info[button]["bg1"], pg.Rect(x, y, 320, 80))
                            text = GUI.font32.render(button, True, buttons_info[button]["bg1"])
                        pg.display.flip()
                        pg.draw.rect(HOME, buttons_info[button]["color"], pg.Rect(x + 10, y + 10, 300, 60))
                        textRect = text.get_rect()
                        textRect.x = x + 15
                        textRect.y = y + 10
                        pg.Surface.blit(HOME, text, textRect)
                        y += 100
                    pg.display.flip()
                update = False
            if not do_exit :
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        return "exit"
                    if event.type == pg.KEYDOWN :
                        if event.dict['key'] == pg.K_UP and not is_up_pressed :
                            is_up_pressed = True
                            selected_button -= 1
                            update = True
                        if event.dict['key'] == pg.K_DOWN and not is_down_pressed :
                            is_down_pressed = True
                            selected_button += 1
                            update = True
                        if event.dict['key'] == pg.K_RETURN and not is_enter_pressed :
                            is_enter_pressed = True
                            choosen = True
                            update = True
                    if event.type == pg.KEYUP :
                        if event.dict['key'] == pg.K_UP and is_up_pressed :
                            is_up_pressed = False
                        if event.dict['key'] == pg.K_DOWN and is_down_pressed :
                            is_down_pressed = False
                        if event.dict['key'] == pg.K_RETURN and is_enter_pressed :
                            is_enter_pressed = False
        
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "home window closed", Info.log_path)
        
        return buttons[selected_button]
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - view fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def view() -> str :
        
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "viewer window opened", Info.log_path)
        
        Viewer.open()
        Viewer.show((1000, 1000))
        
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "viewer window closed", Info.log_path)
        
        return "home"
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - generator fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def generator() -> str :
        
        Console.open_animation(Console.A.FILL_R)
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules importation", Console.C.WARNING, "SCREEN - generaor"))
        
        import pygame as pg
        from files import generator as gen
        
        Console.log(Console.animate() + " <=> " + Console.color("Init - modules initialization", Console.C.WARNING, "SCREEN - generator"), delete = True)
        
        pg.init()
        
        Console.animation_step = 4
        Console.log(Console.animate() + " <=> " + Console.color("Window - creation", Console.C.WARNING, "SCREEN - generator"), delete = True)
        
        settings = ["limit", "size", "next", "exit"]
        settings_values = [0.5, 20, None, None]
        selected_setting = 0
        settings_info = {
            "limit" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
            "size" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
            "next" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
            "exit" : {"selected?" : False, "color" : (200, 150, 150), "bg1" : (200, 110, 110), "bg2" : (100, 50, 50)}
                }
        do_exit = False
        is_up_pressed = False
        is_down_pressed = False
        is_enter_pressed = False
        choosen = False
        update = True
        size = (520, (100 * len(settings)) + 80)
        size_x, size_y = size
        GENERATOR = pg.display.set_mode(size)
        pg.display.set_caption("MAP | GENERATOR")
        pg.display.set_allow_screensaver(False)
        icon = pg.image.load("files\\images\\logo_little_simple.png")
        pg.display.set_icon(icon)
        GENERATOR.fill((255, 255, 255))
        pg.display.flip()
        mod = None
        
        Console.animation_step = 8
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements placement", Console.C.WARNING, "SCREEN - generator"), delete = True)
        
        GUI.add_credit(GENERATOR)
        
        Console.animation_step = Console.animation_max_step
        Console.log(Console.animate() + " <=> " + Console.color("Window - ready", Console.C.VALID, "SCREEN - generator"), delete = True)
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "generator window opened", Info.log_path)
        
        Console.cmd('%CMDOW% "MAP | GENERATOR" /ena /res')
        
        while not do_exit :
            if selected_setting < 0 :
                selected_setting = len(settings) - 1
            if selected_setting > len(settings) - 1 :
                selected_setting = 0
            if update :
                if choosen :
                    if settings[selected_setting] == "next" :
                        map_size = (settings_values[settings.index("size")], settings_values[settings.index("size")])
                        map_limit = settings_values[settings.index("limit")]
                        settings = ["smooth", "boolean", "binary", "string", "save", "exit"]
                        settings_values = [False, None, None, None, None, None]
                        selected_setting = 0
                        settings_info = {
                            "smooth" : {"selected?" : True, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
                            "boolean" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
                            "binary" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
                            "string" : {"selected?" : False, "color" : (150, 150, 150), "bg1" : (110, 110, 110), "bg2" : (50, 50, 50)},
                            "save" : {"selected?" : False, "color" : (100, 100, 100), "bg1" : (80, 80, 80), "bg2" : (0, 0, 0)},
                            "exit" : {"selected?" : False, "color" : (200, 150, 150), "bg1" : (200, 110, 110), "bg2" : (100, 50, 50)}
                                }
                        selected_setting = 0
                        choosen = False
                    elif settings[selected_setting] == "boolean" :
                        mod = "bool"
                        settings = ["save", "exit"]
                        settings_values = [None, None]
                        selected_setting = 0
                        settings_info = {
                            "save" : {"selected?" : False, "color" : (100, 100, 100), "bg1" : (80, 80, 80), "bg2" : (0, 0, 0)},
                            "exit" : {"selected?" : False, "color" : (200, 150, 150), "bg1" : (200, 110, 110), "bg2" : (100, 50, 50)}
                                }
                        selected_setting = 0
                        choosen = False
                    elif settings[selected_setting] == "binary" :
                        mod = "bin"
                        settings = ["save", "exit"]
                        settings_values = [None, None]
                        selected_setting = 0
                        settings_info = {
                            "save" : {"selected?" : False, "color" : (100, 100, 100), "bg1" : (80, 80, 80), "bg2" : (0, 0, 0)},
                            "exit" : {"selected?" : False, "color" : (200, 150, 150), "bg1" : (200, 110, 110), "bg2" : (100, 50, 50)}
                                }
                        selected_setting = 0
                        choosen = False
                    elif settings[selected_setting] == "string" :
                        mod = "str"
                        settings = ["save", "exit"]
                        settings_values = [None, None]
                        selected_setting = 0
                        settings_info = {
                            "save" : {"selected?" : False, "color" : (100, 100, 100), "bg1" : (80, 80, 80), "bg2" : (0, 0, 0)},
                            "exit" : {"selected?" : False, "color" : (200, 150, 150), "bg1" : (200, 110, 110), "bg2" : (100, 50, 50)}
                                }
                        selected_setting = 0
                        choosen = False
                    elif settings[selected_setting] == "limit" :
                        settings_values[settings.index("limit")] = GUI.select_val(settings_values[settings.index("limit")], 0.01, 0, 1, "LIMIT")
                        choosen = False
                    elif settings[selected_setting] == "size" :
                        settings_values[settings.index("size")] = GUI.select_val(settings_values[settings.index("size")], 10, 10, 1000, "SIZE")
                        choosen = False
                    elif settings[selected_setting] == "smooth" :
                        settings_values[settings.index("smooth")] = bool(GUI.select_val(int(settings_values[settings.index("smooth")]), 1, 0, 1, "SMOOTH"))
                        Generator.smooth(settings_values[settings.index("smooth")])
                        choosen = False
                    elif settings[selected_setting] == "save" :
                        new_map = gen.NoiseMap(size = map_size)
                        if mod == "bool" :
                            new_map.boolean(map_limit)
                        if mod == "bin" :
                            new_map.binary(map_limit)
                        if mod == "str" :
                            new_map.string(map_limit)
                        new_map.compile()
                        #new_map.name = ""
                        new_map.save()
                        
                        Console.log(Console.color("\n--------------------", Console.C.VALID))
                        Console.log(Console.color(f"\n    {new_map.file.name} in {new_map.file.path}\n\n    additional info :\n        - boolean = {new_map.is_bool}\n        - binary = {new_map.is_bin}\n        - string = {new_map.is_str}\n        - size = {map_size}", Console.C.VALID, "file saved"))
                        Console.log(Console.color("--------------------", Console.C.VALID))
                        
                        choosen = False
                        pg.quit()
                        do_exit = True
                    elif settings[selected_setting] == "exit" :
                        pg.quit()
                        do_exit = True
                        choosen = False
                    size = (520, (100 * len(settings)) + 90)
                    size_x, size_y = size
                    GENERATOR = pg.display.set_mode(size)
                    pg.display.set_caption("MAP | GENERATOR")
                    pg.display.set_allow_screensaver(False)
                    icon = pg.image.load("files\\images\\logo_little_simple.png")
                    pg.display.set_icon(icon)
                    GENERATOR.fill((255, 255, 255))
                    pg.display.flip()
                    GUI.add_credit(GENERATOR)
                    x = 100
                    y = 20
                    for setting in settings :
                        if setting == settings[selected_setting] :
                            pg.draw.rect(GENERATOR, settings_info[setting]["bg2"], pg.Rect(x - 10, y, 330, 80))
                            text = GUI.font32.render(setting, True, settings_info[setting]["bg2"])
                        else :
                            pg.draw.rect(GENERATOR, (255, 255, 255), pg.Rect(x - 10, y, 330, 80))
                            pg.draw.rect(GENERATOR, settings_info[setting]["bg1"], pg.Rect(x, y, 320, 80))
                            text = GUI.font32.render(setting, True, settings_info[setting]["bg1"])
                        pg.display.flip()
                        pg.draw.rect(GENERATOR, settings_info[setting]["color"], pg.Rect(x + 10, y + 10, 300, 60))
                        textRect = text.get_rect()
                        textRect.x = x + 15
                        textRect.y = y + 10
                        pg.Surface.blit(GENERATOR, text, textRect)
                        y += 100
                    pg.display.flip()
                else :
                    x = 100
                    y = 20
                    for setting in settings :
                        if setting == settings[selected_setting] :
                            pg.draw.rect(GENERATOR, settings_info[setting]["bg2"], pg.Rect(x - 10, y, 330, 80))
                            text = GUI.font32.render(setting, True, settings_info[setting]["bg2"])
                        else :
                            pg.draw.rect(GENERATOR, (255, 255, 255), pg.Rect(x - 10, y, 330, 80))
                            pg.draw.rect(GENERATOR, settings_info[setting]["bg1"], pg.Rect(x, y, 320, 80))
                            text = GUI.font32.render(setting, True, settings_info[setting]["bg1"])
                        pg.display.flip()
                        pg.draw.rect(GENERATOR, settings_info[setting]["color"], pg.Rect(x + 10, y + 10, 300, 60))
                        textRect = text.get_rect()
                        textRect.x = x + 15
                        textRect.y = y + 10
                        pg.Surface.blit(GENERATOR, text, textRect)
                        y += 100
                    pg.display.flip()
                update = False
            if not do_exit :
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        return "exit"
                    if event.type == pg.KEYDOWN :
                        if event.dict['key'] == pg.K_UP and not is_up_pressed :
                            is_up_pressed = True
                            selected_setting -= 1
                            update = True
                        if event.dict['key'] == pg.K_DOWN and not is_down_pressed :
                            is_down_pressed = True
                            selected_setting += 1
                            update = True
                        if event.dict['key'] == pg.K_RETURN and not is_enter_pressed :
                            is_enter_pressed = True
                            choosen = True
                            update = True
                    if event.type == pg.KEYUP :
                        if event.dict['key'] == pg.K_UP and is_up_pressed :
                            is_up_pressed = False
                        if event.dict['key'] == pg.K_DOWN and is_down_pressed :
                            is_down_pressed = False
                        if event.dict['key'] == pg.K_RETURN and is_enter_pressed :
                            is_enter_pressed = False
        
        Console.LOG.log(Console.status_list[1], Console.title_list[1], "generator window closed", Info.log_path)
        
        return "home"
    
    Console.log(Console.animate() + " <=> " + Console.color("Init - select_val fonction", Console.C.WARNING, "CLASS - GUI"), delete = True)
    
    def select_val(current_limit : int | float, step : int | float, low : int | float, high : int | float, name : str) -> float :
        
        Console.log(Console.color(f"{name} selector opened", Console.C.INFO, "SCREEN - select_val"))
        Console.LOG.log(Console.status_list[1], Console.title_list[1], f"{name} selector window opened", Info.log_path)
        
        import pygame as pg
        from files import generator as gen
        from time import sleep
        do_exit = False
        is_left_pressed = False
        is_right_pressed = False
        is_enter_pressed = False
        update = True
        new_limit = current_limit
        size = (500, 300)
        size_x, size_y = size
        pg.init()
        LIMIT = pg.display.set_mode(size)
        pg.display.set_caption(f"MAP | GENERATOR | {name} SELECTOR")
        pg.display.set_allow_screensaver(False)
        icon = pg.image.load("files\\images\\logo_little_simple.png")
        pg.display.set_icon(icon)
        LIMIT.fill((255, 255, 255))
        pg.display.flip()
        
        Console.animation_step = 8
        Console.log(Console.animate() + " <=> " + Console.color("Window - elements placement", Console.C.WARNING, "SCREEN - generator"), delete = True)
        
        GUI.add_credit(LIMIT)
        
        Console.cmd(f'%CMDOW% "MAP | GENERATOR | {name} SELECTOR" /ena /res')
        
        while not do_exit :
            if update :
                LIMIT.fill((255, 255, 255))
                GUI.add_credit(LIMIT)
                text = GUI.font32.render(str(new_limit), True, (210, 210, 210))
                textRect = text.get_rect()
                textRect.x = (size_x-textRect.width)//2
                textRect.y = (size_y-textRect.height)//2
                pg.Surface.blit(LIMIT, text, textRect)
                pg.display.flip()
                update = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return current_limit
                if event.type == pg.KEYDOWN :
                    if event.dict['key'] == pg.K_LEFT :
                        is_left_pressed = True
                    if event.dict['key'] == pg.K_RIGHT :
                        is_right_pressed = True
                    if event.dict['key'] == pg.K_RETURN and not is_enter_pressed :
                        is_enter_pressed = True
                        do_exit = True
                        update = True
                elif event.type == pg.KEYUP :
                    if event.dict['key'] == pg.K_LEFT and is_left_pressed :
                        is_left_pressed = False
                    if event.dict['key'] == pg.K_RIGHT and is_right_pressed :
                        is_right_pressed = False
                    if event.dict['key'] == pg.K_RETURN and is_enter_pressed :
                        is_enter_pressed = False
            if is_left_pressed :
                sleep(0.1)
                new_limit -= step
                update = True
            if is_right_pressed :
                sleep(0.1)
                new_limit += step
                update = True
            new_limit = round(new_limit, 2)
            if new_limit < low :
                new_limit = low
            if new_limit > high :
                new_limit = high
                
        Console.log(Console.color(f"{name} selector closed", Console.C.INFO, "SCREEN - select_val"))
        Console.LOG.log(Console.status_list[1], Console.title_list[1], f"{name} selector window closed", Info.log_path)
        
        return new_limit
    
    Console.animation_step = Console.animation_max_step
    Console.log(Console.animate() + " <=> " + Console.color("Init - Finish", Console.C.VALID, "CLASS - GUI"), delete = True)
    Console.LOG.log(Console.status_list[1], Console.title_list[2], "GUI initialized", Info.log_path)

GUI.start()

Console.cmd('%CMDOW% "MAP - Launcher" /vis')

from keyboard import is_pressed

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
    Console.LOG.log(Console.status_list[2], Console.title_list[4], "Program closed", Info.log_path)
else :
    Console.log(Console.color("Program closing cancel (press escape again to close program)", Console.C.ERROR), delete = True)
    Console.LOG.log(Console.status_list[1], Console.title_list[5], "Program closing cancelled", Info.log_path)
    while is_pressed('escape') :
        pass
    while not(is_pressed('escape')) :
        pass
