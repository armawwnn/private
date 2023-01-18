import time
import psutil

last_resive = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_resive + last_sent


while True:
    byte_resive = psutil.net_io_counters().bytes_recv
    byte_sent = psutil.net_io_counters().bytes_sent
    byte_total = last_resive + last_sent

    new_resive = last_resive - byte_resive
    new_sent = last_sent - byte_sent
    new_total = byte_total - last_total

    mb_new_resive = new_resive / 1024/1024
    mb_new_sent = new_sent / 1024/1024
    mb_new_tota = new_total / 1024/1024

    print(f"{mb_new_resive:.2f} MB received, {mb_new_sent:.2f} MB sent , {mb_new_tota:.2f} MB total")

    time.sleep(1)

    last_resive = byte_resive
    last_sent = byte_sent
    last_total = byte_total
