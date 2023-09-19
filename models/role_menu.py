'''
@Project : fastApi_01
@File: role_menu.Py
@IDE: 角色菜单表
@Author : 此去经年
@Date: 2023-09-21 10:32

'''
from common.table import Table, fields

class RoleMenu(Table):
    role = fields.ForeignKeyField("models.Role", on_delete=fields.CASCADE)
    menu = fields.ForeignKeyField("models.Menu", on_delete=fields.CASCADE)

    class Meta:
        table = "sys_role_menu"

