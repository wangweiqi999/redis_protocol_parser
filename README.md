# Redis 协议解析器

**A basic Redis protocol parser**

Redis 协议具体请见 [Redis Protocol specification
](https://redis.io/topics/protocol)

## 使用说明

调用 `parser.py` 中的 `parsed` 函数即可得到解析后的 Redis 协议

例如:

```
>>> from parser import parsed
>>> input_str = '*3\r\n:1\r\n:2\r\n:3\r\n'
>>> output_str = parsed(input_str)
>>> print(output_str)

[1, 2, 3]
```

## 运行测试用例

1. 安装依赖: `nose`
2. 进入项目所在目录
3. 在 terminal 中执行 `nosetests` 命令
