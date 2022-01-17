from raiseexcetionex import UserEx

a='10'
try:
    print(10/0)
except ArithmeticError as e:
    print(f"there was an {e} error")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f"ocurredd   {e}")
else:
    print("error")
finally:
    print(f"there was an {Exception} error")

a=100

try:
    raise(UserEx())
except UserEx as e:
    print(e)