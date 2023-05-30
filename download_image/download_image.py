from os import path, mkdir

from icrawler.builtin import GoogleImageCrawler


def download_image(dir_name: str = '', keyword: str = '', max_num: int = 0):
    # todo: This statement will be to create folder if she was not created
    if not path.exists(dir_name):
        mkdir(dir_name)

    google_crawler = GoogleImageCrawler(storage={'root_dir': f'{dir_name}'})
    google_crawler.crawl(keyword=keyword, max_num=max_num)

    if path.exists(dir_name):
        print('Yours images downloaded successful')
    else:
        print('We are sorry for some problems')
