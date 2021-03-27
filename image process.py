import cv2
import random

#pixel format BGR
#size 100x100

#import image
img = cv2.imread('image9.jpg',1)


#makes all the pixels black or white
def correct_pixels(img):
    #all rows
    for y in range(0, 100):
        #all columns
        for x in range(0, 100):
            
            #if bright pixel make it white
            if img[y][x][0] > [125] and img[y][x][1] > [125] and img[y][x][2] > [125] :
                img[y][x] = [255,255,255]
            
            #if pixel is not white make black
            if img[y][x][0] != [255] and img[y][x][1] != [255] and img[y][x][2] != [255] :
                img[y][x] = [0,0,0]
                
                       
    
    return img
#2d array containing RGB of all pixels
new_img = correct_pixels(img)


#display new image for 2.5 seconds
cv2.imshow('digit',new_img)

cv2.waitKey(2500)

#expected output for number
print('What number is it supposed to be:')
correct_num = input()


#==============================================================================================================================

#function reads a file that contains the count of times a wrong number was guessed
def get_mistakes():
    
    mistakes = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    
    file = open("mistakes.txt","r")

    
    for digit in range(0,10):
        mistakes[digit] = int(file.read(1))
    
    
    file.close()
    
    file = open("mistakes.txt")
    file.close()
    
    return mistakes


#==============================================================================================================================

#records a mistake in the file if the guess was wrong
def write (mistakes):
    file = open("mistakes.txt","w")
    for i in range(0,10):
        file.write(str(mistakes[i]))
    file.close()
    return 0



#==============================================================================================================================
def horizontal_top_line(new_img):
    #check for top hoizontal  (5,7)
    line_found = False
    
    for y in range(0, 20):
        for x in range(0, 100):
            
            if img[y][x][0] == 0 and x < 49:
                offset = 0
                straight_line = True 
                for offset in range(0,50):
                    
                    if img[y][x+offset][0] == 255 and img[y-1][x+offset][0] == 255 and img[y+1][x+offset][0] == 255:
                        straight_line = False
                
                if straight_line == True:
                    line_found = True
    
    return line_found

#==============================================================================================================================

def surround_top_left_down(new_img):
    #checks to see if there is a coordinate that has a black line above bellow and to the left of it
    #should only be present in 5
    
    #return value
    probes_pass = 0
    #x and y coordinates
    probes_y = 30
    probe_x1 = 30
    probe_x2 = 50
    probe_x3 = 70
    
    #success criteria for each probe 3 out of possible 3 is a pass 
    probe1 = 0
    probe2 = 0
    probe3 = 0
    
    #making sure probe did not pinpoint a line 
    if img[probes_y][probe_x1][0] != 0:
        #check the horizontal line from the start to our probe
        for x in range(0,probe_x1+1):
            if new_img[probes_y][x][0] == 0:
                #if it finds a black pixel it means there is a part of the nuber to the left of the probe
                probe1+=1
                break
        #checking from the top of the image towards the probe
        for y in range(0,probes_y+1):
            #if black pixel is encounterd there is part of the digit above the probe
            if img[y][probe_x1][0] == 0:
                probe1+=1
                break
        #checking from the probe down towards the middle of the image
        for y in range(probes_y,70):
            #if black pixel is encounterd there is part of the digit bellow the probe
            if img[y][probe_x1][0] == 0:
                probe1+=1
                break        
        
              
    if img[probes_y][probe_x2][0] != 0:        
        for x in range(0,probe_x2+1):
            if new_img[probes_y][x][0] == 0:
                probe2+=1
                break
        for y in range(0,probes_y+1):
            if img[y][probe_x2][0] == 0:
                probe2+=1
                break
        for y in range(probes_y,70):
            if img[y][probe_x2][0] == 0:
                probe2+=1
                break
            
    if img[probes_y][probe_x3][0] != 0:        
        for x in range(0,probe_x3+1):
            if new_img[probes_y][x][0] == 0:
                probe3+=1
                break
        for y in range(0,probes_y+1):
            if img[y][probe_x3][0] == 0:
                probe3+=1
                break
        for y in range(probes_y,70):
            if img[y][probe_x3][0] == 0:
                probe3+=1
                break
    #counting all the probes that passed
    if probe1 == 3:
        probes_pass+= 1
    if probe2 == 3:
        probes_pass+= 1
    if probe3 == 3:
        probes_pass+= 1

    
    #if there is a black pixel to the right of our probe it is not a 5 so we retroactivly fail that probe
    for x in range(probe_x1+1,100):
        if img[probes_y][x][0] == 0 and probe1 == 3:
            probes_pass-= 1
            break
    for x in range(probe_x2+1,100):
        if img[probes_y][x][0] == 0 and probe2 == 3:
            probes_pass-= 1
            break
    for x in range(probe_x3+1,100):
        if img[probes_y][x][0] == 0 and probe3 == 3:
            probes_pass-= 1
            break
        
    return probes_pass
