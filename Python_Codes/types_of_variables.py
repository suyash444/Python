# create a class dump and define the instance and static variables
class Dump:
    well = 10  # this is called static variable as its inside class and outside init method

    def __init__(self):
        self.engine = 'bugati'
        self.top_speed = 320  # this is called instance variable as its inside init method


c1 = Dump()
c2 = Dump()

c1.engine = 'Ferrari'  # we can change the value by calling object name
c1.top_speed = 450
c1.well = '50'

print(c1.engine, c1.top_speed, c1.well)
print(c2.engine, c2.top_speed, c2.well)
