movie = input()


type_of_ticket = ""
total_student = 0
total_standard = 0
total_kids = 0
total_tickets = 0


while movie != "Finish":
    free_spots = int(input())
    current_spots = free_spots
    while current_spots > 0:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break

        if type_of_ticket == "student":
            total_student += 1
        elif type_of_ticket == "kid":
            total_kids += 1
        else:
            total_standard += 1

        current_spots -= 1

    if current_spots > 0:
        print(f"{movie} - {(free_spots-current_spots)/free_spots*100:.2f}% full.")
    else:
        print(f"{movie} - 100.00% full.")
    movie = input()

total_tickets = total_standard + total_student + total_kids
print(f"Total tickets: {total_tickets}")
print(f"{total_student/total_tickets*100:.2f}% student tickets.")
print(f"{total_standard/total_tickets*100:.2f}% standard tickets.")
print(f"{total_kids/total_tickets*100:.2f}% kids tickets.")
