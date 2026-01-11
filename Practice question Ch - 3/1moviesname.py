movies = []
#1st way
movie1 = input("Name of first movie :")
movie2 = input("Name of second movie :")
movie3 = input("Name of third movie :")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

#2nd way
movies.append(input("1st movie:"))
movies.append(input("2st movie:"))
movies.append(input("3st movie:"))

print(movies)

#3rd way

mov = input("Name of first movie :")
movies.append(mov)
mov = input("Name of second movie :")
movies.append(mov)
mov = input("Name of third movie :")
movies.append(mov)

print(movies)