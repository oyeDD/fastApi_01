'''
@Project : fastApi_01
@File: utils.Py
@IDE: 
@Author : 此去经年
@Date: 2023-09-26 14:46

'''

from typing import List, Dict, Any

# 源数据类型
SourceList = List[Dict[str, Any]]

SourceTree = SourceList


def list2tree(arr: SourceList, parent_name: str = "pid", children_name: str = "children") -> SourceTree:
    """
    列表转嵌套树
    :param arr: 传入的list
    :param parent_name: 关系的key名
    :param children_name: 嵌套数据使用的key名
    :return:
    """
    # 1. 将列表转换成字典，列表中元素的唯一标识作为key，列表元素作为value
    menu_map = {item["id"]: item for item in arr}

    tree = []
    for item in arr:

        if item.get(parent_name) is None:
            # 根节点
            tree.append(item)
        else:
            menu_item = menu_map.get(item[parent_name])
            # 子节点
            if menu_item.get(children_name) is None:
                menu_item[children_name] = []
            menu_item[children_name].append(item)
    return tree