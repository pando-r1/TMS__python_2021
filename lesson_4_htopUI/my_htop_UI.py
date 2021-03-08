import psutil


TEMPLATES = {
    "memory": {
        "total memory": "User memory total: {total:_>10}",
        ""
    }
    # "cpu": {
    #     "Name_column: "
    #     # "times": "User time: {user:_>10}, system time: {system:_>10}",
    #     # "persents": "User used: {user:_>9}%, system time: {system:_>9}%",
    # }
}


def logo():
    """ Writing program's logo """

    logo_htop = [["|||   ||| ||||||||| ||||||||| |||||||||"],
                 ["|||||||||    |||    |||   ||| |||||||||"],
                 ["|||   |||    |||    ||||||||| |||      "]]
            
    return ["{: ^80}".format(*logo) for logo in logo_htop]

def get_memory():
    """ Memory's information """
    memory = psutil.virtual_memory()
    res = {"total": memory[0], "available": memory[1], 
        "used": memory[3], "free": memory[4]}

    return res

# def get_cpu():
#     res = {"times": [], "persents": []}
#     data_times = psutil.Process()
#     for cpu in data_times.as_dict():
#         res["times"].append(cpu[])
#     data_persent = psutil.cpu_times_percent(percpu=True, interval=1)
    
#     return data_times

def show(**kwargs):
    print(**kwargs)
    print(TEMPLATES["memory"]["total"].format(**t), end="\t")
    


def main():
    # print(*logo(), sep="\n")
    # print(get_cpu())
    show()


    show(get_memory)


if __name__ == "__main__":
    main()