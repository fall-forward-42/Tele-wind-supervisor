import wmi
import GPUtil
import cpuinfo
import socket
import psutil
import os
import speedtest
import ctypes
import sys

def get_system_info():
    """Lấy thông tin hệ thống."""
    system_info = wmi.WMI().Win32_ComputerSystem()[0]
    return {
        "Manufacturer": system_info.Manufacturer,
        "Model": system_info.Model,
        "Name": system_info.Name,
        "NumberOfProcessors": system_info.NumberOfProcessors,
        "SystemType": system_info.SystemType,
        "TotalPhysicalMemory": int(system_info.TotalPhysicalMemory) // (1024**3)  # GB
    }

def get_cpu_info():
    """Lấy thông tin CPU."""
    cpu = cpuinfo.get_cpu_info()
    return {
        "Brand": cpu['brand_raw'],
        "Architecture": cpu['arch'],
        "Cores": psutil.cpu_count(logical=False),
        "Threads": psutil.cpu_count(logical=True),
        "Frequency": psutil.cpu_freq()._asdict()
    }

def get_gpu_info():
    """Lấy thông tin GPU."""
    gpus = GPUtil.getGPUs()
    gpu_list = []
    for gpu in gpus:
        gpu_list.append({
            "Name": gpu.name,
            "Load": f"{gpu.load * 100}%",
            "Memory Free": f"{gpu.memoryFree}MB",
            "Memory Used": f"{gpu.memoryUsed}MB",
            "Temperature": f"{gpu.temperature}°C"
        })
    return gpu_list

def get_network_info():
    """Lấy thông tin mạng."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {
        "Hostname": hostname,
        "IP Address": ip_address
    }

def get_memory_info():
    """Lấy thông tin RAM."""
    virtual_memory = psutil.virtual_memory()
    return {
        "Total": f"{virtual_memory.total // (1024**3)} GB",
        "Available": f"{virtual_memory.available // (1024**3)} GB",
        "Used": f"{virtual_memory.used // (1024**3)} GB",
        "Percentage": f"{virtual_memory.percent}%"
    }

def get_disk_info():
    """Lấy thông tin ổ cứng."""
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System Type": partition.fstype,
            "Total": f"{usage.total // (1024**3)} GB",
            "Used": f"{usage.used // (1024**3)} GB",
            "Free": f"{usage.free // (1024**3)} GB",
            "Percentage": f"{usage.percent}%"
        })
    return disk_info

#  BUG: Bị chặn 
def get_speedtest_info():
    """Kiểm tra tốc độ mạng."""
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e+6  # Mbps
    upload_speed = st.upload() / 1e+6  # Mbps
    ping = st.results.ping
    return {
        "Download Speed": f"{download_speed:.2f} Mbps",
        "Upload Speed": f"{upload_speed:.2f} Mbps",
        "Ping": f"{ping:.2f} ms"
    }

def get_os_info():
    """Lấy thông tin hệ điều hành và môi trường."""
    return {
        "OS Name": os.name,
        "User": os.getlogin(),
        "Current Directory": os.getcwd(),
        "PATH": os.environ.get('PATH', '')
    }




#print(get_os_info())
