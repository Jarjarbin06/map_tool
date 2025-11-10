## event_logger ##
## by JARJARBIN'S STUDIO ##

"""
    Python Version: 3.13\n
    File name: logger.py\n
    Author: Jarjarbin's Studio\n
    Description:\n
"""

dt_module_active : bool = True
try : import datetime as dt
except ModuleNotFoundError : dt_module_active = False

os_module_active : bool = True
try : import os
except ModuleNotFoundError : os_module_active = False

tb_module_active : bool = True
try : import traceback as tb
except ModuleNotFoundError : tb_module_active = False

log_start_time : str
log_path : str

def create(
        path : str
        ) -> None :
    """create log file

    Args:
        path (str): path to the log folder
    """

    global dt_module_active, os_module_active, tb_module_active
    global log_start_time, log_path

    assert dt_module_active, "Error: datetime module not found, some functionalities will be disabled"

    log_path = path
    log_start_time = str(dt.datetime.now()).replace(":", "_")

    with open("{}/{}.txt".format(path, log_start_time), 'a') as log_file :
        log_file.write("   date          time      | [type.] category | detail\n\n---START---")
    log_file.close()

def log(
        log_status : str,
        log_title : str,
        log_description : str
        ) -> None :
    """format then save a log

    Args:
        log_status (str): status/type of the log
        log_title (str): category of the log
        log_description (str): information and detail of the log
    """

    assert dt_module_active, "Error: log function cannot be used without datetime module, log can not be save"
    assert isinstance(log_status, str), "Error: log_status must be a string"
    assert len(log_status) == 5, "Error: log_status must have a length of 5 characters"
    assert isinstance(log_title, str), "Error: log_title must be a string"
    assert len(log_title) == 8, "Error: log_title must have a length of 8 characters"
    assert isinstance(log_description, str), "Error: log_description must be a string"

    log_time : str = str(dt.datetime.now())
    log_str : str = f"{log_time} | [{log_status}] {log_title} | {log_description}"

    save(log_str)

def multiple_log(
        log_list : list[tuple[str, str, str]]
        )  -> None:
    """format then save logs

    Args:
        log_list (list[tuple[str, str, str]]): list of logs,
            a log is a tuple of the status/type of the log,
            the category of the log,
            the information and detail of the log
    """

    assert dt_module_active, "Error: multiple_save function cannot be used without datetime module, logs can not be save"
    assert isinstance(log_list, list), "Error: log must be a list"
    for log_idx in range(len(log_list)) :
        assert isinstance(log_list[log_idx], tuple), f"Error: log at index {log_idx} must be a tuple"
        assert len(log_list[log_idx]) == 3, "Error: log must have three elements"
        assert isinstance(log_list[log_idx][0], str), f"Error: log_status of log at index {log_idx} must be a tuple"
        assert len(log_list[log_idx][0]) == 5, f"Error: log_status of log at index {log_idx} must have a length of 5 characters"
        assert isinstance(log_list[log_idx][1], str), f"Error: log_title of log at index {log_idx} must be a tuple"
        assert len(log_list[log_idx][1]) == 8, f"Error: log_title of log at index {log_idx} must have a length of 8 characters"
        assert isinstance(log_list[log_idx][2], str), f"Error: log_description of log at index {log_idx} must be a tuple"

    logs_list : list[str | None] = [None]
    log_time : str = str(dt.datetime.now())
    count : int = 1

    for log_item in log_list :
        log_status, log_title, log_description = log_item
        log_str : str = f"{log_time} | [{log_status}] {log_title} | {log_description}"
        if logs_list[-1] == log_str : count += 1
        else :
            if count == 1 : logs_list.append(log_str)
            else :
                prev_log = logs_list[-1]
                del logs_list[-1]
                logs_list.append(f"{prev_log} [X{count}]")
                logs_list.append(log_str)
                count = 1

    logs_list.remove(None)

    multiple_save(logs_list)

def save(
        log_str : str
        ) :
    """save a log

    Args:
        log_str (str): formated log
    """

    assert dt_module_active, "Error: save function cannot be used without datetime module, log can not be save"
    assert isinstance(log_str, str), "Error: log_str must be a string"

    with open(f"{log_path}/{log_start_time}.txt", 'a') as log_file :
        log_file.write(f"\n{log_str}")
    log_file.close()

