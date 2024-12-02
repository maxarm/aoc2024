def read_demo_input(day: int) -> str:
    path = f"data/demo_data{day:02}.txt"
    with open(path, "r") as f:
        lines = f.readlines()
    return lines