#==============================================================================================================================

#checks image for vertical line in the middle present in  1 and 4
def vertical_line_middle(new_img):
    found_line = False
    line = False
    
    for x in range(30,70):
        for y in range(0,100):
            
            if img [y][x][0] == 0:
                
                if y < 49:
                    line = True
                    for offset in range(0,45):
                        if img[y+offset][x][0] == 255 and img[y+offset][x+1][0] == 255 and img[y+offset][x+2][0] == 255 and img[y+offset][x+3][0] == 255 and img[y+offset][x-1][0] == 255 and img[y+offset][x-2][0] == 255 and img[y+offset][x-3][0] == 255:
                            line = False                    
            if line == True:
                found_line = True
    
    
    return found_line
#==============================================================================================================================

#checks for a horizontal line at the bottom
def horizontal_bottom_line(new_img):
    #check for bottom hoizontal  (1,2)
    line_found = False
    
    for y in range(70, 98):
        for x in range(0, 100):
            
            if img[y][x][0] == 0 and x < 48:
                offset = 0
                straight_line = True 
                for offset in range(0,49):
                    
                    if img[y][x+offset][0] == 255 and img[y-1][x+offset][0] == 255 and img[y-1][x+offset][0] == 255 and img[y+1][x+offset][0] == 255 and img[y+2][x+offset][0] == 255:
                        straight_line = False
                
                if straight_line == True:
                    line_found = True
    
    return line_found
#==============================================================================================================================

#checks if there is a circle in the lower half of the image
def lower_circle(new_img):
    found_circle = False
    probeX = 49
    probeY = 74
    criteria = 0
    
    for x in range(0,probeX):
        if img[probeY][x][0] == 0:
            criteria+=1
            break
        
    for x in range(probeX,100):
        if img[probeY][x][0] == 0:
            criteria+=1
            break
    for y in range(40,probeY):
        if img[y][probeX][0] == 0:
            criteria+=1
            break
    for y in range(probeY,100):
        if img[y][probeX][0] == 0:
            criteria+=1
            break
    if criteria == 4:
        found_circle = True
        
        
    return found_circle

#==============================================================================================================================

#same thing as the previous function this time for the top half
def upper_circle(new_img):
    found_circle = False
    probeX = 49
    probeY = 24
    criteria = 0
    
    for x in range(0,probeX):
        if img[probeY][x][0] == 0:
            criteria+=1
            
            if x + 15 > probeX:
                criteria-=1        
            
            break
        
    for x in range(probeX,100):
        if img[probeY][x][0] == 0:
            criteria+=1
                  
            break
    
    for y in range(0,probeY):
        if img[y][probeX][0] == 0:
            criteria+=1
            break
    
    for y in range(probeY,60):
        if img[y][probeX][0] == 0 or img[y][probeX+1][0] == 0 or img[y][probeX-1][0] == 0:
            criteria+=1
            break
        
    if criteria == 4:
        found_circle = True

        
    return found_circle

#==============================================================================================================================
def big_circle(new_img):
    found_circle = False
    probeX = 49
    probeY = 49
    criteria = 0
    
    top_count = 0
    bottom_count = 0
    
    bottom_detected = False
    
    for x in range(0,probeX):
        if img[probeY][x][0] == 0:
            criteria+=1
            break
        
    for x in range(probeX,100):
        if img[probeY][x][0] == 0:
            criteria+=1
            break
    for y in range(0,probeY):
        if img[y][probeX][0] == 0:
            if img[y-1][probeX][0] == 255:
                top_count+=1
    if top_count == 1:
        criteria +=1
                
    for y in range(probeY,100):
        if img[y][probeX][0] == 0:
            if img[y-1][probeX][0] == 255:
                bottom_count+=1
    if bottom_count == 1:
        criteria +=1

    if criteria == 4:
        found_circle = True
        
    for y in range(70,100):
        if img[y][probeX][0] == 0: 
            bottom_detected = True

    if bottom_detected == False:
        found_circle = False
        
    return found_circle

#==============================================================================================================================

