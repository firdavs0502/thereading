from ism import *
from ochistva import *
from familiya import *

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)

t1.start()
t2.start()
t3.start()