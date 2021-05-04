class Q1_cube_volume:
    def cubeVolume(sideLength):
        if type(sideLength) is int:
            volume = float(sideLength) * float(sideLength) * float(sideLength)
        elif type(sideLength) is float:
            volume = sideLength * sideLength * sideLength
        else :
            volume = sideLength
        return volume


    #print(cubeVolume(10))