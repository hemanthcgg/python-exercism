"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    seat = "ABCD"
    for i in range(number):
        yield seat[i%4]


def generate_seats(number):
    row = 1
    seat_index = 0
    seats_generated = 0
    seat_letters = "ABCD"
    seats_per_row = len(seat_letters)

    # while seats_generated < number:
    #     if row == 13:
    #         row += 1
    #         continue
    #     letter = seat_letters[seat_index]
    #     yield f"{row}{letter}"
    #     seats_generated += 1
    #     seat_index += 1
    #     if seat_index >= seats_per_row:
    #         seat_index = 0
    #         row += 1

    letters = generate_seat_letters(number)
    while seats_generated < number:
        if(row == 13):
            row+=1
            continue
        letter = next(letters)
        yield f"{row}{letter}"
        if letter == 'D':
            row += 1
        seats_generated += 1

    
def assign_seats(passengers):
    l = len(passengers)
    seats = generate_seats(l+1)
    return dict([(i, next(seats)) for i in passengers])

def generate_codes(seat_numbers, flight_id):
    for i in seat_numbers:
        base = f"{i}{flight_id}"
        base_l = 12 - len(base)
        yield f"{base}{'0'*base_l}"