#3 is an extremly dificult number to read because it has no easy features, therefore probes are used to find out if the number is 3
def find_3(new_img):
    probe_success = 0
    probe1a = 0
    probe1b = 0
    
    probe2a = 0
    probe2b = 0
    
    probe3a = 0
    probe3b = 0    
    
    #X = 30 50 70
    #Y = 30 70
    
    probeX1 = 30
    probeX2 = 50
    probeX3 = 70
    
    probeY1 = 30
    probeY2 = 70
    
    
    if img[probeY1][probeX1][0] != 0:
        #check the horizontal line from the start to our probe
        
        for x in range(0,probeX1+1):
            if new_img[probeY1][x][0] == 0:
                #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                probe1a-=1
                break
        
        for x in range(probeX1,100):
            if new_img[probeY1][x][0] == 0:
                #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                probe1a+=1
                break    
        
        #checking from the top of the image towards the probe
        for y in range(0,probeY1+1):
            #if black pixel is encounterd there is part of the digit above the probe
            if img[y][probeX1][0] == 0:
                probe1a+=1
                break
        #checking from the probe down towards the middle of the image
        for y in range(probeY1,60):
            #if black pixel is encounterd there is part of the digit bellow the probe
            if img[y][probeX1][0] == 0:
                probe1a+=1
                break            
        
        if probe1a == 3 and img[probeY2][probeX1][0] != 0:
            for x in range(0,probeX1+1):
                if new_img[probeY2][x][0] == 0:
                    #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                    probe1b-=1
                    break
        
            for x in range(probeX1,100):
                if new_img[probeY2][x][0] == 0:
                    #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                    probe1b+=1
                    break    
        
            #checking from the top of the image towards the probe
            for y in range(40,probeY2+1):
                #if black pixel is encounterd there is part of the digit above the probe
                if img[y][probeX1][0] == 0:
                    probe1b+=1
                    break
            #checking from the probe down towards the middle of the image
            for y in range(probeY2,100):
                #if black pixel is encounterd there is part of the digit bellow the probe
                if img[y][probeX1][0] == 0:
                    probe1b+=1
                    break            
            
    if probe1b == 3:
        probe_success +=1
        


    if img[probeY1][probeX2][0] != 0:
        #check the horizontal line from the start to our probe
        
        for x in range(0,probeX2+1):
            if new_img[probeY1][x][0] == 0:
                #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                probe2a-=1
                break
        
        for x in range(probeX2,100):
            if new_img[probeY1][x][0] == 0:
                #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                probe2a+=1
                break    
        
        #checking from the top of the image towards the probe
        for y in range(0,probeY1+1):
            #if black pixel is encounterd there is part of the digit above the probe
            if img[y][probeX2][0] == 0:
                probe2a+=1
                break
        #checking from the probe down towards the middle of the image
        for y in range(probeY1,60):
            #if black pixel is encounterd there is part of the digit bellow the probe
            if img[y][probeX2][0] == 0:
                probe2a+=1
                break            
        
        if probe2a == 3 and img[probeY2][probeX2][0] != 0:
            for x in range(0,probeX2+1):
                if new_img[probeY2][x][0] == 0:
                    #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                    probe2b-=1
                    break
        
            for x in range(probeX2,100):
                if new_img[probeY2][x][0] == 0:
                    #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                    probe2b+=1
                    break    
        
            #checking from the top of the image towards the probe
            for y in range(40,probeY2+1):
                #if black pixel is encounterd there is part of the digit above the probe
                if img[y][probeX2][0] == 0:
                    probe2b+=1
                    break
            #checking from the probe down towards the middle of the image
            for y in range(probeY2,100):
                #if black pixel is encounterd there is part of the digit bellow the probe
                if img[y][probeX2][0] == 0:
                    probe2b+=1
                    break            
            
    if probe2b == 3:
        probe_success +=1
        
        
        if img[probeY1][probeX3][0] != 0:
        #check the horizontal line from the start to our probe
        
            for x in range(0,probeX3+1):
                if new_img[probeY1][x][0] == 0:
                    #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                    probe3a-=1
                    break
            
            for x in range(probeX3,100):
                if new_img[probeY1][x][0] == 0:
                    #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                    probe3a+=1
                    break    
            
            #checking from the top of the image towards the probe
            for y in range(0,probeY1+1):
                #if black pixel is encounterd there is part of the digit above the probe
                if img[y][probeX3][0] == 0:
                    probe3a+=1
                    break
            #checking from the probe down towards the middle of the image
            for y in range(probeY1,60):
                #if black pixel is encounterd there is part of the digit bellow the probe
                if img[y][probeX3][0] == 0:
                    probe3a+=1
                    break            
            
            if probe3a == 3 and img[probeY2][probeX3][0] != 0:
                for x in range(0,probeX3+1):
                    if new_img[probeY2][x][0] == 0:
                        #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                        probe3b-=1
                        break
            
                for x in range(probeX3,100):
                    if new_img[probeY2][x][0] == 0:
                        #if it finds a black pixel it means there is a part of the nuber to the left of the probe bad for 3
                        probe3b+=1
                        break    
            
                #checking from the top of the image towards the probe
                for y in range(40,probeY2+1):
                    #if black pixel is encounterd there is part of the digit above the probe
                    if img[y][probeX3][0] == 0:
                        probe3b+=1
                        break
                #checking from the probe down towards the middle of the image
                for y in range(probeY2,100):
                    #if black pixel is encounterd there is part of the digit bellow the probe
                    if img[y][probeX3][0] == 0:
                        probe3b+=1
                        break            
                
        if probe3b == 3:
            probe_success +=1
            
    
    
    return probe_success

