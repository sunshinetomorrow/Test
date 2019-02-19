# coding=utf8
import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB



# create data

datas = {
    't_view':[

        {'content_id': '133456092', 'content_type': 8,'user_id':'test001','baby_id':'test001','student_id':'test001',
           'user_type':1}
        # ,
        # {'content_id': '123456093', 'content_type': 8, 'user_id': 'test002', 'baby_id': 'test002','student_id': 'test002',
        #  'user_type': 1}

    ],


}

#测试dbcomment2库，表t_user_1的数据
# datas = {
#     't_user_1':[
#
#         {'user_id':'test001','user_type':1,'baby_id':'test001','name':'test','wx_name':'','image':'test001img',}
#
#     ],
# 't_user':[
#         {'user_id':'testuser001','user_type':1,'baby_id':'testuser001','name':'test','wx_name':''},
#         {'user_id':'testuser001','user_type':1,'baby_id':'testuser002','name':'test','wx_name':''}
#     ]
#
# }


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
