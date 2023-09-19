'''
@Project : fastApi_01
@File: user.Py
@IDE: 
@Author : 此去经年
@Date: 2023-09-21 10:08

'''

from common.table import Table, fields

"""用户表
后面打算提供根据username、nickname 查询 所以设置了索引
username 必须唯一
"""


class User(Table):
    id = fields.IntField(pk=True)  # 用户ID
    username = fields.CharField(max_length=20, description="账号", unique=True, index=True)
    password = fields.CharField(max_length=20, description="密码")
    nickname = fields.CharField(max_length=20, description="昵称", index=True)
    email = fields.CharField(max_length=255,description="邮箱")
    created_at = fields.DatetimeField()  # 创建时间

    class Meta:
        table = "sys_user"



class Profile(Table):
    id = fields.IntField(pk=True)  # 配置文件ID
    user_id = fields.ForeignKeyField('models.User', related_name='profile')  # 关联用户
    avatar = fields.CharField(max_length=255,description="头像")  # 头像
    address = fields.CharField(max_length=255,description="地址")  # 地址
    phone = fields.CharField(max_length=20,description="电话号码")  # 电话号码

    class Meta:
        table = "user_Profile"


class Settings(Table):
    id = fields.IntField(pk=True)  # 设置ID
    user_id = fields.ForeignKeyField('models.User', related_name='settings')  # 关联用户
    theme = fields.CharField(max_length=255,description="主题")  # 主题
    notifications = fields.BooleanField()  # 是否开启通知
    language = fields.CharField(max_length=50)  # 语言

    class Meta:
        table = "sys_Settings"


class Order(Table):
    id = fields.IntField(pk=True)  # 订单ID
    user_id = fields.ForeignKeyField('models.User', related_name='orders')  # 关联用户
    order_number = fields.CharField(max_length=20)  # 订单号
    total_amount = fields.DecimalField(max_digits=10, decimal_places=2)  # 订单总金额
    order_date = fields.DatetimeField()  # 订单日期

    class Meta:
        table = "user_Order"





