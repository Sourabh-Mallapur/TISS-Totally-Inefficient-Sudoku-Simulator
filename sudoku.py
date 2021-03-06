def main():

    import copy
    import pygame
    import random
    import datetime
    from highscores import highscores,timings,displayhighscore

    mat =  [[0,0,0,0,0,0,0,0,0], #empty matrix
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

    def isSafe(row, col, num):       #function to check if num is ok to place at a row and column
        for x in range(9):
            if mat[row][x] == num:
                return False
        for x in range(9):
            if mat[x][col] == num:
                return False
        Row = row - row % 3  #given any row number returns the row number of the leftmost row of the 3x3 matrix
        Col = col - col % 3  #given any col number returns the col number of the topmost col of the 3x3 matrix
        for i in range(3):
            for j in range(3):
                if mat[i + Row][j + Col] == num:
                    return False
        return True

    diff = (0,0,0)
    t = [1,2,3,4,5,6,7,8,9] # inserts a shuffled row to the matrix
    random.shuffle(t)
    mat[0] = t

    def solve(mat,row,col):                 #function to solve the sudoku
        if (col == 9 and row == 8):         #end check
            return True
        if col == 9:           #row increment
            row += 1
            col = 0
        # if mat[row][col] > 0:
            # return solve(mat,row,col+1)
        t = [x for x in range(1,10)]
        random.shuffle(t)
        for x in t:
            if isSafe(row,col,x):
                mat[row][col] = x
                if solve(mat, row, col + 1):
                    return True
        mat[row][col] = 0
        return False

    solve(mat,1,0)
    solved_mat = copy.deepcopy(mat)    #something to store the solved matrix

    def emptyspaces(mat,diff):
        for i in mat:
            for j in range(random.randint(diff[0],diff[1])):  #editing the matrix to remove some elments
                i[random.randint(0,8)] = 0

    def insert(position, counter, tet): # counter, tet responsable for time tracking
        i,j = position[1], position[0]
        myfont = pygame.font.Font('./Data/fonts/Fredoka One.ttf', 30)
        while 1:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT: #time increment
                    counter += timed             #time related stuff
                    t = str(counter)
                    tet = t[11:19]
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if(mat[i-1][j-1] != 0):  #if number is alredy entered
                    return counter
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_BACKSPACE): #Backspace is clear
                        usermat[i-1][j-1] = 0  #sets value as 0
                        pygame.draw.rect(win, bg_colour,(position[0]*50 + 5, position[1]*50 + 5,40,40))
                        pygame.display.update(50,50,450,450)
                        return counter
                    if(48 < event.key < 58):  # checking for valid input
                        pygame.draw.rect(win, bg_colour, (position[0]*50 + 5, position[1]*50+ 5,40,40))
                        #pygame.draw.rect(window,bg_colour,(startx,starty,width,height))
                        value = myfont.render(str(event.key-48), True, (85,120,109))
                        win.blit(value, (position[0]*50 +17, position[1]*50 + 5))
                        usermat[i-1][j-1] = event.key - 48
                        pygame.display.update(50,50,450,450)
                        return counter
                    else:     # to clear selindicator
                        pygame.draw.rect(win, bg_colour,(position[0]*50 + 21, position[1]*50 + 5,14,7))
                        pygame.display.update(50,50,450,450)
                        return counter
            tt = myfont.render(tet, True, (bg_colour))
            tt = pygame.transform.rotate(tt, 270)  # Flip the text vertically.
            win.blit(tt,(552,40))
            pygame.display.update(550,0,45,200)
            win.blit(side,(550,0))

    def checkclickdiff(x,y):
        nonlocal diff
        if x in range(189,341) and y in range(269,311):
            diff = (1,2, 'Easy')
            emptyspaces(mat,diff) 
            return 0
        if x in range(189,341) and y in range(319,361):
            diff = (2,3, 'Medium')
            emptyspaces(mat,diff) 
            return 0
        if x in range(189,341) and y in range(369,411):
            diff = (2,4, 'Hard')
            emptyspaces(mat,diff) 
            return 0
        return 1

    def diffselect(N,o):
        r = displayhighscore()     #function to display highscores
        pygame.draw.rect(win,line_colour,(130,124,272,340),0,13)                  #buttons!!!!!
        pygame.draw.rect(win,line_colour_bold,(130,124,272,340),6,13)
        pygame.draw.rect(win,(64,71,92),(190,270,150,40),0,10)
        pygame.draw.rect(win,(line_colour_bold),(190,270,150,40),3,10)
        pygame.draw.rect(win,(64,71,92),(190,320,150,40),0,10)
        pygame.draw.rect(win,(line_colour_bold),(190,320,150,40),3,10)
        pygame.draw.rect(win,(64,71,92),(190,370,150,40),0,10)
        pygame.draw.rect(win,(line_colour_bold),(190,370,150,40),3,10)
        t1 = myfont.render('SELECT YOUR',True,(line_colour_bold))
        t2 = myfont.render('DIFFICULTY',True,(line_colour_bold))
        t3 = myfont.render('EASY',True,(line_colour))
        t4 = myfont.render('MEDIUM',True,(line_colour))
        t5 = myfont.render('HARD',True,(line_colour))
        win.blit(t1,(160,152))
        win.blit(t2,(177,182))
        win.blit(t3,(226,271))
        win.blit(t4,(203,321))
        win.blit(t5,(225,371))
        for i in r:
            if i[1] == '99:99:99':
                i[1] = 'No High Score yet'
        font1 = pygame.font.Font('./Data/fonts/Fredoka One.ttf',18)
        for i in range(3):
            e = r[i][0] + ': ' + r[i][1] 
            f = font1.render(e,True,(line_colour_bold))
            win.blit(f,(40,590 + 25*i))
        while N:
            clock.tick(144)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    N = checkclickdiff(pos[0], pos[1])
        bg_img = pygame.image.load('./Data/Images/background.png').convert()
        win.blit(bg_img,(0,-690+o))
        win.blit(bg_img,(0,o))
        pygame.display.update()
        return 0

    def checkclickmain(x,y,i):
        if x in range(199,336) and y in range(389,441):
            return diffselect(1,i)                       #check if play is clicked
        return 1

    def bg(bg_img,sidemain,N):
        i, g = 0, 0
        height = 690
        while N:
            clock.tick(144)
            win.fill((0,0,0))
            win.blit(bg_img,(0,i))              #code for looping background
            win.blit(bg_img,(0,-height+i))
            win.blit(sidemain,(550,g))
            win.blit(sidemain,(550,-height+g))
            if (i > height):
                i=0
                win.blit(bg_img,(0,-height+i))
            i += 0.17
            if (g > height):
                g = 0
                win.blit(sidemain,(550,-height+g))
            g += 0.3
            #high score part
            # f = myfont.render('')
            logo = pygame.image.load('./Data/Images/lo1.png').convert_alpha()
            win.blit(logo, (91,60))
            pygame.draw.rect(win,(64,71,92),(200,390,135,50),0,8)
            pygame.draw.rect(win,(line_colour),(200,390,135,50),4,8)
            f = myfont.render('PLAY!',True,line_colour)
            win.blit(f,(222,396))                            #Buttons!!!
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    N = checkclickmain(pos[0],pos[1],i)   #closure to checking main menu buttons
        return i

    def check(solved_mat,question_mat,usermat,o):
        if usermat == solved_mat:             #check if user solved sudoku is correct
            y = str(counter - datetime.timedelta(minutes=1))
            y = y[11:19]
            highscoreornot = highscores(diff[2],y)  #Check if highscore and store 
            font = pygame.font.Font('./Data/fonts/fredoka One.ttf',25)
            height = 690
            bg_img = pygame.image.load('./Data/Images/background.png').convert()
            bg2 = pygame.image.load('./Data/Images/oncompletion.png').convert_alpha()
            pygame.display.update(550,0,40,690)
            while 1:
                clock.tick(144)  #set fps to 144
                win.fill((0,0,0))
                win.blit(bg_img,(0,o))
                win.blit(bg_img,(0,-height+o))
                win.blit(bg2,(0,0))
                f = font.render(y,True,(255,254,254))
                win.blit(f,(228,317))
                if highscoreornot:
                    f = myfont.render('NEW HIGH SCORE!',True,(255,254,254))
                    f = pygame.transform.rotate(f, random.choice(range(-4,5,1))) 
                    win.blit(f,(147,347))
                win.blit(sidemain,(550,o))
                win.blit(sidemain,(550,-height+o))
                if (o > height):
                    o = 0
                    win.blit(bg_img,(0,-height+o))
                    win.blit(sidemain,(550,-height+o))
                o += 0.17
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  #pressed esc key
                        main()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
            return



        N = 1            #else show wrong entries in red and corrrect ones in green
        f = pygame.font.Font('./Data/fonts/fredoka One.ttf',15)
        b = pygame.image.load('./Data/Images/dim.png').convert_alpha()
        right = pygame.image.load('./Data/Images/right.png').convert_alpha()
        righttl = pygame.image.load('./Data/Images/righttl.png').convert_alpha()
        righttr = pygame.image.load('./Data/Images/righttr.png').convert_alpha()
        rightbl = pygame.image.load('./Data/Images/rightbl.png').convert_alpha()
        rightbr = pygame.image.load('./Data/Images/rightbr.png').convert_alpha()
        wrong = pygame.image.load('./Data/Images/wrong.png').convert_alpha()
        wrongtl = pygame.image.load('./Data/Images/wrongtl.png').convert_alpha()
        wrongtr = pygame.image.load('./Data/Images/wrongtr.png').convert_alpha()
        wrongbl = pygame.image.load('./Data/Images/wrongbl.png').convert_alpha()
        wrongbr = pygame.image.load('./Data/Images/wrongbr.png').convert_alpha()
        win.blit(b,(0,0))
        pygame.draw.rect(win,(line_colour_bold),(395,617,80,32),0,5)
        pygame.draw.rect(win,(line_colour),(395,617,80,32),3,5)
        v10 = f.render('return',True,(line_colour))
        win.blit(v10,(410,623))
        for i in range(9): #row
            for j in range(9): #column
                if question_mat[i][j] == 0 and usermat[i][j] != 0:
                    if usermat[i][j] == solved_mat[i][j]:
                        if i == 0 and j == 0:
                            win.blit(righttl,(50+50*j,50+50*i))
                        elif i == 8 and j == 8:                            #special checks for rounded corners
                            win.blit(rightbr,(50+50*j,50+50*i))
                        elif i == 0 and j == 8:
                            win.blit(righttr,(50+50*j,50+50*i))
                        elif i == 8 and j == 0:
                            win.blit(rightbl,(50+50*j,50+50*i))
                        else:
                            win.blit(right,(50+50*j,50+50*i))
                    else:
                        if i == 0 and j == 0:
                            win.blit(wrongtl,(50+50*j,50+50*i))
                        elif i == 8 and j == 8:
                            win.blit(wrongbr,(50+50*j,50+50*i))
                        elif i == 0 and j == 8:
                            win.blit(wrongtr,(50+50*j,50+50*i))
                        elif i == 8 and j == 0:
                            win.blit(wrongbl,(50+50*j,50+50*i))
                        else:
                            win.blit(wrong,(50+50*j,50+50*i))
        pygame.display.update()
        while N:                 #loop for going back to entering number, 
            clock.tick(144)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if pos[0] in range(395,476) and pos[1] in range(616,650):  #return button

                # if return button clicked, go back to normal but keep the user entered numbers on the board

                        bg_img = pygame.image.load('./Data/Images/background.png').convert()
                        win.blit(bg_img,(0,o))
                        win.blit(bg_img,(0,-690+o))
                        pygame.draw.rect(win,(bg_colour),(50,50,450,450),0,12)
                        for i in range (8):
                            if i == 2 or i == 5:
                                pygame.draw.line(win,(line_colour),(100 + 50*i,50),(100 + 50*i,499),5)  #vertical lines
                                pygame.draw.line(win,(line_colour),(50,100 + 50*i),(499,100 + 50*i),5)  #horizontal lines
                            else:
                                pygame.draw.line(win,(line_colour),(100 + 50*i,50),(100 + 50*i,499),3)
                                pygame.draw.line(win,(line_colour),(50,100 + 50*i),(499,100 + 50*i),3)
                        pygame.draw.rect(win,(line_colour),(50,50,450,450),3,12)

