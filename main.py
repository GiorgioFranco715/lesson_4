if __name__ == "__main__":
    print('test')
    #names = "Юрій"
    #surname = "Юськів"
    #fathername = "Михайлович"
    #
    #
    #
    # print(f"{surname},{name[0].upper},{fathername[0].upper}")
    #set
    #arr_surnames = {"Doe","Lee","Chan"}
    #arr_surnames.add('test')
   # print(arr_surnames)
   # print(user_data['pib'])
    #user_data =
     #примітивні дані
    # a = 1
    # b = a
    # b += 1
    # print(a,b)
    #Складні дані
    # a = [1]
    # b = a
    # b += [1]
    # print(a,b)

    users = [
        {
            "name":"John",
            "age": 31
        },
        {
            "name": "Jane",
            "age": 27
        },{
            "name": "Jack",
            "age": 15
        },{
            "name": "Jeff",
            "age": 40
        }
    ]
    # del users[0]
    # del users[2]
    # del users[0]
    # del (users[0])

    #print(users[2]["name"],users[2]["age"])


    # одиницівиміру = input("Введіть одиницю виміру температури:")
    # users_data_цельсії = int(input("Введіть температуру на вулиці:"))
    # if одиницівиміру = ("Цельсії"):
    #     users_data_цельсії * 9/5 + 32=users_data_фаренгейти
    #
    # цельсії_в_фаренгейти = (0 °C × 9/5) + 32 = 32 °F
    #
    # if users_data > 0:
    #     print("Вдягнись легко")
    # elif users_data == 0:
    #     print("Вдягнись як хочеш")
    # else:
    #     print("Вдягнись тепло")

        print("___START PROGRAM___ \n\n")
        system_metrics = input(f"Please choise system metrics:\n"
                               f"c - Celsius\n"
                               f"f - Farengeit\n" 
                               f"k - Kalvin\n")
                               f"Please choise: ")
        temperature_value = int(input(f"Please input temperature value:  "))

        # conditional temp
        if system_metrics.lower() == "c":
            print


