## event_logger ##
## by JARJARBIN'S STUDIO ##

def init(path : str) :
    """init logger module

    Args:
        path (str): path to the log folder
    """
    global log
    global datetime
    global datetime_module_active
    global session_start_time
    try :
        import datetime
    except ModuleNotFoundError :
        print("[module error : datetime module not found]\n[some fonctionnalities will be disabled]")
        datetime_module_active = False
    else :
        datetime_module_active = True
    if datetime_module_active :
        session_start_time = str(datetime.datetime.now())
        with open("{}\\{}.txt".format(path, session_start_time.replace(":", "_")), 'a') as log_file :
            log_file.write("   date          time      | [type.] category | information : detail\n")
        log_file.close()
    else :
        pass
    return

def log(log_status : str, log_title : str, log_description : str, path : str) :
    """encrypt and save 1 log

    Args:
        log_status (str): status/type of the log
        log_title (str): category of the log
        log_description (str): information and detail of the log
        path (str): path to the log folder
    """
    if datetime_module_active :
        log_time = str(datetime.datetime.now())
        log_str = f"{log_time} | [{log_status}] {log_title} | {log_description}"
        save(log_str, path)
    else :
        print("[log function cannot be used without datetime module, log can not be save]")
    return

def multiple_log(logs : list[tuple[str]], path : str) :
    if datetime_module_active :
        logs_list = [None]
        log_time = str(datetime.datetime.now())
        count = 1
        for log_item in logs :
            log_status, log_title, log_description = log_item
            log_str = f"{log_time} | [{log_status}] {log_title} | {log_description}"
            if logs_list[-1] == log_str :
                count += 1
            else :
                if count == 1 :
                    logs_list.append(log_str)
                else :
                    prev_log = logs_list[-1]
                    del logs_list[-1]
                    logs_list.append(f"{prev_log} [X{count}]")
                    logs_list.append(log_str)
                    count = 1
        logs_list.remove(None)
        multiple_save(logs_list, path)
    else :
        print("[log function cannot be used without datetime module, log can not be save]")
    return

def save(log_str : str, path : str) :
    if datetime_module_active :
        with open("{}/{}.txt".format(path, session_start_time.replace(":", "_")), 'a') as log_file :
            log_file.write(f"\n{log_str}")
        log_file.close()
    else :
        pass
    return

def multiple_save(log_list : list[str], path : str) :
    if datetime_module_active :
        with open("{}/{}.txt".format(path, session_start_time.replace(":", "_")), 'a') as log_file :
            for log_str in log_list :
                log_file.write(f"\n{log_str}")
        log_file.close()
    else :
        pass
    return