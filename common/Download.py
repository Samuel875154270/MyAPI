import sys
import urllib3


class Download(object):
    file_sizes = 0

    # 以1024*1024=1m为单位分块下载
    def download(self, remote_url, save_path, chunk_size=1024):
        print('Download is initializing, please wait for minute.')
        http = urllib3.PoolManager()
        with http.request('HEAD', remote_url, preload_content=False) as response:
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
        message = '\r{}: [{}{}] {}% {} {}'.format(file_name, '=' * int(percent), ' ' * int(100 - percent),
                                                  round(percent, 2), self.unit(self.file_sizes),
                                                  self.unit(total_sizes))
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
