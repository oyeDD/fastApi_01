'''
@Project : fastApi_01
@File: shemas.Py
@IDE: 通用出入参数校验模型
@Author : 此去经年
@Date: 2023-09-26 14:45

'''

from typing import Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')


class R(GenericModel, Generic[T]):
    code: int
    data: T
    msg: str

    @staticmethod
    def success(msg: str = "success", data: T = None) -> "R":
        return R(code=200, msg=msg, data=data)

    @staticmethod
    def fail(msg: str = "fail", data: T = None) -> "R":
        return R(code=400, msg=msg, data=data)