import pygame
import math
import random
from pygame.locals import *
from sys import exit

class Castle:
    """
    Xây dựng đối tượng pháo đài, một lớp đối tượng cấu tạo nên trò chơi.
        Thuộc tính:
            healthValue (kiểu dữ liệu: số nguyên): lượng máu trong chống chịu của pháo đài
            health + healthBar (kiểu dữ liệu: hình ảnh): giao diện máu của pháo đài
            image (kiểu dữ liệu: hình ảnh): giao diện pháo đài
        Phương thức:
            damageRec(): xem chi tiết ở __doc__ của phương thức này
            display(): xem chi tiết ở __doc__ của phương thức này
    """
    healthValue = 200
    image = pygame.image.load("images/Castle.png")
    healthBar = pygame.image.load("images/HealthBar.png")
    health = pygame.image.load("images/Health.png")
    def damageRec(self,enemy,index):
        """
        Phương thức tạo hiệu ứng giảm từ 3 đến 10 máu cũng như tính toán giá trị của thuộc tính healthValue của pháo đài khi bị tấn công.
            Tham số truyền vào:
                enemy (kiểu dữ liệu: Enemy): đối tượng quân địch
                index (kiểu dữ liệu: số nguyên): chỉ số của quân địch đó trong list quân địch nhằm xóa quân địch đó sau khi chạm vào pháo đài
            Kết quả trả về:
                Lượng máu pháo đài được hiển thị giảm và quân địch đã va vào pháo đài sẽ biến mất
        """
        self.healthValue -= random.randint(3,10)
        enemy.enemies.pop(index)
        if self.healthValue > 0:
            self.health = pygame.transform.scale(self.health,(self.healthValue,14))
            screen.blit(self.health,(8,8))
        else:
            screen.blit(self.healthBar,(5,5))
    def display(self):
        """
        Xuất các thuộc tính của pháo đài lên màn hình.
        """
        screen.blit(self.image, (0,450))
        screen.blit(self.healthBar,(5,5))
        screen.blit(self.health,(8,8))
        font = pygame.font.Font(None, 24)
        text = font.render("Castle", True, (0,0,0))
        screen.blit(text,(220,5))

