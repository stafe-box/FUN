import random

a = [', а там армяне в нарды играют', ', ну и оттрарабанили его в сраку', ', а она ему как раз', ', ну и оттрарабанили её в сраку', ', а он ему как раз', ', а там насрано']
x = len(a)

text = input('СРАТЬ ЗДЕСЬ\n')
num = random.randrange(0, x)
print(text, a[num])

