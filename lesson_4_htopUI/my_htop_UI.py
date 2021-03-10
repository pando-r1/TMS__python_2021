import psutil, datetime


TEMPLATES = {

    "cpu": {
        "loading": "{total:_>10}"
    }
}


def logo():
    """ Writing program's logo """

    logo_htop = [["|||   ||| ||||||||| ||||||||| |||||||||"],
                 ["|||||||||    |||    |||   ||| |||||||||"],
                 ["|||   |||    |||    ||||||||| |||      "],
                 ["dude that's very difficult to understand,"], 
                 ["are you  sure about what you are doing?"],
                 ["||||||||| ||||||||| ||||||||| |||   |||"],
                 ["|||       |||   ||| |||||||||    |||   "],
                 ["||||||||| ||||||||| |||          |||   "]]
                 
            
    return ["{:^4}".format(*logo) for logo in logo_htop]


def get_cpu_loading():
    cpu_loading = psutil.cpu_percent(interval=1, percpu=True)
    res = {n+1: "" for n in range(len(cpu_loading))}
    res = dict(zip(res, cpu_loading))
    
    return ["core_"+str(key)+"............................."
            +str(res[key])+"%" for key in res]


def get_pid():
    task_rans = len(psutil.pids())

    return f'task{task_rans:.>34}'


def get_mem():
    mem = psutil.virtual_memory()
    return f'mem_used{mem[2]:.>31}%/{round(mem[0]/1024**3)}gb'


def get_swap():
    swap = psutil.swap_memory()
    return f'swap_used{swap[3]:.>29}%/{round(swap[0]/1024**3)}gb'


def get_time_runs():
    time_up = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    time_up = datetime.datetime.strptime(time_up, '%Y-%m-%d %H:%M:%S')
    time_now = datetime.datetime.now()
    res = time_now - time_up

    return f'time_up{str(res):.>42}'


# def show(**kwargs):
    
#     print(TEMPLATES["cpu"]["loading"].format(**t))
    

def main():
    print(*logo(), sep="\n")
    # get_memory()
    print(*get_cpu_loading(), sep="\n")
    print(get_pid())
    print(get_mem())
    print(get_swap())
    print(get_time_runs())


if __name__ == "__main__":
    main()