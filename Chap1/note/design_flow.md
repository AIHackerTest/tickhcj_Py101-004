
### CLI 版天气通需要完成的功能有：

1. 输入城市名，返回该城市的天气数据；
2. 输入指令，打印帮助文档（一般使用 h 或 help）；
3. 输入指令，退出程序的交互（一般使用 quit 或 exit）；
4. 在退出程序之前，打印查询过的所有城市。


- 核心功能：输入城市名，返回该城市的天气数据。

- 初步的实现思路：

  1. 查询 A 数据所对应的 B 数据
    - 需了解这个功能怎么实现
  2. 用 input( ) 接收输入，使用 if...else... 判断指定输入，使用 print( ) 打印文本
  3. 用 input( ) 接收输入，让程序在得到指定输入时，退出运行
    - 需了解如何让程序退出运行
  4. 将所有被查询过的数据保存，再打印出来
    - 需了解如何保存用户每一次输入结果


### 1wd1

- 四个条件判断完成，判断输入的指令并执行相应判断
- 成功读取`weather_info`
- 如何将读取的数据放入dict
  - 初步想法：以`,`为分隔符，城市名对应key，天气情况对应value

### 1wd2

- 使用`wiht as`，代码更简洁
- 创建简单字典，输入指令读取内容

### 1wd3

- 成功保存历史查询记录，查询记录会被调用两次，想封装为一个函数`history(c, w)`调用，运行报错`NameError: name 'c' is not defined`
- 同一个城市查询多次，历史记录就会重复保存,使用`if`
- `.format()`打印字典里的`key``value`，去除字符串的`''`
- 调用`split()`将天气信息数据转换为可查询的字典
- 成功运行程序，实现要求的四个功能
