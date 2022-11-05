class Tv:

    def __init__(self, volume):
        self.volume = volume

    def volumes(self):
        volume = int(input('coloque um novo volume: '))
        self.volume = volume
        print(self.volume)

volume = int(input("Deseja qual volume?"))

object = Tv(volume)

object.volumes()