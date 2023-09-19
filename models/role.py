'''
@Project : fastApi_01
@File: Role.Py
@IDE: 角色表
@Author : 此去经年
@Date: 2023-09-21 10:23

'''

from common.table import Table, fields

class Role(Table):
    role_name = fields.CharField(max_length=10, index=True, description="角色名称")
    desc = fields.CharField(max_length=60, null=True, description="描述")

    class Meta:
        table = "sys_role"
