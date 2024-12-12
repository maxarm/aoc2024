def read_file(day: int, filename: str) -> str:
    path = f"day{day}/{filename}"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def read_test_input(day: int) -> str:
    return read_file(day, "testin.txt")

def read_input(day: int) -> str:
    return read_file(day, "in.txt")

def read_lines(day: int, read_test_data: bool=False) -> str:
    return read_test_input(day) if read_test_data else read_input(day)

def read_lines_of_b(day: int, read_test_data: bool=False) -> str:
    return read_file(day, "testinb.txt") if read_test_data else read_file(day, "inb.txt")

def read_data(day: int, read_test_data: bool=False) -> str:
    return read_lines(day, read_test_data)[0]