def multiple_save(
        log_list : list[str]
        ) :
    """save logs

    Args:
        log_list (list[str]): list of formated logs
    """

    assert dt_module_active, "Error: multiple_save function cannot be used without datetime module, logs can not be save"
    assert isinstance(log_list, list), "Error: log must be a list"
    for log_idx in range(len(log_list)) :
        assert isinstance(log_list[log_idx], str), f"Error: log at index {log_idx} must be a str"
    for log_idx in range(len(log_list)):
        assert isinstance(log_list[log_idx], str), f"Error: log at index {log_idx} must be a str"

    with open(f"{log_path}/{log_start_time}.txt", 'a') as log_file :
        for log_str in log_list : log_file.write(f"\n{log_str}")
    log_file.close()

def log_end(
        ) -> None :
    """mark the end of a log file
    """

    with open(f"{log_path}/{log_start_time}.txt", 'a') as log_file :
        log_file.write(f"\n----END----\n")
    log_file.close()

def read(
        ) -> str :
    """return a string of the content of the log-file

    Returns:
        str: the content of the log-file
    """

    log_str : str

    with open(f"{log_path}/{log_start_time}.txt", 'r') as log_file:
        log_str = log_file.read()
    log_file.close()

    return log_str

def show(
        log_str : str | None = None,

        *,
        show_all : bool = False
        ) -> None :
    """show a reformated version of the log-file

    Args:
        log_str (str | None): the content of the log-file,
            if None then log_str will be set to the result of read() (defaults to None)
    """

    assert isinstance(log_str, (str, None)), f"Error: log_str must be a string"
    assert ("---START---\n" in log_str and "----END----\n" in log_str) and log_str.index("---START---\n") < log_str.index("----END----\n"), "Error: log_str is of a wrong format"

    log_str: str

    if not log_str :
        log_str = read()

    color_dict: dict = {
        "[INFO.]" : ("\033[37m", "\033[7m"),
        "[WARN.]" : ("\033[33m", "\033[43m"),
        "[ERROR]" : ("\033[31m", "\033[41m"),
    }
    color : tuple[str, str]
    start : int = log_str.index("---START---\n") + len("---START---\n")
    end : int = log_str.index("----END----\n")
    logs : list = [lines.split(" | ") for lines in log_str[start:end].splitlines()]
    t_size = os.get_terminal_size()
    header1 : str = "\033[4m\033[7m|\033[0m\033[1m\033[4m    date          time      | \033[0m\033[4m\033[7m[type.]\033[0m\033[1m\033[4m category | detail"
    header2 : str = "\033[7m|\033[0m\033[1m"
    ender : str = "\033[4m\033[7m|\033[0m\033[1m\033[4m"
    detail_size : int

    assert 56 < t_size.columns, "Error: terminal size is too small"
    assert 1 < t_size.columns, "Error: terminal size is too small"

    print(header1, end = "")
    detail_size = (t_size.columns - 56)
    for _ in range(detail_size) :
        print(" ", end = "")
    print("\033[0m")

    print(header2, end="")
    detail_size = (t_size.columns - 1)
    for _ in range(detail_size):
        print(" ", end="")
    print("\033[0m")

    for log_line in logs :
        assert len(log_line) in [1, 3], f"Error: log is of a wrong format ({log_line})"
        assert len(log_line[0]) >= 3, f"Error: first element of log is of a wrong format ({log_line[0]})"

        if log_line[0][:3] == ">>>" :
            print(f"\033[7m>>>\033[0m \033[37m{log_line[0][3:]}\033[0m")
        else :
            assert len(log_line[0]) == 26, f"Error: log_timestamp is of a wrong format ({log_line[0]})"
            assert log_line[1][:7].upper() in color_dict, f"Error: format title is not valid ({log_line[1][:7].upper()})"

            color = color_dict[log_line[1][:7].upper()]
            print(f"{color[1]}|\033[0m ", end = "")
            print(f"{color[0]}{log_line[0]}\033[0m | ", end = "")
            print(f"{color[1]}{log_line[1][0:7]}\033[0m ", end = "")
            print(f"{color[0]}{log_line[1][8:]}\033[0m | ", end = "")

            if len(log_line[2]) > detail_size :
                print(f"{log_line[2][:detail_size]}...")
            else:
                print(f"{color[0]}{log_line[2]}\033[0m")

    print(ender, end = "")
    detail_size = (t_size.columns - 1)
    for _ in range(detail_size):
        print(" ", end="")
    print("\033[0m")

#execute to see log file in terminal
if __name__ == '__main__' :
    try:
        log_path, log_start_time = "files/info/logs", "2025-11-07 18_00_00.067346"
        show(read())
    except AssertionError as err : print(err); exit(84)
    except Exception as err : print(f"unexpected error :\n{''.join(tb.format_exception(None, err, err.__traceback__))}"); exit(84)
    else : exit(0)
