import sys
import urllib3


class Download(object):
    file_sizes = 0

    # 以1024*1024=1m为单位分块下载
    def download(self, remote_url, save_path, chunk_size=1024):
        print('Download is initializing, please wait for minute.')
        http = urllib3.PoolManager()
        with http.request('GET', remote_url, preload_content=False) as response:
            content_size = int(response.headers['content-length'])  # 获取目标文件的B大小
            print('Downloading...')
            with open(save_path, 'wb') as file:
                for chunk in response.stream(chunk_size):
                    file.write(chunk)
                    self.progress_bar(save_path.split('/')[-1], content_size, len(chunk))
        response.release_conn()

    # 更新下载进度
    def progress_bar(self, file_name, total_sizes, file_size):
        self.file_sizes += file_size
        if self.file_sizes >= total_sizes:
            self.file_sizes = total_sizes
        percent = (self.file_sizes / total_sizes) * 100
        message = '\r{}: [{}{}] {}% {}MB {}MB'.format(file_name, '=' * int(percent), ' ' * int(100 - percent),
                                                      round(percent, 2), round(self.file_sizes / 1024 / 1024, 2),
                                                      round(total_sizes / 1024 / 1024, 2))
        sys.stdout.write(message)
        sys.stdout.flush()
