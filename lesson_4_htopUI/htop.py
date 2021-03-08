import psutil

import random
TEMPLATES = {
    "cpu": {
        "times": "User time: {user:_>10}, system time: {system:_>10}",
        "persents": "User used: {user:_>9}%, system time: {system:_>9}%",
    }
}


def get_cpu():
    res = {"times": [], "persents": []}
    data_times = psutil.cpu_times(percpu=True)
    for cpu in data_times:
        res["times"].append({"user": cpu.user, "system": cpu.system})
    data_persent = psutil.cpu_times_percent(percpu=True, interval=1)
    for cpu in data_persent:
        res["persents"].append({"user": cpu.user, "system": cpu.system})
    return res


def show(**kwargs):
    times = kwargs["cpu"]["times"]
    persents = kwargs["cpu"]["persents"]
    # for t in times:
    #     print(TEMPLATES["cpu"]["times"].format(**t))
    # for p in persents:
    #     print(TEMPLATES["cpu"]["persents"].format(**p))

    for t, p in zip(times, persents):
        print(TEMPLATES["cpu"]["times"].format(**t), end="\t")
        print(TEMPLATES["cpu"]["persents"].format(**p))


def main():
    cpu_info = get_cpu()
    show(cpu=cpu_info)


if __name__ == "__main__":
    main()