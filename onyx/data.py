import inspect
from typing import Union
from .handler import Handler
from .enum import data_operator
from .selector import Selector

def get(target:Union[str, tuple, Selector], path:str=None, scale:Union[float, int]=None):
	if isinstance(target, str):
		container_type = "storage"
	if isinstance(target, tuple):
		container_type = "block"
		target = ' '.join(target)
	if isinstance(target, Selector):
		container_type = "entity"
		target = target.build()
	Handler._write(inspect.stack()[1][3], f"data get {container_type} {target} {path or ''} {scale or ''}")

def merge(target:Union[str, tuple, Selector], nbt:str):
	if isinstance(target, str):
		container_type = "storage"
	if isinstance(target, tuple):
		container_type = "block"
		target = ' '.join(target)
	if isinstance(target, Selector):
		container_type = "entity"
		target = target.build()
	Handler._write(inspect.stack()[1][3], f"data merge {container_type} {target} {nbt}")

def modify(target:Union[str, tuple, Selector], path:str, operation:data_operator, data_location:dict):
	if isinstance(target, str):
		container_type = "storage"
	if isinstance(target, tuple):
		container_type = "block"
		target = ' '.join(target)
	if isinstance(target, Selector):
		container_type = "entity"
		target = target.build()
	
	if operation.value == "insert" and "signature1" in data_location:
		raise ValueError("Specified 'insert' operation but not 'index'")
	if operation.value == "insert" and "signature44" in data_location:
		raise ValueError("Specified 'insert' operation but not 'index'")
	if operation.value != "insert" and "signature7" in data_location:
		raise ValueError(f"Specified 'index' but the operation is {operation.value}, not 'insert'")
	if operation.value != "insert" and "signature33" in data_location:
		raise ValueError(f"Specified 'index' but the operation is {operation.value}, not 'insert'")

	if "signature44" or "signature33" in data_location:
		Handler._write(inspect.stack()[1][3], f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}")
	elif "signature7" or "signature1" in data_location:
		Handler._write(inspect.stack()[1][3], f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}")
	else:
		Handler._warn("Missing signature for 'data_location'. Consider using 'set_to()' or 'set_from()' to avoid errors.")
		Handler._write(inspect.stack()[1][3], f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}")

def remove(target:Union[str, tuple, Selector], path:str):
	if isinstance(target, str):
		container_type = "storage"
	if isinstance(target, tuple):
		container_type = "block"
		target = ' '.join(target)
	if isinstance(target, Selector):
		container_type = "entity"
		target = target.build()
	Handler._write(inspect.stack()[1][3], f"data remove {container_type} {target} {path}")