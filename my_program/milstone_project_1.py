MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see a movie, 'f' to find a movie title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter your movie title: " )
    director = input("Enter your movie director: " )
    year = input("Enter your movie year: " )

    movies.append({
    'title': title,
    'director': director,
    'year': year
})

def show_movies():
    for movie in movies:
        print_movie(movie)
        
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


def find_movies():
    search_title = input("Enter your movie title you're looking for: ")
    
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)
        

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
          add_movie()
        elif selection == "l":
          show_movies()
        elif selection == "f":
          find_movies()
    else:
        print("Unknown command. plaese try again.   ")
        
selection = input(MENU_PROMPT)

menu()