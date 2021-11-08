def numatoms(atomicelement,atomicweight=196.97):
    #avogardo's constant
    avo= 6.022*10**23
    #number of atoms formula
    numatoms= (atomicelement/atomicweight)*avo
    print(numatoms)
    return
#callingoutfunction
numatoms(10)
numatoms(10,12.001)
numatoms(10,1.008)
