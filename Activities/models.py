from django.db import models
from Player.models import player
import random

class activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.BigIntegerField()
    reward = models.BigIntegerField()

    def receive_reward(self, player):
        player.money += self.reward
        player.xp += self.reward
        player.save()

    def pay_cost(self, player):
        if player.money >= self.cost:
            player.money -= self.cost
            player.save()
        else:
            return False

    def victory(self, player):
        self.receive_reward(player)

    def giveback_money(self, player):
        player.money += self.cost
        player.save()

    def RPS(self, player):
        self.pay_cost(player)
        computer = random.randint(1, 3)
        player = input("Rock", "Paper", "Scissor" "?") #Moet nog aangepast worden qua input
        if player == "Rock" and computer != 1:
            if player == "Rock" and computer == 2:
                return "Paper covers Rock, Computer wins"
            elif player == "Rock" and computer == 3:
                self.victory(player)
                return "Rock smashes Scissors, U win"
            else:
                return "U selected the wrong name"
        elif player == "Paper" and computer != 2:
            if player == "Paper" and computer == 1:
                self.victory(player)
                return "Paper covers Rock, U win"
            elif player == "Paper" and computer == 3:
                return "Scissors cuts through Paper, Computer wins"
            else:
                return "U selected the wrong name"
        elif player == "Scissor" and computer != 3:
            if player == "Scissor" and computer == 1:
                return "Rock smashes Scissors, Computer wins"
            elif player == "Scissor" and computer == 2:
                self.victory(player)
                return "Scissors cuts through paper, U win"
        elif player == "Rock" and computer == 1 or player == "Paper" and computer == 2 or player == "Scissor" and computer == 3:
            self.giveback_money(player)
            return "It is a tie"
        else:
            self.RPS(player)
            return "U chose a invalid option" # Hier moet nog gefixt worden
        player.save()
