import random
import classPlayer
import classVilager
import classKiller
import classDoc
import classSeer
import classFool
import classGossipGirl
import time

def seer_move(players):
    for classPlayer.Player in players:
        if classPlayer.Player.role == "Seer" and classPlayer.Player.alive and classPlayer.Player.gossip == 0:
            vote_to_see = input(f"{classPlayer.Player.name} choose who to SEE: ")
            if any(classPlayer.Player.name == vote_to_see for classPlayer.Player in players):
                if classPlayer.Player.role == "Killer" and classPlayer.Player.alive:
                    print(f"{classPlayer.Player.name} is killer")
                elif classPlayer.Player.role != "Killer" and classPlayer.Player.alive:
                    print(f"{classPlayer.Player.name} is not a killer")
                else:
                    print("You are sooooo stupid that you chose a dead person")
        elif classPlayer.Player.role == "Seer" and classPlayer.Player.alive and classPlayer.Player.gossip > 0:
            vote_to_see = input(f"{classPlayer.Player.name} choose who to SEE: ")
            if any(classPlayer.Player.name == vote_to_see for classPlayer.Player in players):
                if classPlayer.Player.role == "Killer" and classPlayer.Player.alive:
                    print(f"{classPlayer.Player.name} is not a killer")
                elif classPlayer.Player.role != "Killer" and classPlayer.Player.alive:
                    print(f"{classPlayer.Player.name} is killer")
                else:
                    print("You are sooooo stupid that you chose a dead person")
def killers_move(players):
        if classPlayer.Player.role == "Killer" and classPlayer.Player.alive and classPlayer.Player.gossip == 0:
            vote_to_kill = input(f"{classPlayer.Player.name} choose who to KILL: ")
            if any(classPlayer.Player.name == vote_to_kill for classPlayer.Player in players):
                if  classPlayer.Player.role == "Killer" and classPlayer.Player.alive:
                    print("You cant kill yourself")
                elif classPlayer.Player.alive and classPlayer.Player.role != "Killer" and classPlayer.Player.gossip == 0:
                    classPlayer.Player.vote_k += 1
                    print(f"{classPlayer.Player.name} is dead")
                    print(f"{classPlayer.Player.name} vote to kill is  {classPlayer.Player.vote_k}")
                elif classPlayer.Player.alive and classPlayer.Player.role != "Killer" and classPlayer.Player.gossip > 0:
                    classPlayer.Player.vote_k += 1
                    print(f"{classPlayer.Player.name} is dead")
                    print(f"{classPlayer.Player.name} vote to kill is  {classPlayer.Player.vote_k}")
                    for classPlayer.Player in players:
                        if classPlayer.Player.role == "Gossip girl":
                            classPlayer.Player.vote_k += 1
                            print(f"{classPlayer.Player.name} is dead")
                            print(f"{classPlayer.Player.name} vote to kill is  {classPlayer.Player.vote_k}")
                else:
                    print("This person is already dead")
            else:
                print("This player is not in game ")
def doctor_move(players):
    for classPlayer.Player in players:
        if classPlayer.Player.role == "Doctor" and classPlayer.Player.alive and classPlayer.Player.gossip == 0:
            vote_to_save = input(f"{classPlayer.Player.name} choose who to SAVE: ")
            if any(classPlayer.Player.name == vote_to_save for classPlayer.Player in players):
                if classPlayer.Player.alive and classPlayer.Player.gossip == 0:
                    classPlayer.Player.vote_k -=1
                    print(f"{classPlayer.Player.name} is saved")
                    print(f"{classPlayer.Player.name} vote to kill is {classPlayer.Player.vote_k}")
                elif classPlayer.Player.alive and classPlayer.Player.gossip > 0:
                    classPlayer.Player.vote_k -=1
                    print(f"{classPlayer.Player.name} is saved")
                    print(f"{classPlayer.Player.name} vote to kill is {classPlayer.Player.vote_k}")
                    for classPlayer.Player in players:
                        if classPlayer.Player.role == "Gossip girl":
                            classPlayer.Player.vote_k -= 1
                            print(f"{classPlayer.Player.name} is saved")
                            print(f"{classPlayer.Player.name} vote to kill is {classPlayer.Player.vote_k}")
                else:
                    print("The person is already dead")

def gossipGirl_move(players):
    for classPlayer.Player in players:
        if classPlayer.Player.role == "Gossip girl" and classPlayer.Player.alive:
            vote_to_gossip = input(f"{classPlayer.Player.name} choose for who to Gossip: ")
            if any(classPlayer.Player.name == vote_to_gossip for classPlayer.Player in players):
                if  classPlayer.Player.role == "Gossip girl" and classPlayer.Player.alive:
                    print("You cant gossip for yourself")
                elif classPlayer.Player.alive and classPlayer.Player.role != "Gossip girl":
                    classPlayer.Player.gossip += 1
                    print(f"{classPlayer.Player.name} vote to gossip  {classPlayer.Player.gossip}")
                else:
                    print("This person is already dead")
            else:
                print("This player is not in game ")