#==============================================================================================================================  

#finding out if it has a horizontal line in the middle
def find_middle_horizontal(new_img):
    line_found = False
    
    for y in range(40, 70):
        for x in range(0, 100):
            
            if img[y][x][0] == 0 and x < 49:
                offset = 0
                straight_line = True 
                for offset in range(0,50):
                    
                    if img[y][x+offset][0] == 255 and img[y+1][x+offset][0] == 255 and img[y+2][x+offset][0] == 255 and img[y+3][x+offset][0] == 255 and img[y+4][x+offset][0] == 255 and img[y+5][x+offset][0] == 255 and img[y+6][x+offset][0] == 255:
                        straight_line = False
                
                if straight_line == True:
                    line_found = True
    
    return line_found    
    

#==============================================================================================================================

#the main function 
def guess_number():
    #index = number value = probability
    
    #intitializing important variables
    mistakes = get_mistakes()
    guess_list = [0,0,0,0,0,0,0,0,0,0]
    probability_list = [-1,-1,-1,-1,-1,-1]
    guess = -1
    guess_sum = 0
    miststakes_sum = 0
    
    #find out the total amount of mistakes
    for a in range(0,10):
        miststakes_sum += mistakes[a]
    
    #The values bellow can be treated as binary and the if statements bellow them are like logic gates that dictate the probability of the given image being guessed correctly based on the given binary values
    pro357 = horizontal_top_line(new_img)
    pro5 = surround_top_left_down(new_img)
    pro14 = vertical_line_middle(new_img)
    pro12 = horizontal_bottom_line(new_img)
    pro68 = lower_circle(new_img)
    pro489 = upper_circle(new_img)
    pro0 = big_circle(new_img)
    pro3 = find_3(new_img)
    pro4 = find_middle_horizontal(new_img)
    
    if pro3 > 0:
        if pro3 >1:
            guess_list[3] = 100
        else:
            guess_list[3] = 97
    elif pro0 == True:
        guess_list[0] = 99
    
    elif pro12 == True:
        if pro14 == True:
            guess_list[1] = 70
            guess_list[2] = 30
        else:
            guess_list[2] = 97
    elif pro357 == True:
        if pro5 == 0:
            guess_list[7] = 96
            guess_list[3] = 3
        else:
            guess_list[5] = 96
            guess_list[3] = 3
    elif pro14 == True:
        if pro4 == True: 
            guess_list[4] = 99
        elif pro489 == True:
            guess_list[9] = 90
            guess_list[4] = 5
        elif pro68 == True:
            guess_list[6] = 90       
        else:
            guess_list[1] = 97
    
    elif pro68 == True:
        if pro489 == True:
            guess_list[8] = 99
        else:
            guess_list[6] = 99
    
    elif pro489 == True:
        guess_list[9] = 99
        
    else:
        for x in range(0,10):
            guess_list[x] = 1
     
    
    # generate 2 primary guesses 
    count = 0
    for j in range(1,3):
        
        max_num = 0
        index = -1
        for i in range(0,10):
            if guess_list[i] > max_num:
                index = i
                max_num = guess_list[i]
        
        if max_num != 0:
            probability_list[count] = index
            probability_list[count+1] = max_num
            guess_list[index] = -1
        count += 2

    # the algorithm makes a difinitive final guess using random chance and probability 
    random_num = random.randrange(1,101)
    
    if probability_list[1] >= random_num:
        guess = probability_list[0]
        
    elif probability_list[3] >= random_num - probability_list[1]:
        guess = probability_list[2]
    else:
        guess = random.randrange(0,10)
    
    if guess_list[0] == 1:
        guess = random.randrange(0,10)
    
    #checking historical mistakes to adjust the guess
    if mistakes[guess] != 0:
        new_odds = (1-(mistakes[guess]/miststakes_sum)) * 100
        
        if new_odds >= random.randrange(0,101):
            guess = guess
        
        elif probability_list[2] == -1:
            guess = random.randrange(0,10)
        else:
            new_odds = (1-(mistakes[probability_list[2]]/miststakes_sum)) * 100
            
            if new_odds >= random.randrange(0,101):
                guess = probability_list[2]
            else:
                guess = random.randrange(0,10)
    
    #recording the result if it is a mistake
    print("I'm guess this is a",guess )
    
    if guess != int(correct_num):
        if mistakes[guess] < 9:
            mistakes[guess]= mistakes[guess]+1
        
    write(mistakes)
    return guess
    
    
    
guess_number()            
          
            
     
          