#populating the mat

                        for i in range (9):
                            for j in range (9):
                                if (0 < usermat[i][j] < 10):
                                    if mat[i][j] == 0:
                                        value = myfont.render(str(usermat[i][j]),True,(85,120,109))
                                        win.blit(value,((j+1)*50 + 17,(i+1)*50 + 5))
                                    else:
                                        value = myfont.render(str(usermat[i][j]),True,text_colour)
                                        win.blit(value,((j+1)*50 + 17,(i+1)*50 + 5))

#adding instructions
                        f = pygame.font.Font('./Data/fonts/Fredoka One.ttf',15)
                        s1 = 'INSTRUCTIONS'
                        s2 = '1.Fill the empty boxes with numbers only from 1 to 9'
                        s3 = '2.Only use each number once in each row, column, & grid'
                        s4 = '3.To fill in a number, click an empty box & enter desired number'
                        s5 = '4.To change a number, click the box and enter another number'
                        s6 = '5.To clear a box, click & Press BackSpace'
                        s7 = '6.Use Esc key to return to main menu'
                        s8 = '7.Click Check button to Check answers'
                        s9 = '8.Each Check adds a minute to your Time'
                        v1 = f.render(s1,True,(line_colour_bold))
                        v2 = f.render(s2,True,(line_colour_bold))
                        v3 = f.render(s3,True,(line_colour_bold))
                        v4 = f.render(s4,True,(line_colour_bold))
                        v5 = f.render(s5,True,(line_colour_bold))
                        v6 = f.render(s6,True,(line_colour_bold))
                        v7 = f.render(s7,True,(line_colour_bold))
                        v8 = f.render(s8,True,(line_colour_bold))
                        v9 = f.render(s9,True,(line_colour_bold))
                        win.blit(v1,(50,500+13))
                        win.blit(v2,(50,518+13))
                        win.blit(v3,(50,536+13))
                        win.blit(v4,(50,554+13))
                        win.blit(v5,(50,572+13))
                        win.blit(v6,(50,590+13))
                        win.blit(v7,(50,608+13))
                        win.blit(v8,(50,626+13))
                        win.blit(v9,(50,644+13))

