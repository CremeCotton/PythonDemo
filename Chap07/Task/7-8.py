wait_food = ['pizza','humburger','ice cream']
finished_food = []
while wait_food:
    current_food = wait_food.pop()
    print(f'正在制作{current_food}')
    finished_food.append(current_food)
for food in finished_food:
    print(f'制作完成的食物:{food}')