# -*- coding: utf-8 -*-

# Importering og initialisering
import pygame
pygame.init()


# Boolean variabler
run = True # Variabel for å skru av spillet
gamestate = "TITLESCREEN" # "Toggleing" av titlescreen
swap = False # Endring av roller

# Tidsvariabel
seconds = 0 # Timer

# Animasjonsvariabler
moonphase = 0 # Måne
thrusteranim_p = 2 # Thruster til lite romskip
thrusteranim_e = 0 # Thruster til stort romskip
explosion = 0 # Eksplosjon


# Vindu
x_screenwidth = 1000 # X-størrelsen til vinduet
y_screenwidth = 600 # Y-størrelsen til vinduet
win = pygame.display.set_mode((x_screenwidth,y_screenwidth)) # Sette "win" som vinduet
pygame.display.set_caption("Cyberpunk 2088") # Navnet til vinduet


tittel_skrift = pygame.font.SysFont('powerredandgreen', 60) # Tekst til tittel
meny_skrift = pygame.font.SysFont('powerredandgreen', 32) # Tekst til timer



# Sprites til spillet
bg = pygame.image.load("cyberpunk-2088/bilder/bg.png") # Bakgrunn
enemy = pygame.image.load("cyberpunk-2088/bilder/ship6.png") # Motstander
char = pygame.image.load("cyberpunk-2088/bilder/ship1.png") # Romskip
box = pygame.image.load("cyberpunk-2088/bilder/box.png") # Bokser


# Lister med sprites, brukes til animasjoner

# Månen (60 bilder)
moon = [pygame.image.load("cyberpunk-2088/bilder/1.png"),pygame.image.load("cyberpunk-2088/bilder/2.png"),pygame.image.load("cyberpunk-2088/bilder/3.png"),pygame.image.load("cyberpunk-2088/bilder/4.png"),pygame.image.load("cyberpunk-2088/bilder/5.png"),pygame.image.load("cyberpunk-2088/bilder/6.png"),pygame.image.load("cyberpunk-2088/bilder/7.png"),pygame.image.load("cyberpunk-2088/bilder/8.png"),pygame.image.load("cyberpunk-2088/bilder/9.png"),pygame.image.load("cyberpunk-2088/bilder/10.png"),pygame.image.load("cyberpunk-2088/bilder/11.png"),pygame.image.load("cyberpunk-2088/bilder/12.png"),pygame.image.load("cyberpunk-2088/bilder/13.png"),pygame.image.load("cyberpunk-2088/bilder/14.png"),pygame.image.load("cyberpunk-2088/bilder/15.png"),pygame.image.load("cyberpunk-2088/bilder/16.png"),pygame.image.load("cyberpunk-2088/bilder/17.png"),pygame.image.load("cyberpunk-2088/bilder/18.png"),pygame.image.load("cyberpunk-2088/bilder/19.png"),pygame.image.load("cyberpunk-2088/bilder/20.png"),pygame.image.load("cyberpunk-2088/bilder/21.png"),pygame.image.load("cyberpunk-2088/bilder/22.png"),pygame.image.load("cyberpunk-2088/bilder/23.png"),pygame.image.load("cyberpunk-2088/bilder/24.png"),pygame.image.load("cyberpunk-2088/bilder/25.png"),pygame.image.load("cyberpunk-2088/bilder/26.png"),pygame.image.load("cyberpunk-2088/bilder/27.png"),pygame.image.load("cyberpunk-2088/bilder/28.png"),pygame.image.load("cyberpunk-2088/bilder/29.png"),pygame.image.load("cyberpunk-2088/bilder/30.png"),pygame.image.load("cyberpunk-2088/bilder/31.png"),pygame.image.load("cyberpunk-2088/bilder/32.png"),pygame.image.load("cyberpunk-2088/bilder/33.png"),pygame.image.load("cyberpunk-2088/bilder/34.png"),pygame.image.load("cyberpunk-2088/bilder/35.png"),pygame.image.load("cyberpunk-2088/bilder/36.png"),pygame.image.load("cyberpunk-2088/bilder/37.png"),pygame.image.load("cyberpunk-2088/bilder/38.png"),pygame.image.load("cyberpunk-2088/bilder/39.png"),pygame.image.load("cyberpunk-2088/bilder/40.png"),pygame.image.load("cyberpunk-2088/bilder/41.png"),pygame.image.load("cyberpunk-2088/bilder/42.png"),pygame.image.load("cyberpunk-2088/bilder/43.png"),pygame.image.load("cyberpunk-2088/bilder/44.png"),pygame.image.load("cyberpunk-2088/bilder/45.png"),pygame.image.load("cyberpunk-2088/bilder/46.png"),pygame.image.load("cyberpunk-2088/bilder/47.png"),pygame.image.load("cyberpunk-2088/bilder/48.png"),pygame.image.load("cyberpunk-2088/bilder/49.png"),pygame.image.load("cyberpunk-2088/bilder/50.png"),pygame.image.load("cyberpunk-2088/bilder/51.png"),pygame.image.load("cyberpunk-2088/bilder/52.png"),pygame.image.load("cyberpunk-2088/bilder/53.png"),pygame.image.load("cyberpunk-2088/bilder/54.png"),pygame.image.load("cyberpunk-2088/bilder/55.png"),pygame.image.load("cyberpunk-2088/bilder/56.png"),pygame.image.load("cyberpunk-2088/bilder/57.png"),pygame.image.load("cyberpunk-2088/bilder/58.png"),pygame.image.load("cyberpunk-2088/bilder/59.png"),pygame.image.load("cyberpunk-2088/bilder/60.png")]
# Thruster 1 (4 bilder)
p_thruster = [pygame.image.load("cyberpunk-2088/bilder/aexhaust1.png"),pygame.image.load("cyberpunk-2088/bilder/aexhaust2.png"),pygame.image.load("cyberpunk-2088/bilder/aexhaust3.png"),pygame.image.load("cyberpunk-2088/bilder/aexhaust4.png")]
# Thruster 2 (4 bilder)
e_thruster = [pygame.image.load("cyberpunk-2088/bilder/exhaust1.png"), pygame.image.load("cyberpunk-2088/bilder/exhaust2.png"),pygame.image.load("cyberpunk-2088/bilder/exhaust3.png"),pygame.image.load("cyberpunk-2088/bilder/exhaust4.png")]
# Eksplosjon til lite romskip (10 bilder)
boom = [pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_001.png"), pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_003.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_008.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_009.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_012.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_013.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_014.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_017.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_019.png"),pygame.image.load("cyberpunk-2088/bilder/Ship1_Explosion_020.png")]



