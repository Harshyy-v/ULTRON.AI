import psutil
import platform
from datetime import datetime
import GPUtil
from func.Speak import speak


def get_system_info():
    uname = platform.uname()
    system_info = {
        "System": uname.system,
        "Node Name": uname.node,
        "Release": uname.release,
        "Version": uname.version,
        "Machine": uname.machine,
        "Processor": uname.processor,
    }
    return system_info


def get_boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return f"{bt.year}-{bt.month}-{bt.day} {bt.hour}:{bt.minute}:{bt.second}"


def get_cpu_info():
    cpu_info = {
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True),
        "Max Frequency": f"{psutil.cpu_freq().max:.2f}Mhz",
        "Min Frequency": f"{psutil.cpu_freq().min:.2f}Mhz",
        "Current Frequency": f"{psutil.cpu_freq().current:.2f}Mhz",
        "CPU Usage Per Core": psutil.cpu_percent(percpu=True, interval=1),
        "Total CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
    }
    return cpu_info


def get_ram_info():
    svmem = psutil.virtual_memory()
    ram_info = {
        "Total": f"{svmem.total / (1024 ** 3):.2f}GB",
        "Available": f"{svmem.available / (1024 ** 3):.2f}GB",
        "Used": f"{svmem.used / (1024 ** 3):.2f}GB",
        "Percentage": f"{svmem.percent}%",
    }
    return ram_info


def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        partition_info = {
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File system type": partition.fstype,
        }
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            partition_info.update({
                "Total Size": f"{partition_usage.total / (1024 ** 3):.2f}GB",
                "Used": f"{partition_usage.used / (1024 ** 3):.2f}GB",
                "Free": f"{partition_usage.free / (1024 ** 3):.2f}GB",
                "Percentage": f"{partition_usage.percent}%",
            })
        except PermissionError:
            continue
        disk_info.append(partition_info)
    return disk_info


def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = []
    for gpu in gpus:
        info = {
            "GPU Name": gpu.name,
            "GPU Load": f"{gpu.load * 100:.0f}%",
            "GPU Free Memory": f"{gpu.memoryFree}MB",
            "GPU Used Memory": f"{gpu.memoryUsed}MB",
            "GPU Total Memory": f"{gpu.memoryTotal}MB",
            "GPU Temperature": f"{gpu.temperature} °C",
        }
        gpu_info.append(info)
    return gpu_info


def print_system_info():
    print("This is your System Information ....")
    speak("This is your System Information ....")
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\nBoot Time:")
    print(get_boot_time())

    print("\nCPU Info:")
    cpu_info = get_cpu_info()
    for key, value in cpu_info.items():
        if isinstance(value, list):
            print(f"{key}:")
            for i, usage in enumerate(value):
                print(f"  Core {i}: {usage}%")
        else:
            print(f"{key}: {value}")

    print("\nRAM Info:")
    ram_info = get_ram_info()
    for key, value in ram_info.items():
        print(f"{key}: {value}")

    print("\nDisk Info:")
    disk_info = get_disk_info()
    for partition in disk_info:
        for key, value in partition.items():
            print(f"{key}: {value}")
        print("-" * 40)

    print("\nGPU Info:")
    gpu_info = get_gpu_info()
    if not gpu_info:
        print("No GPU found")
    else:
        for i, info in enumerate(gpu_info):
            print(f"GPU {i + 1}:")
            for key, value in info.items():
                print(f"  {key}: {value}")



