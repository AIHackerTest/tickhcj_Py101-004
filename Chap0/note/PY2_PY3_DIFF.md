- PY2的输入用`raw_input`在PY3中使用`input()`
- 打印`print`统一使用`print()`,可直接打印中文，PY3使用unicorn编码
- PY3调用自定义的函数会在当前目录下生成`_pycache_`目录，
  PY2是在文件所在目录生成后缀名为.pyc的cache
- `random`函数使用需要`import random`，哪些函数需要调取modul
- 数据类型的判断
  - `import types`
  - PY2 `type(3) is types.IntType`返回`True`;
  - PY3 `type(3) is types.IntType`错误提示`AttributeError: module 'types' has no attribute 'IntType'`

- `x = input()`->>`3` `type(x)`->>`class 'str'`
  - `isinstance(x, int)`->>`Flase`
- `x = 3`->>`type(x)`->>`class 'int'`
  - `isinstance(x, int)`->>`True`
