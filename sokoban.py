def main():
    history = []

    while True:
        action = input("Action: ").strip().capitalize().replace(" ", "")
        try:
            int(action)
            print("Wrong input!!")

        except:
            if action == "Undo":

                if history:
                    print(f"Undo: {history.pop()}")
                    
                else:

                    print("The history is empty!")
                    break


            elif action == "Restart":
                history.clear()

            else:
                history.append(action)

        print(history)




main()
