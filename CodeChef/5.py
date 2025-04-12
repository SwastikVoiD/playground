def machine(a,b,c):
    cuboid = [a,b,c]
    scrap = 0
    count = 0
    pi = 355/113
    k = min(cuboid)
    if k == 0:
        return 0, 0
    else:
        
        vol_of_cube = k**3
        scrap += vol_of_cube*(1-(pi/6))
        count += 1

        if k == 1:
            return count, scrap

        else:
            m = min(cuboid)
            if a == m:
                cuboid1 = [m,b-m,c-m]
                cuboid2 = [m,]
            
        # # leftovers
        # re_cubes1, re_scrap1 = machine(a%k,b,c)
        # re_cubes2, re_scrap2 = machine(a,b%k,c)
        # re_cubes3, re_scrap3 = machine(a,b,c%k)

        # scrap += re_scrap3 + re_scrap2 + re_scrap1
        # count += re_cubes1 + re_cubes2 + re_cubes3



            return count, scrap

print(machine(3,6,7))