'''
@Project : fastApi_01
@File: user_role.Py
@IDE: 用户角色表
@Author : 此去经年
@Date: 2023-09-21 10:32

'''
from common.table import Table, fields

class UserRole(Table):
    user = fields.ForeignKeyField("models.User", on_delete=fields.CASCADE)
    role = fields.ForeignKeyField("models.Role", on_delete=fields.CASCADE)

    class Meta:
        table = "sys_user_role"