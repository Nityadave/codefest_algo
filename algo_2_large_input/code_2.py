
# reading input file
f1 = open('ET_large.txt','r')
data = f1.readline()
#reading total towns to paint
townhouse = []
for i in range(int(data)):
    # in towns reading total house to paint 
    houses = []
    data_2 = f1.readline()
    for j in range(int(data_2)):
        string = f1.readline()
        #appending rooms details of each houses
        houses.append([int(s)for s in (string.split(','))])
    #appending houses details in town
    townhouse.append(houses)
f1.close()

#acc liter 1.5  2.5 hours
#normal liter 2.25  3.25 hours
# used for output
case = 1
f2 = open("ET_output.txt","w")
#itrating through towns
for k in townhouse:
    #variable reset 
    time = 0
    normal_liter = 0
    accent_liter = 0
    #itrating through houses
    for i in k:
        #dividing standard_walls
        standard_wall = i[2]*4
        standard_wall_acc = (standard_wall/3)
        standard_wall_nor = (standard_wall*2)/3
        #dividing roof_walls
        roof_wall  = i[1]*3
        roof_wall_acc = (roof_wall/3)
        roof_wall_nor = (roof_wall*2)/3
        #dividing Victorian_walls
        vic_wall = i[3]*6
        vic_wall_acc = (vic_wall/3)
        vic_wall_nor = (vic_wall*2)/3

        #calculating time
        standard_wall_time = (standard_wall_acc*2.5) + (standard_wall_nor*3.25)
        roof_wall_time = (roof_wall_acc*2.5) + (roof_wall_nor*3.25)
        vic_wall_time = (vic_wall_acc*2.5) + (vic_wall_nor*3.25)


        time += standard_wall_time + roof_wall_time + vic_wall_time
        
        #calculating normal liter 
        standard_wall_qtty = (standard_wall_nor*2.25)
        roof_wall_qtty = (roof_wall_nor*2.25)
        vic_wall_qtty = (vic_wall_nor*2.25)
        normal_liter += standard_wall_qtty + roof_wall_qtty + vic_wall_qtty

        #calculating accent liter
        standard_wall_qtty = (standard_wall_acc*1.5)
        roof_wall_qtty = (roof_wall_acc*1.5)
        vic_wall_qtty = (vic_wall_acc*1.5)
        accent_liter += standard_wall_qtty + roof_wall_qtty + vic_wall_qtty
    #writting output in file
    f2.write(f"Case #{case}:{time},{accent_liter},{normal_liter} \n")
    case += 1
f2.close()