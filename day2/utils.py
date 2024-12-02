def read_file(day: int, filename: str) -> str:
    path = f"day{day}/{filename}"
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

def read_test_input(day: int) -> str:
    return read_file(day, "testin.txt")

def read_input(day: int) -> str:
    return read_file(day, "in.txt")

def read_data(day: int, read_test_data: bool=False) -> str:
    return read_test_input(day) if read_test_data else read_input(day)