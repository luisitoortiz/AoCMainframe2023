def is_configuration_possible(configuration, red, green, blue):
    for group in configuration:
        for cube in group:
            count, color = cube.split()
            print(color, count)
            count = int(count)
            if color == 'red' and count > red:
                return False
            elif color == 'green' and count > green:
                return False
            elif color == 'blue' and count > blue:
                return False
    return True


target_red = 12
target_green = 13
target_blue = 14
possible_games = []

with open('advent2.txt', 'r') as file:
    for line in file:
        game_id, config_str = line.strip().split(':')
        configuration = [group.strip().split(', ') for group in config_str.split(';')]
        print(configuration)    
        if is_configuration_possible(configuration, target_red, target_green, target_blue):
            possible_games.append(int(game_id.split()[1]))

print("Possible games:", possible_games)
print("Sum of IDs:", sum(possible_games))
