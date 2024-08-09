# test_example.py
import calculator

def test_add():
    assert calculator.sum(2, 3) == 5
    assert calculator.sum(-1, 1) == 0
    assert calculator.sub(-1, -2) == 1
    assert calculator.sub(2,2) == 0

