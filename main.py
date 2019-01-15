import random


class Magic:

    def __init__(self, username):
        self.username = username

    def generate_random_answer(self):
        """method that generates a randomn number"""
        answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
                   'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy',
                   'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                   'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
                   'Outlook not so good', 'Very doubtful']
        answer = (answers[random.randint(0, len(answers) - 1)])
        return answer

    def show_progress(self):
        """method to show progress"""
        print("In progress,kindly wait.....")
        return ("In progress,kindly wait.....")

    @classmethod
    def Replay(self):
        """method to replay the game"""
        print('Do you have another question? [Y/N] ')
        reply = input()
        # check whether user needs replay
        if reply == 'Y':
            print("ask me a question")
            input()
            Magic.show_progress(self)
            print(Magic.generate_random_answer(self))
            Magic.Replay()
        # check whether user dont need replay
        elif reply == 'N':
            exit()
        else:
            print('I apologies, I did not catch that. Please repeat.')
            Magic.Replay()
