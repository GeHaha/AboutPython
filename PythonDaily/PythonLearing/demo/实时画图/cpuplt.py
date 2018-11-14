# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:33:42 2018

@author: Administrator
"""



import psutil as p
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

POINTS = 300

fig,ax = plt.subplots()

ax.set_ylim([0, 100])
ax.set_xlim([0, POINTS])
ax.set_autoscale_on(False)

ax.set_xticks([])
ax.set_yticks(range(0, 101, 10))
ax.grid(True)

user = [None] * POINTS
nice = [None] * POINTS
sys = [None] * POINTS
idle = [None] * POINTS

l_user, = ax.plot(range(POINTS), user, label = 'User %')
l_nice, = ax.plot(range(POINTS), nice, label = 'Nice %')
l_sys, = ax.plot(range(POINTS), sys, label = 'Sys %')
l_idle, = ax.plot(range(POINTS), idle, label = 'Idle %')

ax.legend(loc = 'upper center',
           ncol = 4, prop = font_manager.FontProperties(size = 10))

bg = fig.canvas.copy_from_bbox(ax.bbox)

def prepare_cpu_usage():
    t = p.cpu_times()
    if hasattr(t, 'nice'):
        return [t.user, t.nice, t.system, t.idle]
    else: 
        return [t.user, 0, t.system, t.idle]

before = prepare_cpu_usage()

def get_cpu_usage():
    global before

    now = prepare_cpu_usage()
    delta = [now[i] - before[i] for i in range(len(now))]
    total = sum(delta)
    before = now
    return [(100.0*dt)/(total+0.1) for dt in delta]

def OnTimer(ax):
    global user,nice,sys,idle,bg

    tmp = get_cpu_usage()

    user = user[1:] + [tmp[0]]
    nice = nice[1:] + [tmp[1]]
    sys = sys[1:] + [tmp[2]]
    idle = idle[1:] + [tmp[3]]

    l_user.set_ydata(user)
    l_nice.set_ydata(nice)
    l_sys.set_ydata(sys)
    l_idle.set_ydata(idle)

    ax.draw_artist(l_user)
    ax.draw_artist(l_nice)
    ax.draw_artist(l_sys)
    ax.draw_artist(l_idle)

    ax.figure.canvas.draw()

timer = fig.canvas.new_timer(interval=100)
timer.add_callback(OnTimer,ax)
timer.start()
plt.show()
