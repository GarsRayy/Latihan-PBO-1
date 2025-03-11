import random

class Robot:
    def __init__(self, nama, hp, attack, skill_name, skill_power, accuracy):
        self.nama = nama
        self.hp = hp
        self.attack = attack
        self.defense = False
        self.skill_name = skill_name
        self.skill_power = skill_power
        self.skill_used = False  # Menandai apakah skill sudah digunakan
        self.accuracy = accuracy  # Akurasi serangan dalam persentase (0-1)
        self.stunned = 0  # Durasi stun
        self.silenced = 0  # Durasi silence
    
    def attack_enemy(self, enemy):
        if self.stunned > 0:
            print(f"{self.nama} sedang terkena STUN dan tidak bisa menyerang!")
            return
        
        if random.random() <= self.accuracy:  # Cek apakah serangan berhasil
            damage = self.attack // 2 if enemy.defense else self.attack
            enemy.hp -= damage
            print(f"{self.nama} menyerang {enemy.nama} dengan kekuatan {damage}. HP {enemy.nama} tersisa: {enemy.hp}")
        else:
            print(f"{self.nama} gagal menyerang!")
    
    def use_skill(self, enemy):
        if self.stunned > 0:
            print(f"{self.nama} sedang terkena STUN dan tidak bisa menggunakan skill!")
            return
        
        if self.silenced > 0:
            print(f"{self.nama} sedang terkena SILENCE dan tidak bisa menggunakan skill!")
            return
        
        if not self.skill_used:
            enemy.hp -= self.skill_power
            self.skill_used = True
            
            if random.random() <= 0.5:
                enemy.stunned = 2  # 50% chance stun musuh selama 2 ronde
            if random.random() <= 0.5:
                enemy.silenced = 2  # 50% chance silence musuh selama 2 ronde
            
            print(f"{self.nama} menggunakan skill {self.skill_name}! {enemy.nama} kehilangan {self.skill_power} HP.")
            if enemy.stunned > 0:
                print(f"{enemy.nama} terkena STUN dan tidak bisa bergerak!")
            if enemy.silenced > 0:
                print(f"{enemy.nama} terkena SILENCE dan tidak bisa menggunakan skill!")
        else:
            print(f"{self.nama} sudah menggunakan skill dan tidak bisa menggunakannya lagi!")
    
    def defend(self):
        self.defense = True
        print(f"{self.nama} memilih bertahan! Serangan musuh akan berkurang 50%.")
    
    def is_alive(self):
        return self.hp > 0
    
    def reset_status(self):
        """Mengurangi durasi stun dan silence setelah setiap ronde."""
        if self.stunned > 0:
            self.stunned -= 1
        if self.silenced > 0:
            self.silenced -= 1
        self.defense = False  # Reset status bertahan setiap ronde

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
    
    def start_battle(self):
        round_num = 1
        while self.robot1.is_alive() and self.robot2.is_alive():
            print(f"\nRound-{round_num} ==================================================")
            print(f"{self.robot1.nama} [HP: {self.robot1.hp}] - Skill: {self.robot1.skill_name}")
            print(f"{self.robot2.nama} [HP: {self.robot2.hp}] - Skill: {self.robot2.skill_name}")
            
            actions = {}
            for robot in [self.robot1, self.robot2]:
                if robot.stunned > 0:
                    print(f"{robot.nama} tidak bisa bergerak karena STUN!")
                    continue  # Lewati aksi jika robot stun
                
                while True:
                    try:
                        print("\n1. Attack     2. Defense     3. Use Skill     4. Give up")
                        choice = int(input(f"{robot.nama}, pilih aksi: "))
                        if choice in [1, 2, 3, 4]:
                            actions[robot] = choice
                            break
                        else:
                            print("Masukkan angka yang benar!")
                    except ValueError:
                        print("Masukkan angka valid!")
            
            for robot in [self.robot1, self.robot2]:
                if robot in actions:
                    choice = actions[robot]
                    enemy = self.robot2 if robot == self.robot1 else self.robot1
                    
                    if choice == 1:
                        robot.attack_enemy(enemy)
                    elif choice == 2:
                        robot.defend()
                    elif choice == 3:
                        robot.use_skill(enemy)
                    elif choice == 4:
                        print(f"\n{robot.nama} menyerah!")
                        print(f"{enemy.nama} menang!")
                        return
            
            self.robot1.reset_status()
            self.robot2.reset_status()
            round_num += 1
        
        winner = self.robot1 if self.robot1.is_alive() else self.robot2
        print(f"\n{winner.nama} menang!")

# Input nama robot
nama1 = input("Masukkan nama Robot 1: ")
nama2 = input("Masukkan nama Robot 2: ")

# Inisialisasi dua robot dengan skill dan accuracy
robot1 = Robot(nama1, hp=500, attack=10, skill_name="Mega Blast", skill_power=50, accuracy=0.85)
robot2 = Robot(nama2, hp=750, attack=8, skill_name="Thunder Strike", skill_power=40, accuracy=0.75)

# Memulai permainan
game = Game(robot1, robot2)
game.start_battle()