class Player:
    """
    Xây dựng đối tượng người chơi, một lớp đối tượng cấu tạo nên trò chơi.
        Thuộc tính:
            pos (kiểu dữ liệu: list): vị trí của người chơi
            keys (kiểu dữ liệu: list): xác định những phím di chuyển nào đã được bấm bởi người chơi
            healthValue (kiểu dữ liệu: số nguyên): lượng máu trong chống chịu của người chơi
            health + healthBar (kiểu dữ liệu: hình ảnh): giao diện máu của người chơi
            image (kiểu dữ liệu: hình ảnh): giao diện người chơi
        Phương thức:
            rotate(): xem chi tiết ở __doc__ của phương thức này
            display(): xem chi tiết ở __doc__ của phương thức này
            catchEventMove(): xem chi tiết ở __doc__ của phương thức này
            move(): xem chi tiết ở __doc__ của phương thức này
            damageRec(): xem chi tiết ở __doc__ của phương thức này

    """
    def __init__(self,pos,keys):
        self.pos=pos
        self.keys=keys
    healthValue = 200
    image=pygame.image.load("images/Archer.png")
    image=pygame.transform.scale(image,(60,60))
    healthBar = pygame.image.load("images/HealthBar.png")
    health = pygame.image.load("images/Health.png")
    def rotate(self):
        """
        Xoay nhân vật theo con trỏ chuột.
            Kết quả trả về:
                playerrot (kiểu dữ liệu: hình ảnh): hình ảnh nhân vật đã được xoay theo hướng của con trỏ chuột
                newPos (kiểu dữ liệu: list): vị trí mới của hình ảnh nhân vật sau khi xoay theo con trỏ chuột
        """
        position=pygame.mouse.get_pos()
        angle=math.atan2(position[1]-self.pos[1],position[0]-self.pos[0])
        playerrot=pygame.transform.rotate(self.image, 360 - angle*180/3.14)
        newPos=[self.pos[0]-playerrot.get_rect().width/2, self.pos[1]-playerrot.get_rect().height/2]
        return playerrot, newPos
    def display(self):
        """Xuất các thuộc tính của nhân vật lên màn hình."""
        playerrot, newPos=self.rotate()
        screen.blit(playerrot,newPos)
        screen.blit(self.healthBar,(5,35))
        screen.blit(self.health,(8,38))
        font = pygame.font.Font(None, 24)
        text = font.render("You", True, (0,0,0))
        screen.blit(text,(220,35))
    def catchEventMove(self,event):
        """
        Bắt sự kiện di chuyển.
            Tham số truyền vào:
                event (kiểu dữ liệu: sự kiện): sự kiện bấm các nút trên bàn phím đã xảy ra
            Kết quả trả về:
                keys (kiểu dữ liệu: list): trả về danh sách xác định những phím di chuyển nào đã được bấm bởi người chơi
        """
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                self.keys[0]=True
            if event.key==K_s:
                self.keys[1]=True
            if event.key==K_a:
                self.keys[2]=True
            if event.key==K_d:
                self.keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                self.keys[0]=False
            if event.key==pygame.K_s:
                self.keys[1]=False
            if event.key==pygame.K_a:
                self.keys[2]=False
            if event.key==pygame.K_d:
                self.keys[3]=False
        return self.keys
    def move(self,keys):
        """
        Di chuyển nhân vật.
            Tham số truyền vào:
                keys (kiểu dữ liệu: list): danh sách xác định những phím di chuyển nào đã được bấm bởi người chơi
            Kết quả trả về:
                pos (kiểu dữ liệu: list): vị trí của người chơi sau khi di chuyển
        """
        self.keys=keys
        if keys[0]:
            self.pos[1]-=5
        if keys[1]:
            self.pos[1]+=5
        if keys[2]:
            self.pos[0]-=5
        if keys[3]:
            self.pos[0]+=5
        return self.pos
    def damageRec(self,enemy,index):
        """
        Phương thức tạo hiệu ứng giảm từ 15 đến 25 máu cũng như tính toán giá trị của thuộc tính healthValue của người chơi khi bị tấn công.
            Tham số truyền vào:
                enemy (kiểu dữ liệu: Enemy): đối tượng quân địch
                index (kiểu dữ liệu: số nguyên): chỉ số của quân địch đó trong list quân địch nhằm xóa quân địch đó sau khi chạm vào người chơi
            Kết quả trả về:
                Lượng máu người chơi được hiển thị giảm và quân địch đã va vào người chơi sẽ biến mất
        """
        self.healthValue -= random.randint(15,25)
        enemy.enemies.pop(index)
        if self.healthValue > 0:
            self.health = pygame.transform.scale(self.health,(self.healthValue,14))
            screen.blit(self.health,(8,38))
        else:
            screen.blit(self.healthBar,(5,35))

