name = input("Enter your name : ")
surname = input("Enter your surname : ")
print("What is your favorite ?")
print("1 - One Piece")
print("2 - Naruto Shippuden")
print("3 - My Hero Academia")
anime = input("Your choice : ")
while True:
    if anime in ["1", "2", "3"]:
        break
    else:
        anime = input("Enter a good choice : ")
if anime == "1":
    anime = "One Piece"
elif anime == "2":
    anime = "Naruto Shippuden"
else:
    anime = "My Hero Academia"

print(f"Hello {surname} {name}, your favorite anime is {anime}")