#adding check button
                        pygame.draw.rect(win,(line_colour_bold),(395,617,80,32),0,5)
                        pygame.draw.rect(win,(line_colour),(395,617,80,32),3,5)
                        v10 = f.render('CHECK',True,(line_colour))
                        win.blit(v10,(410,623))
                        pygame.display.update()
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        return


    bg_colour = (233,234,234) #lightblue
    line_colour = (127,157,177) #aqua
    line_colour_bold = (52,64,66) #dark blue
    text_colour = (52,64,66) #DARKblue

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("./Data/sounds/click.wav")
    win = pygame.display.set_mode((590,690))
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load('./Data/Images/icon.png').convert_alpha()
    pygame.display.set_icon(icon)
    global clock #to set fps loosely
    clock = pygame.time.Clock()
    myfont = pygame.font.Font('./Data/fonts/Fredoka One.ttf', 30)           #loading fonts and bunch of assets
    bg_img = pygame.image.load('./Data/Images/background.png').convert()
    sidemain = pygame.image.load('./Data/Images/sideblock1.png').convert()
    side = pygame.image.load('./Data/Images/sideblock.png').convert()
    global o
    o = bg(bg_img,sidemain,1)  #main looping script
    usermat = copy.deepcopy(mat)  #usermat is used to store user anwsers