class Arrow:
    """
    Xây dựng đối tượng mũi tên, một lớp đối tượng cấu tạo nên trò chơi.
        Thuộc tính:
            accuracy (kiểu dữ liệu: list): danh sách lưu lại ố tên trúng đích & tổng số tên đã bắn
            arrows (kiểu dữ liệu: list): có thể hình dung đơn giản là túi tên chứ các mũi tên
            image (kiểu dữ liệu: hình ảnh): giao diện mũi tên
            shootS (kiểu dữ liệu: âm thanh): âm thanh của tiếng bắn tên
        Phương thức:
            catchEventShoot(): xem chi tiết ở __doc__ của phương thức này
            shoot(): xem chi tiết ở __doc__ của phương thức này
            kill(): xem chi tiết ở __doc__ của phương thức này
    """
    pygame.mixer.init()
    accuracy=[0,0]
    arrows=[]
    image=pygame.image.load("images/Arrow.png")
    image=pygame.transform.scale(image,(24,15))
    shootS=pygame.mixer.Sound("sounds/shoot.wav")
    shootS.set_volume(0.25)
    def __init__(self):
        self.arrows=[]
        self.accuracy=[0,0]
    def catchEventShoot(self,event,player):
        """
        Bắt sự kiện click chuột để bắn tên.
            Tham số truyền vào:
                event (kiểu dữ liệu: sự kiện): sự kiện click chuột để bắn của người chơi
                player (kiểu dữ liệu: Player): dùng để truy cập giá trị thuộc tính vị trí của nhân vật để hiển thị vị trí mũi tên được bắn ra
            Kết quả trả về:
                arrows (kiểu dữ liệu: list): trả về túi tên đã được thêm mũi tên vừa được bắn với các giá trị chứa trong mũi tên gồm "góc bắn tên", "tọa độ x ban đầu", "tọa độ y ban đầu"
        """
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            self.accuracy[1]+=1
            self.arrows.append([math.atan2(position[1]-player.pos[1],position[0]-player.pos[0]),player.pos[0],player.pos[1]])
            self.shootS.play()
        return self.arrows
    def shoot(sefl):
        """
        Bắn tên.
            Kết quả trả về:
                Xuất ra màn hình hoạt ảnh mũi tên đã bắn dựa vào các giá trị chứa trong mũi tên đó gồm "góc bắn tên", "tọa độ x ban đầu", "tọa độ y ban đầu"
        """
        for arrow in sefl.arrows:
            index=0
            posX=math.cos(arrow[0])*15
            posY=math.sin(arrow[0])*15
            arrow[1]+=posX
            arrow[2]+=posY
            if arrow[1]<-40 or arrow[1]>400 or arrow[2]<-40 or arrow[2]>720:
                sefl.arrows.pop(index)
            index+=1
            arrow1=pygame.transform.rotate(sefl.image, 360-arrow[0]*180/3.14)
            screen.blit(arrow1, (arrow[1], arrow[2]))
    def kill(sefl,enemy,index,index1):
        """
        Hạ gục quân địch.
            Tham số truyền vào:
                enemy (kiểu dữ liệu: Enemy): đối tượng quân địch
                index (kiểu dữ liệu: số nguyên): chỉ số của quân địch đó trong list quân địch nhằm xóa quân địch đó sau khi bị trúng tên
                index1 (kiểu dữ liệu: số nguyên): chỉ số của mũi tên đã bắn trong túi tên nhằm xóa mũi tên đó sau khi hạ quân địch
            Kết quả trả về:
                Làm mất quân địch và mũi tên đã bắn quân địch đó khỏi màn hình
        """
        sefl.accuracy[0]+=1
        enemy.enemies.pop(index)
        sefl.arrows.pop(index1)

class Enemy:
    """
    Xây dựng đối tượng quân địch, một lớp đối tượng cấu tạo nên trò chơi.
        Thuộc tính:
            enemies (kiểu dữ liệu: list): danh sách quân địch đã xuất hiện
            max (kiểu dữ liệu: số nguyên): số lượng quân địch tối đa xuất hiện trên màn hình
            appeared (kiểu dữ liệu: số nguyên): số lượng quân địch đã xuất hiện trên màn hình
            remaining (kiểu dữ liệu: số nguyên): số lượng quân địch còn lại có thể xuất hiện trên màn hình
            image (kiểu dữ liệu: hình ảnh): giao diện quân địch
            hit, boom, scream (kiểu dữ liệu: âm thanh): âm thanh của những va chạm và tiếng hét của quân địch khi bị trúng tên
        Phương thức:
            randomAppear(): xem chi tiết ở __doc__ của phương thức này
    """
    pygame.mixer.init()
    enemies=[]
    max=100
    appeared=0
    remaining = max - appeared
    image=pygame.image.load("images/Enemy.png")
    hit=pygame.mixer.Sound("sounds/hit.wav")
    hit.set_volume(0.25)
    boom=pygame.mixer.Sound("sounds/boom.wav")
    boom.set_volume(0.25)
    scream=pygame.mixer.Sound("sounds/scream.wav")
    scream.set_volume(0.25)
    def __init__(self):
        self.enemies=[]
    def randomAppear(self,arrow,castle,player):
        """
        Tạo địch xuất hiện ngẫu nhiên.
            Tham số truyền vào:
                arrow (kiểu dữ liệu: Arrow): đối tượng mũi tên
                castle (kiểu dữ liệu: Castle): đối tượng pháo đài
                player (kiểu dữ liệu: Player): đối tượng nhân vật người chơi
            Kết quả trả về:
                Quân địch xuất hiện ngẫu nhiên ở mỗi số vị trí và lao về phía pháo đài. Quân địch sẽ biến mất nếu chạm vào pháo đài hoặc nhân vật người chơi hoặc bị trúng tên
        """
        if self.remaining == 0:
            self.enemies.append([random.randint(20,350),0])
            self.remaining = self.max - (self.appeared*2)
            if self.appeared>=35:
                self.appeared=35
            else:
                self.appeared+=5
        index=0
        for enemy in self.enemies:
            enemy[1]+=7
            # Kiểm tra chạm trúng pháo đài
            enemyrect=pygame.Rect(self.image.get_rect())
            enemyrect.top=enemy[1]
            enemyrect.left=enemy[0]
            if enemyrect.bottom>500:
                castle.damageRec(self,index)
                self.boom.play()
            # Kiểm tra trúng tên
            index1=0
            for arrowS in arrow.arrows:
                arrowrect=pygame.Rect(arrow.image.get_rect())
                arrowrect.left=arrowS[1]
                arrowrect.top=arrowS[2]
                if enemyrect.colliderect(arrowrect):
                    arrow.kill(self,index,index1)
                    self.hit.play()
                    self.scream.play()
                index1+=1
            # Kiểm tra va chạm người chơi
            playerrect=pygame.Rect(player.image.get_rect())
            playerrect.top=player.pos[1]
            playerrect.left=player.pos[0]
            if enemyrect.colliderect(playerrect):
                player.damageRec(self,index)
                self.scream.play()
            # Quân địch tiếp theo
            index+=1
        for enemy in self.enemies:
            screen.blit(self.image, enemy)
        self.remaining-=1

