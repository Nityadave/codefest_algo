# This is algo 1 problem :-The Web Server Problem
# as per the conditions the best site with most images and less text content 
# should be served first

#reading file
f1 = open("TWSP_small.txt","r") #this is input file
size = int(f1.readline())

site_content = [] 

for i in range(size):
    string = f1.readline()
    #appending each site content details
    string = string.replace('   ','  ') 
    string = string.strip()
    site_content.append([int(s)for s in (string.split('  '))])
f1.close()

#creating a empty variable for the answer
solve = []*size

#itrating from each site details
for i in range(size):
    
    #finding the best site to serve first contains the best site detail and its text content to later compare and switch 
    best = [site_content[0],site_content[0][0]]
    
    #itrating from the site details
    for i in site_content:
        
        #checking if text mb is less then images to load (considering that each test content contains 5 mb and total size of all images is 20 mb fixed)
        if i[0]*5 < 20:
            
            #checking if best site's text content is more then current site
            if best[1] > i[0]:
                
                #replacing best site
                best = [i,i[0]]
            
            #checking if best site's text content is equal to current site 
            elif best[1] == i[0]:
                
                #checking if  best site images is less then equal to current sites images  
                if best[0][1] <= i[1]:
                    
                    #replacing best site
                    best = [i,i[0]]
        
        #checking if current sites text contents mb is equal to current side's image mb(it is a diffrent condition so only best site can be serve first)
        elif i[0]*5 == 20:
                
                # same conditions as above used to get more acurrate best sites 
                if best[1] > i[0]:
                    
                    #replacing best site
                    best = [i,i[0]]

                elif best[1] == i[0]:

                    if best[0][1] <= i[1]:

                        #replacing best site
                        best = [i,i[0]]
        # else if the current sites text content is more then 20 mb(image size)
        else:
                # checking same conditions
                if best[1] > i[0]:

                    best = [i,i[0]]

                elif best[1] == i[0]:

                    if best[0][1] <= i[1]:

                        best = [i,i[0]]

    #best site is appended on the solution and  removed from the old site content list 
    solve.append(best[0])
    site_content.remove(best[0])

f2 = open("TWSP_output.txt","w") #this is output file

for ans in solve:
    my_string = ', '.join(str(x) for x in ans) # making the output same as given in sample 
    my_string += '\n'

    f2.write(my_string)

