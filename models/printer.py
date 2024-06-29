

class Printer:
    def __init__(self):
        pass
    
    def print_ranking(self, data):
        length_max = 12
        print("| Player      | Points      |")
        print("| ----------- | ----------- |")
        for player in data:
            self.print_row_of_info([player.player.name, str(player.points)], length_max)

    def print_row_of_info(self, data, length_max):
        pad_char = ' '
        for item in data:
            item = str(item)
            print('| ', end='')
            if len(item) > length_max:
                print(item[:length_max], end="")
            elif len(item) < length_max:
                print(item.ljust(length_max, pad_char), end="")
            else:
                print(item, end="")
        print('|')

    def print_rows_of_info(self, data, length_max):
        """Give the printer a title and data. The printer will print a nice table in the consol."""
        number = length_max - 2
        dotted_line = '-' * number
        new_list = [dotted_line] * len(data[0])
        data.insert(1, new_list)
        for items in data:
            self.print_row_of_info(items, length_max)