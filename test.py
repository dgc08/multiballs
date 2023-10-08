from src.utils import Singleton
from test2 import testf


if __name__ == "__main__":
    s = Singleton()
    s.set_value(2)
    testf()
    print(s.get_value())