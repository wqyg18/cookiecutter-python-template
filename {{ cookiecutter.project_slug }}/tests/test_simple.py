import pytest

def test_addition():
    """一个简单的加法测试"""
    assert 1 + 1 == 2

def test_subtraction():
    """一个简单的减法测试"""
    assert 5 - 3 == 2

def test_multiplication():
    """一个简单的乘法测试"""
    assert 2 * 3 == 6

def test_division():
    """一个简单的除法测试"""
    assert 10 / 2 == 5

def test_string_concatenation():
    """字符串连接测试"""
    assert "hello" + " " + "world" == "hello world"

@pytest.mark.skip(reason="这是一个被跳过的测试示例")
def test_skipped_example():
    """被跳过的测试示例"""
    assert False  # 这个测试不会运行