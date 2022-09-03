from unittest import result
from judge_maker import make_judge

def test_make_judge_no1():
    """マトリックスNo1
    10点より下の点数がある場合
    """

    result = make_judge("A", [9, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3

def test_make_judge_no2():
    """マトリックスNo2
    30点以下が3つ以上ある場合
    """

    result = make_judge("A", [20, 20, 20, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2

def test_make_judge_no3():
    """マトリックスNo3
    成績がA~Cの場合
    """

    result = make_judge("A", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 1

def test_make_judge_no4():
    """マトリックスNo4
    成績がDの場合
    """

    result = make_judge("D", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 2

def test_make_judge_no5():
    """マトリックスNo5
    成績がEの場合
    """

    result = make_judge("E", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    assert result == 3

def test_make_judge_no6():
    """マトリックスNo6
    gradeがA~E以外の文字であった場合
    """
    try:
        result = make_judge("X", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
        assert False
    except Exception as e:
        assert e.args[0] == "graderにA～E以外の文字が入力されています"
