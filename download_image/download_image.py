from os import (path, mkdir, getlogin)

from icrawler.builtin import GoogleImageCrawler

path_download = path.join('C:', 'Users', getlogin(), 'Downloads')


def download_image(keyword: str = '', max_num: int = 0):
    # todo: This statement will be to create folder if she was not created
    if not path.exists(f'{path_download}/{keyword}'):
        mkdir(f'{path_download}/{keyword}')

    google_crawler = GoogleImageCrawler(storage={'root_dir': f'{path_download}/{keyword}'})
    google_crawler.crawl(keyword=keyword, max_num=max_num)

    if path.exists(f'{path_download}/{keyword}'):
        print('Yours images downloaded successful')
    else:
        print('We are sorry for some problems')
