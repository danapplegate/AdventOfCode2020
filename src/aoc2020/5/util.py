def calculate_seat_id(boarding_pass):
    raw_row = boarding_pass[0:7]
    raw_col = boarding_pass[7:]
    row = int(raw_row.replace("F", "0").replace("B", "1"), 2)
    col = int(raw_col.replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col
