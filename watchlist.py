movies = {}

while True:
    print("1. Add movie")
    print("2. Mark as watched")
    print("3. View unwatched")
    print("4. View all")
    print("5. Quit")

    choice = input("Pick an option: ")

    if choice == "1":
        movie_name = input("Enter movie name: ")
        movies[movie_name] = False
        print(movie_name)
    elif choice == "2":
        watched_movie = input("What move did you watch: ")
        if watched_movie in movies:
            movies[watched_movie] = True
            print(f"{watched_movie} marked as watched")
    elif choice == "3":
        for x, y in movies.items():
            if y == False:
                print(f"Unwatched movies: {x}")
    elif choice == "4":
        for x, y in movies.items():
            status = "✓" if y else "✗"
            print(f"{x}: {status}")
    elif choice == "5":
        break