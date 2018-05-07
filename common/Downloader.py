# -----Python 3 Compatible
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
# ---------------------------------
import sys
import urllib3
import threading


class Downloader(object):
    """
        url: 待下载文件链接
        save_path：存放下载文件的路径
        max_block_size：可能出现的最大的下载块大小, 单位Byte
        thread_num: 制定下载线程个数，缺省会根据max_block_size自动计算
    """

    def __init__(self, url, save_path, max_block_size=1024 * 1024 * 500, thread_num=0):
        self.url = url
        self.name = save_path
        """"""
        http = urllib3.PoolManager()
        response = http.request('HEAD', url, preload_content=False)
        self.total = int(response.headers['content-length'])
        # 根据要求或者块大小计算线程个数
        if thread_num:
            self.thread_num = thread_num
        else:
            # self.thread_num = (self.total + max_block_size - 1) // max_block_size
            self.thread_num = self.total // max_block_size + 1
        print(self.thread_num)
        """
            threading.Event()实现线程间通信
            threading.Event()可以使一个线程等待其他线程的通知，我们把这个Event()传递到线程对象中，
            Event()默认内置了一个标志，初始值为False。
            一旦该线程通过wait()方法进入等待状态，直到另一个线程调用该Event()的set()方法将内置标志设置为True时，
            该Event()会通知所有等待状态的线程恢复运行。
        """
        self.event_list = [threading.Event() for _ in range(self.thread_num)]
        self.event_list[0].set()
        print('File size is %d B' % self.total)
        print('File size is %d KB' % (self.total / 1024))

    # 划分每个下载块的范围
    def get_range(self):
        ranges = []
        offset = int(self.total / self.thread_num)
        for i in range(self.thread_num):
            if i == self.thread_num - 1:
                ranges.append((i * offset, ''))
            else:
                ranges.append((i * offset, (i + 1) * offset))
        return ranges

    def download(self, start, end, event_num):
        headers = {'Range': 'bytes=%s-%s' % (start, end), 'Accept-Encoding': '*'}
        http = urllib3.PoolManager()
        with http.request('GET', self.url, headers=headers, preload_content=False) as response:
            # print('%s:%s chunk starts to download' % (start, end))
            self.event_list[event_num].wait()
            self.fd.seek(start)
            self.fd.write(response.read())
            # while True:
            #     data = response.read(int(response.headers['content-length']))
            #     if not data:
            #         break
            #     self.fd.write(data)
            # print("Number[%d] block was written" % event_num)
            if event_num < len(self.event_list) - 1:
                self.event_list[event_num + 1].set()
            self.file_sizes = end
            if end == '':
                self.file_sizes = self.total
            percent = (self.file_sizes / self.total) * 100
            message = '\r[{}{}] {}% {} {}'.format('=' * int(percent), ' ' * int(100 - percent),
                                                  round(percent, 2), self.unit(self.file_sizes),
                                                  self.unit(self.total))
            sys.stdout.write(message)
            sys.stdout.flush()

    # 判断文件大小以及单位
    def unit(self, sizes):
        if sizes >= pow(1024, 4):
            sizes_unit = ('{}TB'.format(round(sizes / pow(1024, 4), 2)))
        elif sizes >= pow(1024, 3):
            sizes_unit = ('{}GB'.format(round(sizes / pow(1024, 3), 2)))
        elif sizes >= pow(1024, 2):
            sizes_unit = ('{}MB'.format(round(sizes / pow(1024, 2), 2)))
        elif sizes >= pow(1024, 1):
            sizes_unit = ('{}KB'.format(round(sizes / pow(1024, 1), 2)))
        else:
            sizes_unit = ('{}B'.format(sizes))
        return sizes_unit

    def run(self):
        self.fd = open(self.name, 'wb')
        thread_list = []
        n = 0
        for ran in self.get_range():
            start, end = ran
            # print('thread %d Range:%s ~ %s Bytes' % (n, start, end))
            thread = threading.Thread(target=self.download, args=(start, end, n))
            thread.start()
            thread_list.append(thread)
            n += 1
        # 设置等待线程结束
        for i in thread_list:
            i.join()
        print('\n' + 'download %s load success' % self.name)
        self.fd.close()
