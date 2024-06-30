

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
            if len(item) < length_max:
                print(item.ljust(length_max, pad_char), end="")
            else:
                print(item, end="")
        print('|')

    def print_rows_of_info(self, data):
        """Give the printer a title and data. 
        The printer will print a nice table in the consol.
        The table will be automatically sized to avoid splitting of strings."""
        length_max = get_longest_string_length(data) + 1
        number = length_max - 1
        dotted_line = '-' * number
        new_list = [dotted_line] * len(data[0])
        data.insert(1, new_list)
        for items in data:
            self.print_row_of_info(items, length_max)

def get_longest_string_length(nested_list):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield str(item)  # Convert non-string items to strings

    # Convert all items to strings and then find the longest one
    flat_list = list(flatten(nested_list))
    longest_string = max(flat_list, key=len, default="")
    return len(longest_string)