#drawing the lines

    pygame.draw.rect(win,(bg_colour),(50,50,450,450),0,12)
    for i in range (8):
        if i == 2 or i == 5:
            #pygame.draw.line(display,(rbg_values),startpoint(x,y),endpoint(x,y),width)
            pygame.draw.line(win,(line_colour),(100 + 50*i,50),(100 + 50*i,499),5)  #vertical lines
            pygame.draw.line(win,(line_colour),(50,100 + 50*i),(499,100 + 50*i),5)  #horizontal lines
        else:
            pygame.draw.line(win,(line_colour),(100 + 50*i,50),(100 + 50*i,499),3)
            pygame.draw.line(win,(line_colour),(50,100 + 50*i),(499,100 + 50*i),3)
    pygame.draw.rect(win,(line_colour),(50,50,450,450),3,12)

#populating the mat

    for i in range (9):
        for j in range (9):
            if (0 < mat[i][j] < 10):
                value = myfont.render(str(mat[i][j]),True,text_colour)
                win.blit(value,((j+1)*50 + 17,(i+1)*50 + 5))

#adding instructions
    f = pygame.font.Font('./Data/fonts/Fredoka One.ttf',15)
    s1 = 'INSTRUCTIONS'
    s2 = '1.Fill the empty boxes with numbers only from 1 to 9'
    s3 = '2.Only use each number once in each row, column, & grid'
    s4 = '3.To fill in a number, click an empty box & enter desired number'
    s5 = '4.To change a number, click the box and enter another number'
    s6 = '5.To clear a box, click & Press BackSpace'
    s7 = '6.Use Esc key to return to main menu'
    s8 = '7.Click Check button to Check answers'
    s9 = '8.Each Check adds a minute to your Time'
    v1 = f.render(s1,True,(line_colour_bold))
    v2 = f.render(s2,True,(line_colour_bold))
    v3 = f.render(s3,True,(line_colour_bold))
    v4 = f.render(s4,True,(line_colour_bold))
    v5 = f.render(s5,True,(line_colour_bold))
    v6 = f.render(s6,True,(line_colour_bold))
    v7 = f.render(s7,True,(line_colour_bold))
    v8 = f.render(s8,True,(line_colour_bold))
    v9 = f.render(s9,True,(line_colour_bold))
    win.blit(v1,(50,500+13))
    win.blit(v2,(50,518+13))
    win.blit(v3,(50,536+13))
    win.blit(v4,(50,554+13))
    win.blit(v5,(50,572+13))
    win.blit(v6,(50,590+13))
    win.blit(v7,(50,608+13))
    win.blit(v8,(50,626+13))
    win.blit(v9,(50,644+13))

