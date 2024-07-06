

class Printer:
    def __init__(self):
        pass

    def print_row_of_info(self, data, column_widths):
        pad_char = ' '
        for item, width in zip(data, column_widths):
            item = str(item)
            print('| ', end='')
            if len(item) < width:
                print(item.ljust(width, pad_char), end='')
            else:
                # Truncate the item if it's too long
                print(item[:width], end='')
        print('|')

    def get_longest_string_length_per_column(self, data):
        # Initialize a list with zeros,
        # having length equal to the number of columns
        max_lengths = [0] * len(data[0])

        # Iterate over each row and
        # each column to find the max length of each column
        for row in data:
            for i, item in enumerate(row):
                max_lengths[i] = max(max_lengths[i], len(str(item)))
        return max_lengths

    def print_rows_of_info(self, data):
        """Give the printer a title and data.
        The printer will print a nice table in the console.
        The table will be automatically sized to avoid splitting of strings."""
        column_widths = self.get_longest_string_length_per_column(data)
        column_widths = [width + 1 for width in column_widths]  # Add padding

        # Create a dotted line row
        new_list = ['-' * width for width in column_widths]
        data.insert(1, new_list)

        for items in data:
            self.print_row_of_info(items, column_widths)


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
