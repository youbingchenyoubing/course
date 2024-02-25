import time


def run_time(fun):
    def wrapper():
        start = time.time()
        result = fun()
        end = time.time()
        print(f'函数{fun.__name__}的执行时间为{(end-start):.4}秒')
        return result
    return wrapper


def fun1():
    for _ in range(10):
        time.sleep(0.1)


def fun2():
    for _ in range(10):
        time.sleep(0.2)


if __name__ == "__main__":
    f1 = run_time(fun1)
    f1()
    f2 = run_time(fun2)
    f2()
