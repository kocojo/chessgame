import  pygame as p
import chess_engine
import find_next_move
import sys
HEIGHT = WIDTH = 720
DIM = 8
S_SIZE = HEIGHT//DIM
MAX_FPS = 15
images={}
gs = chess_engine.info()
colors = [p.Color('white'),p.Color('grey')]
player_White = True
def phong(screen,gs):
   run = True
   clock = p.time.Clock()
   screen.fill(p.Color("white"))
   while run:
    draw_board(screen)
    draw_Pieces(screen,gs.board)
    if gs.whiteToMove:
        p.draw.rect(screen, p.Color('white'), p.Rect(3 * S_SIZE, 3 * S_SIZE, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('dark green'), p.Rect(3 * S_SIZE, 4 * S_SIZE, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('dark green'), p.Rect(4 * S_SIZE, 3 * S_SIZE, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('white'), p.Rect(4 * S_SIZE, 4 * S_SIZE, S_SIZE, S_SIZE))
        rect = images["wQ"].get_rect()
        rect.center = S_SIZE * 3 + S_SIZE // 2, S_SIZE * 3 + S_SIZE // 2
        screen.blit(images["wQ"], rect)
        rect1 = images["wR"].get_rect()
        rect1.center = S_SIZE * 3 + S_SIZE // 2, S_SIZE * 4 + S_SIZE // 2
        screen.blit(images["wR"], rect1)
        rect2 = images["wN"].get_rect()
        rect2.center = S_SIZE * 4 + S_SIZE // 2, S_SIZE * 3 + S_SIZE // 2
        screen.blit(images["wN"], rect2)
        rect3 = images["wB"].get_rect()
        rect3.center = S_SIZE * 4 + S_SIZE // 2, S_SIZE * 4 + S_SIZE // 2
        screen.blit(images["wB"], rect3)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            elif event.type == p.MOUSEBUTTONDOWN:  # and (gs.whiteToMove and player_White):
                pos2 = p.mouse.get_pos()
                position_2 = (pos2[1] // S_SIZE, pos2[0] // S_SIZE)
                if position_2 == (3,3):
                    run = False
                    return "wQ"
                elif position_2 == (3,4):
                    run = False
                    return "wR"
                elif position_2 == (4,3):
                    run = False
                    return "wN"
                elif position_2 == (4,4):
                    run = False
                    return "wB"
            elif event.type == p.KEYDOWN:
                if event.key == p.K_u:
                    gs.undo()
                    gs.undo()
                    run =False
        clock.tick(MAX_FPS)
        p.display.update()
        p.display.flip()
    else:
        p.draw.rect(screen, p.Color('white'), p.Rect(3 * S_SIZE, 3 * S_SIZE, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('dark green'), p.Rect(3 * S_SIZE, 4 * S_SIZE, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('dark green'), p.Rect(4 * S_SIZE, 3 * S_SIZE, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('white'), p.Rect(4 * S_SIZE, 4 * S_SIZE, S_SIZE, S_SIZE))
        rect = images["bQ"].get_rect()
        rect.center = S_SIZE * 3 + S_SIZE // 2, S_SIZE * 3 + S_SIZE // 2
        screen.blit(images["bQ"], rect)
        rect = images["bR"].get_rect()
        rect.center = S_SIZE * 3 + S_SIZE // 2, S_SIZE * 4 + S_SIZE // 2
        screen.blit(images["bR"], rect)
        rect = images["bR"].get_rect()
        rect.center = S_SIZE * 4 + S_SIZE // 2, S_SIZE * 3 + S_SIZE // 2
        screen.blit(images["bN"], rect)
        rect = images["bB"].get_rect()
        rect.center = S_SIZE * 4 + S_SIZE // 2, S_SIZE * 4 + S_SIZE // 2
        screen.blit(images["bB"], rect)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            elif event.type == p.MOUSEBUTTONDOWN:  # and (gs.whiteToMove and player_White):
                pos2 = p.mouse.get_pos()
                position_2 = (pos2[1] // S_SIZE, pos2[0] // S_SIZE)
                if position_2 == (3, 3):
                    run = False
                    return "bQ"
                elif position_2 == (3, 4):
                    run = False
                    return "bR"
                elif position_2 == (4, 3):
                    run = False
                    return "bN"
                elif position_2 == (4, 4):
                    run = False
                    return "bB"
            elif event.type == p.KEYDOWN:
                if event.key == p.K_u:
                    gs.undo()
                    gs.undo()
                    run = False

def in_game_sceen(screen):
    global colors
    global player_White
    screen.fill(p.Color((238, 213, 210)))
    color1 = [[p.Color('white'),p.Color('dark green')],[p.Color('white'),p.Color('grey')],[p.Color('white'),p.Color((0, 104, 139))],[p.Color('white'),p.Color((139, 26, 26))]]
    colors = color1[0]
    clock = p.time.Clock()
    pieces = [images["wK"],images['bK']]
    run = True
    background_image = p.image.load("phptqEYTs.png").convert()
    S_SIZE = 45
    y =x = 720//3
    cout = 0
    while run:
        screen.blit(background_image, (0, 0))
        p.draw.rect(screen, p.Color('black'), p.Rect(5 * S_SIZE - 5+x, 2 * S_SIZE - 5+x, S_SIZE + 10, S_SIZE + 10))
        p.draw.rect(screen, color1[cout][0], p.Rect(5 * S_SIZE+x, 2 * S_SIZE+x, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('black'), p.Rect(6 * S_SIZE+x - 5, 2 * S_SIZE-5+x, S_SIZE+10, S_SIZE+10))
        p.draw.rect(screen, color1[cout][1], p.Rect(6 * S_SIZE+x, 2 * S_SIZE+x, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('black'), p.Rect(5 * S_SIZE - 5+x, 3 * S_SIZE-5+x, S_SIZE+10, S_SIZE+10))
        p.draw.rect(screen, color1[cout][1], p.Rect(5 * S_SIZE+x, 3 * S_SIZE+x, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('black'), p.Rect(6 * S_SIZE- 5+x, 3 * S_SIZE-5+x, S_SIZE+10, S_SIZE+10))
        p.draw.rect(screen, color1[cout][0], p.Rect(6 * S_SIZE+x, 3 * S_SIZE+x, S_SIZE, S_SIZE))
        p.draw.rect(screen, p.Color('black'), p.Rect(5 * S_SIZE-5, 2 * S_SIZE + y + 20-5, S_SIZE + 60+10, S_SIZE+10))
        p.draw.rect(screen,p.Color((205, 16, 118)),p.Rect(5 * S_SIZE, 2 * S_SIZE+y+20, S_SIZE+60, S_SIZE))
        p.draw.rect(screen, p.Color('black'), p.Rect(5 * S_SIZE-5, S_SIZE + 80-5, S_SIZE + 60+10, S_SIZE+10))
        p.draw.rect(screen, p.Color((205, 16, 118)), p.Rect(5 * S_SIZE,  S_SIZE +80, S_SIZE + 60, S_SIZE))
        p.draw.rect(screen, p.Color('black'), p.Rect(WIDTH // 2 - 100 - 10, 720 - 200 - 10, 200 + 20, 100 + 20))
        p.draw.rect(screen, p.Color((205, 16, 118)), p.Rect(WIDTH//2-100, 720-200, 200, 100))
        img = pieces[1 if not player_White else 0]
        rect = img.get_rect()
        rect.center = (5 * S_SIZE+250,  S_SIZE +90)
        screen.blit(img, rect)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        # Set up fonts
        font = p.font.SysFont("arial", 15)  # You can specify a font file or use None for default fon
        text_surface = font.render("Change Board", True, BLACK)
        # Get the rect object that has the dimensions of the text surface
        text_rect = text_surface.get_rect()
        # Center the text
        text_rect.center = (5 * S_SIZE+(S_SIZE+60)//2,2 * S_SIZE+y+20+S_SIZE//2)
        # Blit the text surface onto the screen
        screen.blit(text_surface, text_rect)
        font1 = p.font.SysFont( "arial",42)  # You can specify a font file or use None for default fon
        text_surface1 = font1.render("CHESS GAME", True, BLACK)
        # Get the rect object that has the dimensions of the text surface
        text_rect1 = text_surface1.get_rect()
        # Center the text
        text_rect1.center = (WIDTH//2,42)
        # Blit the text surface onto the screen
        font2 = p.font.SysFont("arial", 15)  # You can specify a font file or use None for default fon
        text_surface2 = font2.render("Change Sides", True, BLACK)
        # Get the rect object that has the dimensions of the text surface
        text_rect2 = text_surface2.get_rect()
        # Center the text
        text_rect2.center = (5 * S_SIZE + (S_SIZE + 60) // 2, S_SIZE +80 + S_SIZE // 2)
        # Blit the text surface onto the screen
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface1, text_rect1)
        # Blit the text surface onto the screen
        font3 = p.font.SysFont("arial", 30)  # You can specify a font file or use None for default fon
        text_surface3 = font3.render("Play!", True, BLACK)
        # Get the rect object that has the dimensions of the text surface
        text_rect3 = text_surface3.get_rect()
        # Center the text
        text_rect3.center = (WIDTH//2-100 + 200 // 2, 720-200 + 100 // 2)
        # Blit the text surface onto the screen
        screen.blit(text_surface3, text_rect3)
        # Update the display
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:  # and (gs.whiteToMove and player_White):
                pos1 = p.mouse.get_pos()
                if pos1[0]>(5 * S_SIZE) and pos1[1]>(2 * S_SIZE+y+20) and pos1[0]<(5 * S_SIZE+S_SIZE+60) and pos1[1]<( 2 * S_SIZE+y+20+S_SIZE):
                    if cout<3:
                        cout+=1
                        colors = color1[cout]
                    else:
                        cout = 0
                        colors = color1[cout]
                if pos1[0] > (5 * S_SIZE) and pos1[1] > ( S_SIZE + 80) and pos1[0] < (5 * S_SIZE + S_SIZE + 60) and pos1[1] < ( S_SIZE + 80 + S_SIZE):
                    if player_White:
                        player_White = False
                    else:
                        player_White = True
                if pos1[0] > (WIDTH//2-100) and pos1[1] > (720-200) and pos1[0] < (WIDTH//2-100 + 200) and pos1[1] < ( 720-200 + 100):
                    run = False
        clock.tick(MAX_FPS)
        p.display.update()
        p.display.flip()

def load_img():
    pieces=["wR",'wN','wB','wQ','wK','wp',"bR",'bN','bB','bQ','bK','bp']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load(piece+".png"),(S_SIZE,S_SIZE))
def animateMove(move, screen, gs, clock):
    """
    Animating a move
    """
    colors = [p.Color('white'), p.Color('grey')]
    d_row = move[0][0] - move[1][0]
    d_col = move[0][1] - move[1][1]
    frames_per_square = 10  # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square
    for frame in range(frame_count + 1):
        row, col = (move[0][0]+ d_row * frame / frame_count, move[0][1] + d_col * frame / frame_count)
        draw_board(screen)
        draw_Pieces(screen, gs)
        # erase the piece moved from its ending square
        color = colors[(move[1][0] + move[1][1]) % 2]
        end_square = p.Rect(move[1][1] * S_SIZE, move[1][0] * S_SIZE, S_SIZE, S_SIZE)
        p.draw.rect(screen, color, end_square)
        # draw captured piece onto rectangle
        if gs.board[move[1][0]][move[1][1]] != '--':
            if len(move[1])>2 and move[1]!="oo":
                enpassant_row = move.end_row + 1 if move.piece_captured[0] == 'b' else move.end_row - 1
                end_square = p.Rect(move.end_col * S_SIZE, enpassant_row * S_SIZE, S_SIZE, S_SIZE)
            screen.blit(images[gs.board[move[1][0]][move[1][1]]], end_square)
        # draw moving piece
        screen.blit(images[gs.board[move[0][0]][move[0][1]]], p.Rect(col * S_SIZE, row * S_SIZE, S_SIZE, S_SIZE))
        p.display.flip()
        clock.tick(60)
def change_Pieces(pos1,pos2,screen):
    position_1 = (pos1[1]//S_SIZE,pos1[0]//S_SIZE)
    position_2 = (pos2[1]//S_SIZE,pos2[0]//S_SIZE)
    posible_moves = gs.get_all_posible_move()
    if (position_1,position_2) in posible_moves:
        gs.save_move_log(position_1,position_2)
        gs.board[position_2[0]][position_2[1]] = gs.board[position_1[0]][position_1[1]]
        gs.board[position_1[0]][position_1[1]] = "--"
        gs.whiteToMove = not gs.whiteToMove
        if gs.board[position_2[0]][position_2[1]] == "wK":
            gs.Wking_postion = position_2
        if gs.board[position_2[0]][position_2[1]] == "bK":
            gs.Bking_postion = position_2
        return (position_1,position_2)
    elif gs.board[position_1[0]][position_1[1]][1]=="K" and position_2 ==(position_1[0],position_1[1]+2) and (position_1,"oo") in posible_moves :
        gs.board[position_2[0]][position_2[1]] = gs.board[position_1[0]][position_1[1]]
        gs.board[position_1[0]][position_1[1]] = "--"
        gs.board[position_1[0]][position_1[1] + 1] = gs.board[position_1[0]][position_1[1]+3]
        gs.board[position_1[0]][position_1[1] + 3] = "--"
        gs.whiteToMove = not gs.whiteToMove
        if gs.board[position_2[0]][position_2[1]] == "wK":
            gs.Wking_postion = position_2
        if gs.board[position_2[0]][position_2[1]] == "bK":
            gs.Bking_postion = position_2
        gs.moveLog.push((position_1,"oo"))
        return (position_1,"oo")
    elif gs.board[position_1[0]][position_1[1]][1]=="K" and position_2 ==(position_1[0],position_1[1]-2) and (position_1,"o0o") in posible_moves :
        gs.board[position_2[0]][position_2[1]] = gs.board[position_1[0]][position_1[1]]
        gs.board[position_1[0]][position_1[1]] = "--"
        gs.board[position_1[0]][position_1[1]-1] = gs.board[position_1[0]][position_1[1]-4]
        gs.board[position_1[0]][position_1[1]-4] = "--"
        gs.whiteToMove = not gs.whiteToMove
        if gs.board[position_2[0]][position_2[1]] == "wK":
            gs.Wking_postion = position_2
        if gs.board[position_2[0]][position_2[1]] == "bK":
            gs.Bking_postion = position_2
        gs.moveLog.push((position_1,"o0o"))
        return (position_1, "o0o")
    elif gs.board[position_1[0]][position_1[1]][1]=="p" and position_1[0] == 6 and gs.board[position_1[0]][position_1[1]][0]=="b":
        if (position_1,(position_2[0],position_2[1],"bQ")) in posible_moves:
            mn = phong(screen,gs)
            position_2 = (position_2[0],position_2[1],mn)
            if position_2 in gs.check_move(position_1):
                gs.moveLog.push((position_1, position_2, gs.board[position_2[0][0]][position_2[0][1]]))
                gs.board[position_1[0]][position_1[1]] = "--"
                gs.board[position_2[0][0]][position_2[0][1]] = mn
                gs.whiteToMove = not gs.whiteToMove
                return (position_1,(position_2[0],position_2[1],mn))
    elif gs.board[position_1[0]][position_1[1]][1]=="p" and position_1[0] == 1 and gs.board[position_1[0]][position_1[1]][0]=="w":
        if (position_1,(position_2[0],position_2[1],"wQ")) in posible_moves:
            mn = phong(screen,gs)
            position_2 = (position_2[0],position_2[1],mn)
            if position_2 in gs.check_move(position_1):
                (gs.moveLog.push((position_1, position_2, gs.board[position_2[0]][position_2[1]])))
                gs.board[position_1[0]][position_1[1]] = "--"
                gs.board[position_2[0]][position_2[1]] = mn
                gs.whiteToMove = not gs.whiteToMove
                return (position_1, (position_2[0], position_2[1], mn))
    elif (position_1,(position_2[0],position_2[1],"wp")) in posible_moves:
        gs.moveLog.push((position_1,(position_2[0],position_2[1],"wp"),"bp"))
        gs.board[position_2[0]][position_2[1]] = gs.board[position_1[0]][position_1[1]]
        gs.board[position_1[0]][position_1[1]] = "--"
        gs.board[position_1[0]][position_2[1]] ="--"
        gs.whiteToMove = not gs.whiteToMove
        return (position_1, (position_2[0], position_2[1], "wp"))
    elif (position_1,(position_2[0],position_2[1],"bp")) in posible_moves:
        gs.moveLog.push((position_1, (position_2[0], position_2[1], "bp"), "wp"))
        gs.board[position_2[0]][position_2[1]] = gs.board[position_1[0]][position_1[1]]
        gs.board[position_1[0]][position_1[1]] = "--"
        gs.board[position_1[0]][position_2[1]] = "--"
        gs.whiteToMove = not gs.whiteToMove
        return (position_1, (position_2[0], position_2[1], "bp"))
def draw_board(screen):
    for x in range(DIM):
        for y in range(DIM):
            color = colors[(x + y) % 2]
            p.draw.rect(screen,color,p.Rect(x*S_SIZE,y*S_SIZE,S_SIZE,S_SIZE))
def draw_board1(screen,pos1):
    position_1 = (pos1[1] // S_SIZE, pos1[0] // S_SIZE)
    a = gs.get_all_posible_move()
    colors1 = [p.Color((123, 104, 238)),p.Color(255, 228, 225),p.Color(151, 255, 255)]
    for x in range(DIM):
        for y in range(DIM):
            color = colors[(x + y) % 2]
            if (position_1,(y,x)) in a and (x+y)%2 ==0:
                p.draw.rect(screen, colors1[2], p.Rect(x * S_SIZE, y * S_SIZE, S_SIZE, S_SIZE))
            elif (position_1,(y,x)) in a and (x+y)%2 ==1:
                p.draw.rect(screen, colors1[1], p.Rect(x * S_SIZE, y * S_SIZE, S_SIZE, S_SIZE))
            elif (y,x) ==position_1:
                p.draw.rect(screen,colors1[0],p.Rect(x*S_SIZE,y*S_SIZE,S_SIZE,S_SIZE))
            else:
                p.draw.rect(screen, color, p.Rect(x * S_SIZE, y * S_SIZE, S_SIZE, S_SIZE))
def draw_Pieces(screen,gs):
    for x in range(len(gs)):
        for y in range(len(gs[x])):
            if gs[x][y] != '--':
                rect = images[gs[x][y]].get_rect()
                rect.center = S_SIZE*y+S_SIZE//2,S_SIZE*x+S_SIZE//2
                screen.blit(images[gs[x][y]],rect)
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    run = True
    load_img()
    get = True
    in_game_sceen(screen)
    while run:
        if gs.is_checkmate():
            draw_board(screen)
            draw_Pieces(screen,gs.board)
            font = p.font.SysFont("arial", 42)  # You can specify a font file or use None for default fon
            if gs.whiteToMove:
                text_surface = font.render("Black Win !!!", True, 'black')
            else:
                text_surface = font.render("White Win !!!", True, 'black')

            # Get the rect object that has the dimensions of the text surface
            text_rect = text_surface.get_rect()
            # Center the text
            text_rect.center = (HEIGHT//2,WIDTH//2)
            # Blit the text surface onto the screen
            screen.blit(text_surface, text_rect)
        elif gs.is_stalemate():
            draw_board(screen)
            draw_Pieces(screen, gs.board)
            font = p.font.SysFont("arial", 42)  # You can specify a font file or use None for default fon
            text_surface = font.render("stalemate !!!", True, 'black')
            # Get the rect object that has the dimensions of the text surface
            text_rect = text_surface.get_rect()
            # Center the text
            text_rect.center = (HEIGHT // 2, WIDTH // 2)
        else:
            if get == False:
                draw_board1(screen,pos1)
                draw_Pieces(screen, gs.board)
            else:
                draw_board(screen)
                draw_Pieces(screen, gs.board)
            if player_White != gs.whiteToMove:
               jfk = find_next_move.findBestMove(gs,gs.get_all_posible_move())
               if jfk is not None:
                    gs.change_Pieces(jfk)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN: #and (gs.whiteToMove and player_White):
                if get == True:
                    pos1 = p.mouse.get_pos()
                    get = False
                else:
                   if player_White == gs.whiteToMove:
                        pos2 = p.mouse.get_pos()
                        move = change_Pieces(pos1,pos2,screen)
                        get = True
                        draw_board(screen)
                        draw_Pieces(screen, gs.board)
                        print(gs.Bking_postion)
                        print(gs.Wking_postion)
            elif event.type == p.KEYDOWN:
                if event.key == p.K_u:
                    gs.undo()
                    gs.undo()
        clock.tick(MAX_FPS)
        p.display.update()
        p.display.flip()
    p.quit()
if __name__ == "__main__":
    main()

