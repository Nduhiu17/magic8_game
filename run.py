from main import Magic

print('Hello User, I am the Magic 8 Ball, What is your name?')

name = input()

print('hello ' + name)

new_magic = Magic(username=name)

print("ask me a question")

name = input()

new_magic.show_progress()

print(new_magic.generate_random_answer())

new_magic.Replay()
