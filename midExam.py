class Star_Cinema:
    __hall_list = []
    __show_list = []
    __seats = {}

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [[0, 0, 0, 0], [0, 0, 0, 0], 
                            [0, 0, 0, 0],[0, 0, 0, 0],
                            [0, 0, 0, 0],[0, 0, 0, 0]]

    def book_seats(self, id, seats_to_book):
     for seat in seats_to_book:
        row, col = seat
        if self.__seats[id][row][col] == 1:
            print("Seat at Row:", row, "Column:", col, "is already booked.")
        else:
            self.__seats[id][row][col] = 1
            print("Seat at Row:", row, "Column:", col, "successfully booked.")

    def view_show_list(self):
     if self.__show_list:
        print("Available Shows:")
        for show in self.__show_list:
            print(f"(movie_Id: '{show[0]}', movie_Name: '{show[1]}', movie_Time: '{show[2]}')")
     else:
        print("No shows available.")



    def view_available_seats(self, id):
        print("Available seats for show with ID:", id)
        for row in range(len(self.__seats[id])):
            for col in range(len(self.__seats[id][row])):
                if self.__seats[id][row][col] == 0:
                    print("Row:", row, "Col:", col, "- Available")
                else:
                    print("Row:", row, "Col:", col, "- Booked")

class Hall(Star_Cinema):
    def __init__(self):
        super().__init__()
        self.entry_hall(self)

hall1 = Hall()


while True:
    print("\nOptions:")
    print("1: View all shows")
    print("2: View available seats")
    print("3: Book tickets")
    print("4: Add a new show")
    print("5: Exit")
    
    option = input("Enter Option: ")
    
    if option == '1':
        hall1.view_show_list()
       
    elif option == '2':
        show_id_to_view = input("Enter show ID to view available seats: ")
        if show_id_to_book not in hall1._Star_Cinema__seats:
            print("Input ID not found.")
        else:
            hall1.view_available_seats(show_id_to_view)

    elif option == '3':
        show_id_to_book = input("Enter show ID to book seats: ")
        if show_id_to_book not in hall1._Star_Cinema__seats:
            print("Input ID not found.")
            continue
        num_seats = int(input("Enter number of seats to book: "))
        seats_to_book = []
        for _ in range(num_seats):
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            seats_to_book.append((row, col))
        hall1.book_seats(show_id_to_book, seats_to_book)

    elif option == '4':
            show_id = input("Please Enter any Movie ID: ")
            movie_name = input("Enter movie name: ")
            show_time = input("Which Time show start : ")
            hall1.entry_show(show_id, movie_name, show_time)
      

    elif option == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid option!")



