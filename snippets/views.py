from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from snippets.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        ### 新增用户的接口
        #### 请求方法
            - post

        #### 请求格式
            - json

        #### 请求参数
        | 字段名| 含义  | 类型   | 是否必填   |  示例  |
        |:------:|:------:|:------:|:------:|:------:|
        | first_name | 姓    |  string |是 |李 |
        | last_name | 名    |  string |是 |四 |
        | password | 密码  |  string |是 |test |
        | email | 邮箱    |   string |是 |test@163.com |

        #### 返回参数
        | 字段名| 含义  | 类型   |
        |:------:|:------:|:------:|
        | code | 状态码    |  int |
        | message | 附加消息    |
        | data | 数据  |  dict |

        #### 返回格式
            -json

        #### 返回示例
            - {"code": 0, "message": "success", "data":{}}
        """
        super(UserViewSet, self).create(self, request, *args, **kwargs)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group
    serializer_class = GroupSerializer
