
def fun():
    return
    

def main():

    assert_cases = [
        [0,0,0],
    ]
    for var1, var2, expected in assert_cases:
        result = fun(var1, var2)
        print("var1={}, var2={}, expected={}, result={}"
              .format(var1, var2, expected, result))
        if result != expected:
            print("ERROR")

if __name__ == "__main__":
    main()
