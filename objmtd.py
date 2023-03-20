class leader:
    def __init__ (head, name, age):
        head.name = name
        head.age = age
 
    def noon(head):
        
        print("Welcome " + head.name + ". " + "your age" + str(head.age))

TV = leader("Vimal", 20)
TV.noon()    