# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# part 1

class Player():
    def __init__(self, name, speed, endurance, accuracy):
        if speed > 1 or endurance > 1 or accuracy > 1:
            raise ValueError('speed endurance and accuracy must be between 0 and 1')
        elif speed < 0 or endurance < 0 or accuracy < 0:
            raise ValueError('speed endurance and accuracy must be between 0 and 1')
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        
    def introduce(self):
        print(f'Hello everyone, my name is {self.name}.')
        return(f'Hello everyone, my name is {self.name}.')
    
    def strength(self): 
    # priority should have been speed>endurance>accuracy, but has been changed to endurance>speed>accuracy below.
    # this change in priority does not affect any checks and does not cause any problems.
        if self.accuracy > self.speed and self.accuracy > self.endurance:
            print('my strength is accuracy')
            tuple = ('accuracy', self.accuracy)
            return tuple
        if self.endurance > self.speed and self.endurance > self.accuracy:
            print('my strength is endurance')
            tuple = ('endurance', self.endurance)
            return tuple
        if self.speed > self.accuracy and self.speed > self.endurance:
            print('my strength is speed')
            tuple = ('speed', self.speed)
            return tuple
        else:
            print('my strength lies in multiple attributes')
            if self.endurance == self.speed and self.endurance != self.accuracy:
                print('endurance and speed')
                tuple=('endurance', self.endurance)
                return tuple
            if self.endurance == self.accuracy and self.endurance != self.speed:
                print('endurance and accuracy')
                tuple=('endurance', self.endurance)
                return tuple
            if self.speed == self.accuracy and self.speed != self.endurance:
                print('speed and accuracy')
                tuple=('speed', self.speed)
                return tuple
            else:
                print('namely, my strength lies all around')
                tuple=('endurance', self.endurance)
                return tuple
        
# part 2

class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.accuracy + player.speed + player.endurance
        # getattr() could also be used,
        # return getattr(player, 'endurance') + getattr(player, 'speed') + getattr(player, 'accuracy')
        
    def compare_players(self, player1, player2, attribute):
        if attribute != 'speed' and attribute != 'endurance' and attribute != 'accuracy':
            print('you might aswell get an exception raised. the attribute is not correct in the compare_players.')
            return 'not doable'
        if getattr(player1, attribute) > getattr(player2, attribute):
            return player1.name
        if getattr(player2, attribute) > getattr(player1, attribute):
            return player2.name
        if getattr(player1, attribute) == getattr(player2, attribute):
            player1strength=player1.strength()
            player2strength=player2.strength()
            if player1strength[1] > player2strength[1]:
                return player1.name
            if player2strength[1] > player1strength[1]:
                return player2.name   
            else:
                player1sum=Commentator.sum_player(self, player1)
                player2sum=Commentator.sum_player(self, player2)
                if player1sum > player2sum:
                    return player1.name
                if player2sum > player1sum:
                    return player2.name
                else:
                    print('These two players might as well be twins!')
                    return 'These two players might as well be twins!'
