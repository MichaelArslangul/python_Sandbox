class Doors:

    def count_open_doors(self, number):
        _list = [0]*number
        for i in range(1, number+1):
            for j in range(i, number, i):
                _list[j] = int(not(_list[j]))
        return _list

    def count_open_doors2(self, number):
        for i in range(1,int(number**0.5)+1):
            print("Door {} is open".format(i**2))
        print("All other doors are closed")


door = Doors()
door.count_open_doors2(100)