# Jeg bruker klokkefunksjonen for å begrense antall frames per sekund (fps)
# Dette gir spillet samme fart selv om det spilles på forskjellige PCer
clock = pygame.time.Clock() 


# Variabler for spiller
player_width = 64
player_height = 64
player_pos_y = 300 - player_height/2
player_pos_x = 550
player_vel = 10 # Hastighet

# Variabler for motstandere
enemy_width = 128
enemy_height = 128
enemy_pos_y = 300 - enemy_height/2
enemy_pos_x = 50
enemy_vel = 5 # Hastighet


# Tegning av månen
def moondraw():
    global moonphase # Bruker animasjonsvariablet fra linje 17
    
    
    moonspeed = 10 # Hvor fort bildene blas gjennom
    if moonphase > 59 * moonspeed + (moonspeed-1): # Sirkulere gjennom alle 60 bildene
        moonphase = 0 # Resette varablet
        
    currentmoon = moon[moonphase // moonspeed] # Heltallsdivisjon for å finne riktig bilde   
    
    win.blit(currentmoon,(700,100)) # Tegn månen
    moonphase += 1 


# Tegningen av spillet
def REDRAWGAMEWINDOW():
    global thrusteranim_p, thrusteranim_e # Globale animasjonsvariabler
 
    win.blit(bg, (0,-450)) # Bakrgunn
    moondraw() # Måne
        
    
    if thrusteranim_p > 40 - 1: # 4 bilder, 10 frames på hver, liste starter på 0
        thrusteranim_p = 0
    
    if thrusteranim_e > 40 - 1: # 4 bilder, 10 frames på hver, liste starter på 0
        thrusteranim_e = 0

    # Lite romskip
    win.blit(char,(player_pos_x,player_pos_y)) # Tegning av romskipet
    win.blit(p_thruster[thrusteranim_p // 10], (player_pos_x-50,player_pos_y)) # Tegning av thruster
    
    # Stort romskip
    win.blit(enemy,(enemy_pos_x,enemy_pos_y)) # Tegning av romskip
    win.blit(e_thruster[thrusteranim_e // 10], (enemy_pos_x-20,enemy_pos_y+48)) # Tegning av thruster 
        
        
    # Sirkulere gjennom animasjonene
    thrusteranim_p += 1 # Lite skip
    thrusteranim_e += 1 # Stort skip

    
    
    
    win.blit(meny_skrift.render(f"Tid: {round(seconds, 1)}", True, (255,255,255)), (20,20))
    pygame.display.update() # Oppdatering av skjermen
    
    
# Bevegelse   
def MOVECHECK():
    # Globalisering av variabler
    global player_pos_x, player_pos_y, enemy_pos_x, enemy_pos_y
    
    # Få tastene som er trykket ned
    keys = pygame.key.get_pressed()
    
    # Sjekke hvem som skal spille hvem
    if swap == False: # Hvis venstre spiller stort romskip
        
        # Her er selve bevegelsene
        
        # Lite romskip
        if keys[pygame.K_LEFT] and player_pos_x > 0: # Venstre
            player_pos_x -= player_vel
        
        if keys[pygame.K_RIGHT] and player_pos_x < x_screenwidth-player_width: # Høyre
           player_pos_x += player_vel
        
        if keys[pygame.K_UP] and player_pos_y > -10: # Opp
            player_pos_y -= player_vel
        
        if keys[pygame.K_DOWN] and player_pos_y < y_screenwidth - player_width + 10: # Ned
            player_pos_y += player_vel
            
            
        # Stort romskip
        if keys[pygame.K_a] and enemy_pos_x > 0: # Venstre
            enemy_pos_x -= enemy_vel
            
        if keys[pygame.K_d] and enemy_pos_x < x_screenwidth-enemy_width: # Høyre
            enemy_pos_x += enemy_vel
            
        if keys[pygame.K_w] and enemy_pos_y > -25: # Opp
            enemy_pos_y -= enemy_vel
            
        if keys[pygame.K_s] and enemy_pos_y < y_screenwidth - enemy_width + 25: # Ned
            enemy_pos_y += enemy_vel        
            
    else: # Hvis høyre spiller stort romskip
        
        # Lite romskip
        if keys[pygame.K_a] and player_pos_x > 0: # Venstre
            player_pos_x -= player_vel
        
        if keys[pygame.K_d] and player_pos_x < x_screenwidth-player_width: # Høyre
           player_pos_x += player_vel
        
        if keys[pygame.K_w] and player_pos_y > 0: # Opp
            player_pos_y -= player_vel
        
        if keys[pygame.K_s] and player_pos_y < y_screenwidth-player_width: # Ned
            player_pos_y += player_vel
            
            
        # Stort romskip
        if keys[pygame.K_LEFT] and enemy_pos_x > 0: # Venstre
            enemy_pos_x -= enemy_vel
            
        if keys[pygame.K_RIGHT] and enemy_pos_x < x_screenwidth-enemy_width: # Høyre
            enemy_pos_x += enemy_vel
            
        if keys[pygame.K_UP] and enemy_pos_y > 0: # Opp
            enemy_pos_y -= enemy_vel
            
        if keys[pygame.K_DOWN] and enemy_pos_y < y_screenwidth-enemy_width: # Ned
            enemy_pos_y += enemy_vel
  
            
# Avsluttelse
def QUITCHECK():
    # Globalisering av variabler
    global gamestate, run, x
    
    # Lukke vinduet manuelt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Karakter-kollisjons-boks
    charRect = pygame.Rect(player_pos_x,player_pos_y+20,player_width,player_height-40)
    
    # Motstander-kollisjons-boks
    enemyRect = pygame.Rect(enemy_pos_x+20,enemy_pos_y+40,enemy_width-40,enemy_height-80)

    # Kollisjons-kræsj
    if charRect.colliderect(enemyRect):
        gamestate = "GAMEOVER"


# Timer (WIP)
def TIMERLOOP():
    # Globalisering av variabler
    global seconds # Sekunder som brukes i timeren
    
    seconds = (pygame.time.get_ticks()-start_ticks)/1000 # Timer for å få siste tid


# Titlescreen
def TITLESCREEN():
    # Globalisering av mange variabler
    global gamestate, currently_swapping, start_ticks, swap, player_pos_y, player_pos_x, enemy_pos_y, enemy_pos_x, player_height, enemy_height

    # Få tastene som er trykket ned
    keys = pygame.key.get_pressed()

    # Starte spillet gjennom å trykke på mellomrom
    if keys[pygame.K_SPACE]:
        gamestate = "GAME"
        start_ticks=pygame.time.get_ticks()
        player_pos_y = 300 - player_height/2
        player_pos_x = 550
        enemy_pos_y = 300 - enemy_height/2
        enemy_pos_x = 50
        
    # Bytte på hvem som spiller hvem
    if keys[pygame.K_1] == True:
        swap = True
    if keys[pygame.K_2] == True:
        swap = False
            
    win.blit(bg, (0,-450)) # Tegne bakrgunnen
    moondraw() # Tegne månen
    
    # Teksten i titlescreen
    win.blit(tittel_skrift.render("Cyberpunk 2088", False, (255,255,255)), (50,100))
    win.blit(meny_skrift.render(f"Siste tid: {round(seconds, 1)} sekunder", False, (255,255,255)), (20,20))
    win.blit(meny_skrift.render("Trykk på mellomrom for å starte", False, (255,255,255)), (50,250))
    win.blit(meny_skrift.render("Trykk på 1 eller 2 for å bytte på roller", False, (255,255,255)), (50,300))
    
    # De to boksene nederst på siden
    win.blit(box, (50,470))
    win.blit(box, (800,470))
    
    # Visualisering av spillerbytte
    if swap == False:
        win.blit(char,(812, 485))
        win.blit(enemy,(30, 450))   
    if swap == True:
        win.blit(char,(60, 485))
        win.blit(enemy,(778, 450))
   
   
    pygame.display.update() # Oppdatering av skjermen
    
    
# Deathscreen
def DEATHSCREEN():
    # Globalisering av variabler
    global explosion, gamestate, player_pos_x, player_pos_y, enemy_pos_x, enemy_pos_y
    
    explosion_speed = 10 # Animasjonshastighet
    
    win.blit(bg, (0,-450)) # Tegne bakrgunn
    moondraw() # Tegne månen
    
    # Stort romskip
    win.blit(enemy,(enemy_pos_x,enemy_pos_y)) # Tegning av romskip
    win.blit(e_thruster[0], (enemy_pos_x-20,enemy_pos_y+48)) # Tegning av thruster 
    
    current_boom = boom [explosion // explosion_speed] # Bestemme animasjonsbilde
    win.blit(current_boom, (player_pos_x-32, player_pos_y-32)) # Tegne eksplosjonen
    
    explosion += 1 # Endring av animasjonevariabelet
    
    if explosion > 9 * explosion_speed: # Animasjonen skal spillen kun 1 gang
        explosion = 0 # Resette til neste eksplosjon
        gamestate = "TITLESCREEN" # Sette gamestate til titlescreen
        
        # Resette posisjonene til romskipene
        enemy_pos_y = 300 - enemy_height/2
        enemy_pos_x = 50
        player_pos_y = 300 - player_height/2
        player_pos_x = 550
    
    pygame.display.update() # Oppdatering av skjermen
    

# Main Loop
while run:
    
    clock.tick(100) # Clockspeed
    
    QUITCHECK() # Passe på at du kan gå ut av spillet
    
    # Sjekke hvilken del av spillet dom skal tegnes
    if gamestate == "GAME": # Selve spillet
        
        # Timer
        TIMERLOOP()
        
        # Bevegelse
        MOVECHECK()
    
        # Tegne spillet
        REDRAWGAMEWINDOW()
        
    if gamestate == "GAMEOVER": # Eksplosjonsekvensen
        # Deathscreen
        DEATHSCREEN()
        
    if gamestate == "TITLESCREEN": # Startskjerm
        # Titlescreen
        TITLESCREEN()
        

pygame.quit() # Avslutte spillet