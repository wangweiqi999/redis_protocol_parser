from parser import parsed


# 测试简单字符串
def test_simple_string():
    input_str = '+OK\r\n'
    output = parsed(input_str)
    output_expected = 'OK'
    assert output == output_expected


# 测试错误信息
def test_error():
    input_str = '-Error message\r\n'
    output = parsed(input_str)
    output_expected = 'Error message'
    assert output == output_expected


# 测试整数
def test_integer():
    input_str = ':1\r\n'
    output = parsed(input_str)
    output_expected = 1
    assert output == output_expected


# 测试长字符串
def test_bulk_string():
    input_str = '$6\r\nfoobar\r\n'
    output = parsed(input_str)
    output_expected = 'foobar'
    assert output == output_expected


# 测试长字符串为空
def test_empty_string():
    input_str = '$0\r\n\r\n'
    output = parsed(input_str)
    output_expected = ''
    assert output == output_expected


# 测试长字符串为 None
def test_null_string():
    input_str = '$-1\r\n'
    output = parsed(input_str)
    output_expected = None
    assert output == output_expected


# 测试整数数组
def test_array_int():
    input_str = '*3\r\n:1\r\n:2\r\n:3\r\n'
    output = parsed(input_str)
    output_expected = [1, 2, 3]
    assert output == output_expected


# 测试长字符串数组
def test_array_bulk_string():
    input_str = '*2\r\n$3\r\nfoo\r\n$3\r\nbar\r\n'
    output = parsed(input_str)
    output_expected = ['foo', 'bar']
    assert output == output_expected


# 测试混合数组1
def test_mixed_array1():
    input_str = '*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$6\r\nfoobar\r\n'
    output = parsed(input_str)
    output_expected = [1, 2, 3, 4, 'foobar']
    assert output == output_expected


# 测试混合数组2
def test_mixed_array2():
    input_str = '*2\r\n*0\r\n:1\r\n'
    output = parsed(input_str)
    output_expected = [[], 1]
    assert output == output_expected


# 测试数组为  None
def test_null_array():
    input_str = '*-1\r\n'
    output = parsed(input_str)
    output_expected = None
    assert output == output_expected


# 测试数组为空
def test_empty_array():
    input_str = '*0\r\n'
    output = parsed(input_str)
    output_expected = []
    assert output == output_expected


# 测试嵌套数组1
def test_nested_array1():
    input_str = '*3\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Foo\r\n-Bar\r\n:1\r\n'
    output = parsed(input_str)
    output_expected = [[1, 2, 3], ['Foo', 'Bar'], 1]
    assert output == output_expected


# 测试嵌套数组2
def test_nested_array2():
    input_str = '*1\r\n*1\r\n*1\r\n:1\r\n'
    output = parsed(input_str)
    output_expected = [[[1]]]
    assert output == output_expected


# 测试命令1
def test_command1():
    input_str = '*3\r\n$3\r\nSET\r\n$1\r\na\r\n$12\r\nHello World!\r\n'
    output = parsed(input_str)
    output_expected = ['SET', 'a', 'Hello World!']
    assert output == output_expected


# 测试命令2
def test_command2():
    input_str = '*2\r\n$3\r\nGET\r\n$1\r\na\r\n'
    output = parsed(input_str)
    output_expected = ['GET', 'a']
    assert output == output_expected
