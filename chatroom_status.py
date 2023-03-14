def chatroom_status(users_list):
    n = len(users_list)
    if n == 0:
        return "no one online"
    elif n == 1:
        return f"{users_list[0]} online"
    elif n == 2:
        return f"{users_list[0]} and {users_list[1]} online"
    else:
        return f"{users_list[0]}, {users_list[1]} an {n-2} more online"

print (chatroom_status([]))
print(chatroom_status({"Karyna"}))
print(chatroom_status({"Karyna", "Emma"}))
print(chatroom_status({"Karyna", "Emma", "Tanya"}))
