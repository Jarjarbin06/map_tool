#############################
###                       ###
###          MAP          ###
###  ----console_info---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

char = "#"

class C :
    
    ERROR = (41, 31)
    WARNING = (43, 33)
    VALID = (42, 32)
    INFO = (7 ,0)

class A :
    
    SLIDE_R = [
        f"|--------------|",
        f"|{char}-------------|",
        f"|-{char}------------|",
        f"|--{char}-----------|",
        f"|---{char}----------|",
        f"|----{char}---------|",
        f"|-----{char}--------|",
        f"|------{char}-------|",
        f"|-------{char}------|",
        f"|--------{char}-----|",
        f"|---------{char}----|",
        f"|----------{char}---|",
        f"|-----------{char}--|",
        f"|------------{char}-|",
        f"|-------------{char}|"]
    SLIDE_L = [
        f"|--------------",
        f"|-------------{char}|",
        f"|------------{char}-|",
        f"|-----------{char}--|",
        f"|----------{char}---|",
        f"|---------{char}----|",
        f"|--------{char}-----|",
        f"|-------{char}------|",
        f"|------{char}-------|",
        f"|-----{char}--------|",
        f"|----{char}---------|",
        f"|---{char}----------|",
        f"|--{char}-----------|",
        f"|-{char}------------|",
        f"|{char}-------------|"]
    SLIDER_R = [
        f"|{char}{char}{char}{char}----------|",
        f"|-{char}{char}{char}{char}---------|",
        f"|--{char}{char}{char}{char}--------|",
        f"|---{char}{char}{char}{char}-------|",
        f"|----{char}{char}{char}{char}------|",
        f"|-----{char}{char}{char}{char}-----|",
        f"|------{char}{char}{char}{char}----|",
        f"|-------{char}{char}{char}{char}---|",
        f"|--------{char}{char}{char}{char}--|",
        f"|---------{char}{char}{char}{char}-|"]
    SLIDER_L = [
        f"|----------{char}{char}{char}{char}|",
        f"|---------{char}{char}{char}{char}-|",
        f"|--------{char}{char}{char}{char}--|",
        f"|-------{char}{char}{char}{char}---|",
        f"|------{char}{char}{char}{char}----|",
        f"|-----{char}{char}{char}{char}-----|",
        f"|----{char}{char}{char}{char}------|",
        f"|---{char}{char}{char}{char}-------|",
        f"|--{char}{char}{char}{char}--------|",
        f"|-{char}{char}{char}{char}---------|"]
    FILL_R = [
        f"|--------------|",
        f"|{char}-------------|",
        f"|{char}{char}------------|",
        f"|{char}{char}{char}-----------|",
        f"|{char}{char}{char}{char}----------|",
        f"|{char}{char}{char}{char}{char}---------|",
        f"|{char}{char}{char}{char}{char}{char}--------|",
        f"|{char}{char}{char}{char}{char}{char}{char}-------|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}------|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}-----|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}----|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}---|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}--|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}-|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|"]
    FILL_L = [
        f"|--------------|",
        f"|-------------{char}|",
        f"|------------{char}{char}|",
        f"|-----------{char}{char}{char}|",
        f"|----------{char}{char}{char}{char}|",
        f"|---------{char}{char}{char}{char}{char}|",
        f"|--------{char}{char}{char}{char}{char}{char}|",
        f"|-------{char}{char}{char}{char}{char}{char}{char}|",
        f"|------{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|-----{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|----{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|---{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|--{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|-{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|"]
    EMPTY_R = [
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|-{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|--{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|---{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|----{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|-----{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|------{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|-------{char}{char}{char}{char}{char}{char}{char}|",
        f"|--------{char}{char}{char}{char}{char}{char}|",
        f"|---------{char}{char}{char}{char}{char}|",
        f"|----------{char}{char}{char}{char}|",
        f"|-----------{char}{char}{char}|",
        f"|------------{char}{char}|",
        f"|-------------{char}|",
        f"|--------------|"]
    EMPTY_L = [
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}-|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}--|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}---|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}----|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}-----|",
        f"|{char}{char}{char}{char}{char}{char}{char}{char}------|",
        f"|{char}{char}{char}{char}{char}{char}{char}-------|",
        f"|{char}{char}{char}{char}{char}{char}--------|",
        f"|{char}{char}{char}{char}{char}---------|",
        f"|{char}{char}{char}{char}----------|",
        f"|{char}{char}{char}-----------|",
        f"|{char}{char}------------|",
        f"|{char}-------------|",
        f"|--------------|"]
    EMPTY = [
        f"|--------------|"]
    FULL = [
        f"|{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}{char}|"]
