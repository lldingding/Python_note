def monitor(time):
    # 导入系统模块datetime和第三方模块psutill
    import datetime
    import psutil
    # 获取当前系统时间
    current_time = datetime.datetime.now().strftime("%F %T")
    # cpu信息
    cpu_per = psutil.cpu_percent(interval=time)
    # 内存信息
    memory_info = psutil.virtual_memory()
    # 硬盘信息
    disk_info = psutil.disk_usage("/")
    # 网络信息
    net_info = psutil.net_io_counters()

    log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
    log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (
    psutil.cpu_count(logical=False), memory_info.total / 1024 / 1024 / 1024, disk_info.total / 1024 / 1024 / 1024)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (
    current_time, cpu_per, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "\n\n"
    print(log_str)

    # 操作文件三步骤
    file = open("log", "a")
    file.write(log_str)
    file.close()
def main():
    while True:
        monitor(5)

if __name__ == "__main__":
    main()