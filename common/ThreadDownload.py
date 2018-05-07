import threading
import urllib3

http = urllib3.PoolManager()


class Download(object):
    contents = []
    chunk_list = False

    def __init__(self, url, save_file, count=5):
        """
        :param url: 下载路径
        :param save_file: 文件保存路径
        :param count: 启动的线程数
        """

        self.url = url
        self.save_file = save_file
        self.count = count
        # 获取目标文件的大小，单位bytes
        self.content_length = int(http.request("HEAD", self.url).headers["Content-Length"])

    def download(self, start, end):
        """
        按照文件大小下载文件
        :param start: 文件开始的字节位置
        :param end: 文件结束的字节位置
        :return:
        """

        rp = http.request("GET", self.url, headers={"Range": "bytes={}-{}".format(start, end)})
        file_data = rp.data
        # 记录文件开始下载的字节位置和下载内容
        self.contents.append((start, file_data))

    def run(self):
        """
        启动线程下载任务方法
        :return:
        """

        # 初始化一个空文件
        file = open(self.save_file, "wb")
        file.close()

        # 按照分线程情况启动线程下载
        threads = []
        for length in self.chunk():
            start = length[0]
            end = length[1]
            thread = threading.Thread(target=self.download, args=(start, end))
            thread.start()
            threads.append(thread)

        # 阻塞主线程执行，依次等待上一个子线程结束，再启动下一个子线程，一直到子线程完全结束，然后执行主线程
        for th in threads:
            th.join()

        """
        比较分线程的顺序和下载完成的顺序，按照分线程的顺序写入文件
        因为可能：
        分线程时的chunk_list顺序为：(0, 8741), (8742, 17483), (17484, 26225), (26226, 34967), (34968, 43705)
        下载完成的contents顺序为：(0, 8741),(26226, 34967), (34968, 43705), (8742, 17483), (17484, 26225)
        """
        for start_end in self.chunk_list:
            start_1 = start_end[0]
            for content in self.contents:
                start_2 = content[0]
                if start_1 == start_2:
                    with open(self.save_file, "ab+") as file:
                        file.seek(start_1)
                        file.write(content[1])

    def chunk(self):
        """
        计算每一个文件片段的开始和结束的字节数，并且记录到列表
        :return:
        """

        if self.content_length < self.count or self.count < 1:
            self.count = 1
        mod = self.content_length % self.count
        step = self.content_length // self.count
        step = step + 1 if mod else step

        # 初始化第一个文件块的开始和结束的字节位置
        start = 0
        end = start + step
        chunk_list = [(start, end)]

        # 计算文件块的开始和结束的字节位置
        while self.count > 1:
            self.count -= 1
            start = end + 1
            end = start + step
            if self.count == 1:
                chunk_list.append((start, self.content_length))
                break
            else:
                chunk_list.append((start, end))
        self.chunk_list = chunk_list
        return self.chunk_list


if __name__ == "__main__":
    print("download...........")
    # url = "http://img.zcool.cn/community/01935d57b420380000018c1bc2c27e.jpg@2o.jpg"
    # save = "C:/Users/Administrator/Desktop/test.jpg"
    url = "http://mirror.bit.edu.cn/apache/jmeter/binaries/apache-jmeter-4.0.zip"
    save = "C:/Users/Administrator/Desktop/apache-jmeter-4.0.zip"
    Download(url, save).run()
    print("finish")
