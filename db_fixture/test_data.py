# coding=utf8
import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB



# create data
datas = {
    'program':[

          {'id': 5, 'match_id': '123', 'title': '节目测试1', 'brief': '节目测试1',
                'image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a',
                'large_image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a'},
          {'id': 6, 'match_id': '123', 'title': '新中潮客栈', 'brief': '欣嫂回归，大差不差',
                'image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a',
                'large_image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a'},
          {'id': 7, 'match_id': '123', 'title': 'test节目', 'brief': '',
                'image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a',
                'large_image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a'},
          {'id': 8, 'match_id': '123', 'title': '测试节目', 'brief': '',
                'image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a',
                'large_image': 'http://image.sports.baofeng.com/63970a88457529ec9ad75c74968ba50a'}
    ],

}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
