import timeit
'''''''''
repeat(stmt='pass', setup='pass', timer=<built-in function perf_counter>, repeat=3, number=1000000, globals=None)
    Convenience function to create Timer object and call repeat method.
参数：stmt：要执行的那段代码
setup：执行代码的准备工作,初始化代码或构建环境导入语句,不计入时间，一般是import之类的
timer：这个在win32下是time.clock()，linux下是time.time()，默认的，不用管
number：要执行stmt多少遍
repeat: 表示执行stmt代码number遍的总次数，比如number=2，repeat=3，
返回[time1,time2,time3],time1~3都是stmt运行2次的总时间。
'''''''''


def test1():
    result = []
    for i in range(2000):
        result.append(str(i))
    return result


def test2():
    result = [str(i) for i in range(2000)]
    return result


def test3():
    result = list(map(str,[i for i in range(1000)]))
    return result
REPEAT_NUMBER = 10
RUN_NUMBER = 1000
# Divide by the number of repeats ,i.e. RUN_NUMBER
# repeat 返回一个列表，包含REPEAT_NUMBER个时间值，每一个时间值都是代码运行RUN_NUMBER次的总时间
'''''''''
 Use the min() rather than the average of the timings. 
 That is a recommendation from me, from Tim Peters, and from Guido van Rossum. 
 The fastest time represents the best an algorithm can perform when 
 the caches are loaded and the system isn't busy with other tasks.
  All the timings are noisy -- the fastest time is the least noisy. 
  It is easy to show that the fastest timings are the most reproducible and 
  therefore the most useful when timing two different implementations. 
'''''''''
time1 = min(timeit.repeat(test1,repeat=REPEAT_NUMBER,number=RUN_NUMBER))/RUN_NUMBER
time2 = min(timeit.repeat(test2,repeat=REPEAT_NUMBER,number=RUN_NUMBER))/RUN_NUMBER
time3 = min(timeit.repeat(test3,repeat=REPEAT_NUMBER,number=RUN_NUMBER))/RUN_NUMBER

print('''test1 运行时间为：{}\n
test2 运行时间为：{}\n
test3 运行时间为：{}'''.format(time1,time2,time3))






