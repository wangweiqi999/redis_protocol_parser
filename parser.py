class ProtocolList:
    def __init__(self, input_string):
        self.list = input_string.split('\r\n')
        self.index = 0
        self.length = len(self.list)

    def read_line(self):
        self.index += 1
        return self.list[self.index-1]

    def read_line_previous(self):
        return self.list[self.index-1]

    def __repr__(self):
        return self.list[self.index]


def parsed(input_string):
    protocol_list = ProtocolList(input_string)
    output = parse(protocol_list)
    return output


def parse(protocol_list):
    """
    Input example:
    *2\r\n
    $3\r\n
    GET\r\n
    $3\r\n
    foo\r\n
    :return:
    """
    pl = protocol_list
    output = None
    while pl.index < pl.length:
        line = pl.read_line()
        if line.startswith('+'):
            output = parse_string_simple(line)
        elif line.startswith('-'):
            output = parse_error(line)
        elif line.startswith(':'):
            output = parse_integer(line)
        elif line.startswith('$'):
            output = parse_string_bulk(pl)
        elif line.startswith('*'):
            number_of_elements = int(line[1:])
            output = parse_array(pl, number_of_elements)
        else:
            pass
    return output


def parse_integer(line):
    return int(line[1:])


def parse_string_simple(line):
    return line[1:]


def parse_string_bulk(protocol_list):
    pl = protocol_list
    line = pl.read_line_previous()
    length = int(line[1:])
    if length == 0:
        string = ''
    elif length == -1:
        string = None
    else:
        string = pl.read_line()
    return string


def parse_error(line):
    return line[1:]


def parse_array(protocol_list, number_of_elements):
    if number_of_elements == -1:
        return None
    pl = protocol_list
    output = []
    count = 0
    while count < number_of_elements:
        line = pl.read_line()
        if line.startswith('+'):
            output.append(parse_string_simple(line))
        elif line.startswith('-'):
            output.append(parse_error(line))
        elif line.startswith(':'):
            output.append(parse_integer(line))
        elif line.startswith('$'):
            output.append(parse_string_bulk(pl))
        elif line.startswith('*'):
            n = int(line[1:])
            output.append(parse_array(pl, n))
        else:
            count -= 1
        count += 1
    return output


if __name__ == '__main__':
    input_str = '*3\r\n:1\r\n:2\r\n:3\r\n'
    print(parsed(input_str))
