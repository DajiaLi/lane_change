from multiprocessing import Pool

import gym
import random
import time

from gym import envs
# print(envs.registry.all()) # 查看所有已注册的环境
#
# import time
# from multiprocessing.pool import Pool
#
# def numsCheng(i):
#     return i * 2
#
# if __name__ == '__main__':
#     time1 = time.time()
#     nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     pool = Pool(processes=8)
#     result = pool.map(numsCheng, nums_list)
#     pool.close()        # 关闭进程池，不再接受新的进程
#     pool.join()         # 主进程阻塞等待子进程的退出
#
#     print(result)
#     time2 = time.time()
#     print("计算用时：", time2-time1)

# class A(object):
#     def __init__(self, ):
#         pass
#     def __call__(self, n):
#         print(n)
#
#     def test(self,):
#         with Pool(processes=4) as pool:
#             pool.map(self, range(4))
# a = A()
# a.test()

import numpy as np
a = np.array([1, 2 ,3])
print(int(a))