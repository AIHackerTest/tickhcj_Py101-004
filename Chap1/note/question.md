- cmder无法切换到`d:\`所在目录，可以手动使用鼠标右键cmder here，指定一个文件夹在切换到`d:\`,使用powershell正常执行
- `weather_info.txt`(中文内容)读取出的数据使用`.read()`打印为空，换做之前的`test.txt`(英文内容)读取正常，初步了解关于`open`的用法
  - 问题解决，读取中文挡需要指定编码
  - .readline() 分行读取
  - .readlines() 全部读取
- 文件读取用到LPTHW的章节
  - ex15,ex16,ex17