def nothing(players):
    print(f"{classPlayer.Player.name}")
    input("Press Enter")
def night_time(players):
    for classPlayer.Player in players:
        if classPlayer.Player.role == "Killer":
            killers_move(players)
            time.sleep(3)
            for i in range(1, 11):
                print("")
        elif classPlayer.Player.role == "Doctor":
            doctor_move(players)
            for i in range(1, 11):
                print("")
        elif classPlayer.Player.role == "Gossip girl":
            gossipGirl_move(players)
            for i in range(1, 11):
                print("")
        elif classPlayer.Player.role == "Seer":
            seer_move(players)
            for i in range(1, 11):
                print("")
        else:
            nothing(players)
            for i in range(1, 11):
                print("")
def after_night_or_day(players):
    for classPlayer.Player in players:
        if classPlayer.Player.alive and classPlayer.Player.vote_k >= 1:
            classPlayer.Player.alive = False
            print(f"{classPlayer.Player.name} alive  {classPlayer.Player.alive}")
    alive_players = [classPlayer.Player.name for classPlayer.Player in players if classPlayer.Player.alive]
    if alive_players:
        print("Alive players are "+ " ".join(alive_players))
    else:
        print("No one is alive")
    for classPlayer.Player in players:
        if not classPlayer.Player.alive:
            print(f"{classPlayer.Player.name} is dead")

def day_time(players):
    for p in players:
        if p.alive:
            print(f"{p.name} is alive. They can vote.")
            while True:
                vote_for = input(f"{p.name}, please enter the name of the player you want to vote for: ")
                if vote_for == p.name:
                    print("You cannot vote for yourself.")
                else:
                    break
            for q in players:
                if q.name == vote_for:
                    q.vote += 1
                    print(f"{p.name} has voted for {q.name}. \n")
                    break
    max_vote = max(p.vote for p in players if p.alive)
    for p in players:
        if p.alive and p.vote == max_vote:
            if p.role == "Fool":
                print("Fool win the game")
                p.win += 1
            else:
                print(f"{p.name} has the most votes and will die!")
                p.alive = False
    for classPlayer.Player in players:
        classPlayer.Player.vote_k = 0
        classPlayer.Player.gossip = 0
        classPlayer.Player.vote = 0
        print(f"{classPlayer.Player.name} vote to kill is {classPlayer.Player.vote_k} gossips is {classPlayer.Player.gossip} votes of day {classPlayer.Player.vote}")

def gameplay():
    players = []
    num_players = int(input("Enter number of players(bigger than 7): "))
    if num_players > 7:
        for i in range(num_players):
            classPlayer.Player.name = input(f"Enter name of player {i + 1}: ")
            players.append(classVilager.Villager(classPlayer.Player.name))
    else:
        num_players = int(input("Enter number of players(bigger than 7): "))
    for k in range(2):
        killer = random.choice(players)
        while isinstance(killer, classKiller.Killer):
            killer = random.choice(players)
        players.remove(killer)
        killer.__class__ = classKiller.Killer
        killer.role = "Killer"
        players.append(killer)

    gossipGirl = random.choice([g for g in players if isinstance(g,classVilager.Villager)])
    players.remove(gossipGirl)
    gossipGirl.__class__ = classGossipGirl.gossipGirl
    gossipGirl.role = "Gossip girl"
    players.append(gossipGirl)

    doctor = random.choice([v for v in players if isinstance(v,classVilager.Villager)])
    players.remove(doctor)
    doctor.__class__ = classDoc.Doc
    doctor.role = "Doctor"
    players.append(doctor)

    seer = random.choice([s for s in players if isinstance(s,classVilager.Villager)])
    players.remove(seer)
    seer.__class__ = classSeer.Seer
    seer.role = "Seer"
    players.append(seer)

    fool = random.choice([f for f in players if isinstance(f, classVilager.Villager)])
    players.remove(fool)
    fool.__class__ = classFool.Fool
    fool.role = "Fool"
    players.append(fool)

    for classPlayer.Player in players:
        print(f"{classPlayer.Player.name}")
        input("Press Enter to see your role")
        print(f"{classPlayer.Player.role}")
        time.sleep(5)
        for i in range(1,11):
            print("")

    while True:
        after_night_or_day(players)
        night_time(players)
        print("")
        after_night_or_day(players)
        print("")
        voting=day_time(players)
        print("")
        killer_count = 0
        village_count = 0
        for classPlayer.Player in players:
            if classPlayer.Player.alive:
                if classPlayer.Player.role == "Killer":
                    killer_count += 1
                elif classPlayer.Player.role != "Fool":
                    village_count += 1
        if killer_count == 0:
            print("Villagers win")
            break

        elif killer_count == village_count:
            print("Killers win")
            break
        elif classPlayer.Player.win > 0:
            print("Fool win")
            break


gameplay()
#for classPlayer.Player in players:
#   print(f"Name {classPlayer.Player.name}, role {classPlayer.Player.role}, alive {classPlayer.Player.alive}")