#adding check button
    pygame.draw.rect(win,(line_colour_bold),(395,617,80,32),0,5)
    pygame.draw.rect(win,(line_colour),(395,617,80,32),3,5)
    v10 = f.render('CHECK',True,(line_colour))
    win.blit(v10,(410,623))
    pygame.display.update()
    pygame.time.set_timer(pygame.USEREVENT, 1000)  #making a userevent that triggers every 1000 miliseconds
    global text, counter, timed       #counter variables for time keeping
    counter, timed = datetime.datetime(2022, 1, 1, 0, 0, 0), datetime.timedelta(seconds = 1)
    text = ''



    #main while loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:  # increment time
                counter += timed
                t = str(counter)
                text = t[11:19]
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # on mouse click
                pos = pygame.mouse.get_pos()  # get mouse coordinates
                if pos[1] in range(49,501) and pos[0] in range (49,501):
                    i,j = pos[1]//50, pos[0]//50
                    selindicator = pygame.image.load('./Data/images/selindicator.png').convert_alpha()  #adds an indicator to remind user 
                    if(mat[i-1][j-1] == 0):
                        pygame.mixer.music.play()
                        win.blit(selindicator,(j*50 + 22, i*50 + 5))
                        pygame.display.update(50,50,450,450)
                    counter = insert((pos[0]//50, pos[1]//50),counter,tet = text)      #insert new value and deleting values
                if pos[0] in range(395,476) and pos[1] in range(616,650):  #check button
                    counter = counter + datetime.timedelta(minutes=1)
                    check(solved_mat,mat,usermat,o)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  #pressed esc key
                main()
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        tt = myfont.render(text, True, (bg_colour))
        tt = pygame.transform.rotate(tt, 270)  # Flip the text vertically.
        win.blit(tt,(552,40))
        pygame.display.update(550,0,45,690)
        win.blit(side,(550,0))
        clock.tick(60)
    return

if __name__ == "__main__":
    main() 