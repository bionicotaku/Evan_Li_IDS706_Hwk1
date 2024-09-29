from main import add, subtract

def test_1():
    assert add(1, 2) == 3

def test_2():
    assert subtract(1, 2) == -1
    
def test_3():
    assert add(subtract(1, 2), add(1, 2)) == 2

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    print("All tests passed!")
