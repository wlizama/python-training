"""
Simple programador de tareas 
"""

import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_time(my_arg="default"):
    print("La hora es:", time.time(), my_arg)


def print_some_times():
    print(time.time())
    s.enter(10, 2, print_time)
    s.enter(5, 2, print_time, argument=("5 seconds priority 2",))
    s.enter(10, 1, print_time, kwargs={"my_arg": "10 seconds priority 1"})
    s.run()
    print(time.time())


if __name__ == "__main__":
    print_some_times()