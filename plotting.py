
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
import psutil




def data_gen():
    last_resive = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total = last_resive + last_sent
    i = 0
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
        i +=1

        xdata.append(i)
        ydata.append(mb_new_tota)

        print(f"{mb_new_resive:.2f} MB received, {mb_new_sent:.2f} MB sent , {mb_new_tota:.2f} MB total {i}")
        time.sleep(1)
        last_resive = byte_resive
        last_sent = byte_sent
        last_total = byte_total
        yield i,mb_new_tota



def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []




def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init)
plt.show()
ani1 = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init)
plt.show()
