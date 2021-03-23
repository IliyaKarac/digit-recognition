import cv2

#pixel format BGR
#size 100x100

#import image
img = cv2.imread('image8.jpg',1)

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

new_img = correct_pixels(img)


cv2.imshow('digit',new_img)

cv2.waitKey(500)


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
    
    print("Horizontal top:", line_found)
    return line_found

#==============================================================================================================================

def souround_top_left_down(new_img):
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
            
    print("5 hook probes:",probes_pass)
    return probes_pass
#==============================================================================================================================

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
    
    print("Middle line:",found_line)
    
    return found_line
#==============================================================================================================================
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
    
    print("Horizontal bottom:", line_found)
    return line_found
#==============================================================================================================================
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
        
    print("Lower circle:",found_circle)
        
    return found_circle

#==============================================================================================================================
def upper_circle(new_img):
    found_circle = False
    probeX = 49
    probeY = 24
    criteria = 0
    
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
            criteria+=1
            break
    
    for y in range(probeY,60):
        if img[y][probeX][0] == 0 or img[y][probeX+1][0] == 0 or img[y][probeX-1][0] == 0:
            criteria+=1
            break
        
    if criteria == 4:
        found_circle = True
        
    print("Upper circle:",found_circle)
        
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
    print("Big circle:",found_circle)
        
    return found_circle


horizontal_top_line(new_img)
souround_top_left_down(new_img)
vertical_line_middle(new_img)
horizontal_bottom_line(new_img)
lower_circle(new_img)
upper_circle(new_img)
big_circle(new_img)
                
          