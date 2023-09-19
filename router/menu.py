'''
@Project : fastApi_01
@File: menu.Py
@IDE: 菜单管理
@Author : 此去经年
@Date: 2023-09-26 14:48

'''

from fastapi import APIRouter
from common.shemas import R
from models.menu import Menu
from schemas.menu import MenuSchema, MenuInfo, MenuTree

router = APIRouter(prefix="/menu", tags=["菜单管理"])


@router.get("", summary="菜单🌲")
async def query_menu():
    """
    菜单列表-tree
    :return:
    """
    data = await Menu.filter(status=1).all()
    return R.success(data=data)


@router.post("", summary="创建菜单", response_model=R[MenuInfo])
async def add_menu(menu_schema: MenuSchema):
    """
    新增菜单
    :param menu_schema:
    :return:
    """
    obj = await Menu.create(**menu_schema.dict())
    return R.success(data=obj)


@router.put("/{id}", summary="更新菜单", response_model=R[MenuInfo])
async def edit_menu(id: int, menu_schema: MenuSchema):
    """
    更新菜单
    :param id:
    :param menu_schema:
    :return:
    """
    await Menu.filter(id=id).update(**menu_schema.dict())
    data = await Menu.get_or_none(id=id)
    return R.success(data=data)


@router.delete("/{id}", summary="删除菜单", response_model=R)
async def del_menu(id: int):
    """
    删除菜单
    :param id:
    :return:
    逻辑删除 修改状态
    """
    await Menu.filter(id=id).update(status=9)
    return R.success()