def displayClock(timer):
    """
    Hiển thị đồng hồ đếm ngược thời gian còn lại phải phòng thủ.
        Tham số truyền vào:
            timer (kiểu dữ liệu: số nguyên): Tổng thời gian phòng thủ mà người chơi đã nhập (hoặc mặc định là 90 giây nếu không nhập)
    """
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((timer-pygame.time.get_ticks())//60000)+":"+str((timer-pygame.time.get_ticks())//1000%60).zfill(2)+":"+str((timer-pygame.time.get_ticks())%1000), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[400,5]
    screen.blit(survivedtext, textRect)

def checkEnd(castle,player,timer):
    """
    Kiểm tra điều kiện kết thúc.
        Tham số truyền vào:
            player (kiểu dữ liệu: Player): đối tượng nhân vật người chơi
            timer (kiểu dữ liệu: số nguyên): Tổng thời gian phòng thủ mà người chơi đã nhập (hoặc mặc định là 90 giây nếu không nhập)
        Kết quả trả về:
            running (kiểu dữ liệu: số nguyên): chỉ nhận giá trị 1 và 0 tương ứng "True" và "False" để kết thúc vòng lặp sự kiện game
            exitcode (kiểu dữ liệu: số nguyên): nhận giá trị 1 tương ứng chiến thắng hoặc 0 tương ứng với thất bại
    """
    running = 1
    exitcode = 2
    if pygame.time.get_ticks()>=timer:
        running=0
        exitcode=1
    if castle.healthValue<=0 or player.healthValue<=0:
        running=0
        exitcode=0
    return running, exitcode

def end(exitcode,arrow,castle,timer):
    """
    Dừng trò chơi.
        Tham số truyền vào:
            exitcode (kiểu dữ liệu: số nguyên): dùng để xác định đã thỏa điều kiện kết thúc trò chơi hay chưa
            arrow (kiểu dữ liệu: Arrow): đối tượng mũi tên dùng để truy cập thuộc tính accuracy từ đó xác định tỉ lệ bắn chính xác của người chơi
            castle (kiểu dữ liệu: Castle): đối tượng pháo đài dùng để truy cập thuộc tính healthValue từ đó xác định mức độ hư hại của pháo đài
            timer (kiểu dữ liệu: số nguyên): Tổng thời gian phòng thủ mà người chơi đã nhập (hoặc mặc định là 90 giây nếu không nhập)
        Kết quả trả về:
            Xuất ra màn hình kết thúc game nếu thỏa điều kiện kết thúc bao gồm thông báo Thắng-Thua và tỉ lệ chính xác
            Nếu chiến thắng các thông tin được xuất sẽ bao gồm thêm mức độ thiệt hại của pháo đài từ đó làm cơ sở để người chơi so sánh với nhau
    """
    # Khởi tạo phông nền Win
    win=pygame.image.load("images/BackgroundWin.png")
    # Khởi tạo phông nền Lose
    lose=pygame.image.load("images/BackgroundLose.png")
    playAgain=pygame.image.load("images/PlayAgain.png")
    playAgain=pygame.transform.scale(playAgain,(150,70))
    backToMenu=pygame.image.load("images/BackToMenu.png")
    backToMenu=pygame.transform.scale(backToMenu,(150,70))
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    if arrow.accuracy[1]!=0:
        accuracy=arrow.accuracy[0]*1.0/arrow.accuracy[1]*100
    else:
        accuracy=0
    text = font.render("Accuracy: "+str(round(accuracy,2))+"%", True, (255,255,0))
    if exitcode==0:
        screen.blit(lose, (0,0))
    else:
        screen.blit(win, (0,0))
        text2 = font.render("Castle's health: "+str(castle.healthValue), True, (255,255,0))
        text2Rect = text.get_rect()
        text2Rect.centerx = screen.get_rect().centerx-12
        text2Rect.centery = screen.get_rect().centery+36
        screen.blit(text2, text2Rect)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+12
    screen.blit(text, textRect)
    screen.blit(playAgain,(250,40))
    screen.blit(backToMenu,(250,120))
    playAgBtnRect = playAgain.get_rect()
    playAgBtnRect.top = 40
    playAgBtnRect.left = 250
    btmBtnRect = backToMenu.get_rect()
    btmBtnRect.top = 120
    btmBtnRect.left = 250
    mouse=[]
    while 1:
        if mouse:
            if playAgBtnRect.collidepoint(mouse):
                timer1 = timer+pygame.time.get_ticks()
                start(timer,timer1)
            if btmBtnRect.collidepoint(mouse):
                menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
        pygame.display.flip()

class InputBox:
    """
    Xây dựng đối tượng ô nhập dữ liệu, một lớp đối tượng dùng để lấy giá trị thời gian người chơi muốn thử thách.
        Thuộc tính:
            text_typed (kiểu dữ liệu: chuỗi): dùng để lưu chuỗi ký tự người chơi đã nhập (ở đây người chơi cần nhập một con số, 
                nếu nhập sai thì thời gian sẽ lấy giá trị theo các ký tự số hợp lệ đầu tiên từ trái sang,
                cuối cùng mặc định là 90 giây nếu chuỗi nhập bắt đầu bằng 1 ký tự không phải số)
            COLOR_INACTIVE (kiểu dữ liệu: màu sắc): màu sắc của ô nhập khi bất hoạt
            COLOR_ACTIVE (kiểu dữ liệu: màu sắc): màu sắc của ô nhập khi được click vào để nhập
            rect (kiểu dữ liệu: Rect): xác định vị trí cũng như kích thước ô nhập
            color (kiểu dữ liệu: màu sắc): màu sắc của ô nhập
            text (kiểu dữ liệu: chuỗi): chuỗi người chơi đang nhập
            txt_surface (kiểu dữ liệu: chuỗi): dùng để hiển thị những gì người chơi đã nhập lên màn hình
            active (kiểu dữ liệu: bool): dùng để xác định người dùng đã click vào ô nhập hay chưa
        Phương thức:
            handle_event(): xem chi tiết ở __doc__ của phương thức này
            draw(): xem chi tiết ở __doc__ của phương thức này
    """
    text_typed = ""
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, self.color)
        self.active = False
    def handle_event(self, event):
        """
        Xử lý sự kiện click và nhập input của người chơi.
        Tham số truyền vào:
            event (kiểu dữ liệu: sự kiện): dùng để xác định sự kiện từ chuột và bàn phím đã xảy ra bởi tác động của người chơi
        Kết quả trả về:
            Xuất ra màn hình những gì người chơi đã nhập cũng như lưu lại giá trị đó
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra người dùng click vào ô nhập
            if self.rect.collidepoint(event.pos):
                # Kích hoạt trạng thái ô nhập
                self.active = not self.active
            else:
                self.active = False
            # Chuyển màu của ô nhập để người dùng biết có thể bắt đầu nhập được chưa
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_typed=self.text
                # Trích xuất đoạn text người dùng đã nhập
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)
    def draw(self, screen):
        """
        Xuất ra màn hình ô nhập dữ liệu và chuỗi ký tự người chơi đã nhập.
        """
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

def start(timer,timer1):
    """
    Hàm thực thi trò chơi.
        Tham số truyền vào:
            timer (kiểu dữ liệu: số nguyên): chứa giá trị thời gian người chơi muốn thử thách
                dùng để truyền vào phương thức end() được gọi bên trong phương thức này
            timer1 (kiểu dữ liệu: số nguyên): là giá trị thời gian người chơi muốn thử thách sau khi cộng thêm giá trị thời gian dùng để chờ nhập dữ liệu
                dùng để truyền vào phương thức displayClock() và checkEnd()
        Kết quả trả về:
            Xuất ra màn hình chơi game
    """
    # Khởi tạo phông nền
    background=pygame.image.load("images/Background.png")
    # Khởi tạo pháo đài
    castle=Castle()
    # Khởi tạo người chơi
    pos=[200,400]
    keys=[False, False, False, False]
    player=Player(pos,keys)
    # Khởi tạo vũ khí
    weapon=Arrow()
    # Khởi tạo quân địch
    enemy = Enemy()
    running = 1
    while running:
        screen.fill(0)
        screen.blit(background, (0,0))
        displayClock(timer1)
        castle.display()
        player.display()
        player.pos=player.move(player.keys)
        weapon.shoot()
        enemy.randomAppear(weapon,castle,player)
        pygame.display.flip()
        # Vòng lặp các sự kiện xuất hiện trong quá trình chơi game
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0)
            # Bắt sự kiện thao tác phím để di chuyển nhân vật
            player.keys=player.catchEventMove(event)
            # Bắt sự kiện thao tác chuột để bắn
            weapon.arrows=weapon.catchEventShoot(event,player)
        pygame.display.update()
        fpsClock.tick(60)
        running, exitcode = checkEnd(castle,player,timer1)
        if running==0:
            end(exitcode,weapon,castle,timer)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.flip()

def menu():
    """
    Hàm xuất ra màn hình Menu trò chơi.
    """
    # Khởi tạo phông nền menu
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.2)
    backgroundStart=pygame.image.load("images/BackgroundStart.png")
    inputBG=pygame.image.load("images/inputBG.png")
    inputBG=pygame.transform.scale(inputBG,(350,300))
    inputTextBG=pygame.image.load("images/inputTextBG.png")
    playButton=pygame.image.load("images/StartButton.png")
    playButton=pygame.transform.scale(playButton,(200,100))
    quitButton=pygame.image.load("images/QuitButton.png")
    quitButton=pygame.transform.scale(quitButton,(200,100))
    inputBox = InputBox(100, 200, 200, 32)
    screen.blit(backgroundStart,(0,0))
    screen.blit(inputBG,(25,0))
    screen.blit(inputTextBG,(100,200))
    screen.blit(playButton,(100,300))
    screen.blit(quitButton,(100,450))
    playBtnRect = playButton.get_rect()
    playBtnRect.top = 300
    playBtnRect.left = 100
    quitBtnRect = quitButton.get_rect()
    quitBtnRect.top = 450
    quitBtnRect.left = 100
    timer=90000
    mouse=[]
    while 1:
        inputBox.draw(screen)
        if inputBox.text_typed != "" and inputBox.text_typed.isdecimal():
            timer = int(inputBox.text_typed)*1000
        if mouse:
            if playBtnRect.collidepoint(mouse):
                timer1 = timer+pygame.time.get_ticks()
                start(timer,timer1)
            if quitBtnRect.collidepoint(mouse):
                pygame.quit()
                exit(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
            inputBox.handle_event(event)
        pygame.display.flip()

fpsClock = pygame.time.Clock()
#Khởi tạo màn hình game
pygame.init()
pygame.display.set_caption("Game Thủ Thành")
icon=pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
width, height=400, 720
screen=pygame.display.set_mode((width, height))
menu()
    