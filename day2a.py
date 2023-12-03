def calculate_max_blocks(configuration, red, green, blue):
    max_red = max_green = max_blue = 0

    for group in configuration:
        for cube in group:
            count, color = cube.split()
            count = int(count)
            if color == 'red':
                max_red = max(max_red, count)
            elif color == 'green':
                max_green = max(max_green, count)
            elif color == 'blue':
                max_blue = max(max_blue, count)

    return max_red, max_green, max_blue

total = 0

with open('advent2.txt', 'r') as file:
    for line in file:
        game_id, config_str = line.strip().split(':')
        configuration = [group.strip().split(', ') for group in config_str.split(';')]
        max_red, max_green, max_blue = calculate_max_blocks(configuration, 12, 13, 14)
        game_score = max_red * max_green * max_blue
        total += game_score

print(total)
