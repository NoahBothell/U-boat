from tkinter import *
from PIL import ImageTk, Image
import sys

#screenvalue
main = Tk()

#pictures
HomeScreen = ImageTk.PhotoImage(Image.open("HomeScreen.png"))
TourPicture = ImageTk.PhotoImage(Image.open("./TourPicture.png"))
EngineRoomP = ImageTk.PhotoImage(Image.open("./EngineRoom.png"))
CommanderCabinP = ImageTk.PhotoImage(Image.open("./CommanderCabin.png"))
ControlRoomP = ImageTk.PhotoImage(Image.open("./ControlRoom.png"))
CrewQuartersP = ImageTk.PhotoImage(Image.open("./CrewQuarters.png"))
OfficerQuartersP = ImageTk.PhotoImage(Image.open("./OfficerQuarters.png"))
TorpedoRoomP = ImageTk.PhotoImage(Image.open("./TorpedoRoom.png"))
LetterToHomeP = ImageTk.PhotoImage(Image.open("./LetterToHome.png"))
NewP = ImageTk.PhotoImage(Image.open("./New.png"))
UsesP = ImageTk.PhotoImage(Image.open("./Uses.png"))
DifferentTypesP = ImageTk.PhotoImage(Image.open("./DifferentTypes.png"))
WarEffectP = ImageTk.PhotoImage(Image.open("./WarEffect.png"))

#definitions
def Tour():
    #pictures
    global HomeScreen
    global TourPicture
    global EngineRoomP
    global CommanderCabinP
    global ControlRoomP 
    global CrewQuartersP 
    global OfficerQuartersP 
    global TorpedoRoomP
    global NewP
    global UsesP
    global DifferentTypesP
    global WarEffectP

    #U-boat Tour
    #legend: P=picture, F=function, W=window

    #Base Variables
    main.withdraw()
    W = Toplevel()
    W.title("U-1 tour")

    #definitions
    def HomeScreenF():
        main.deiconify()
        W.withdraw()
        

    def EngineRoom():
        W.withdraw()
        #Base Variables
        We = Toplevel()
        We.title("Engine Room")
        global EngineRoomP

        #definitions
        def AbEngine():
            InfoLabel.config(text = "The diesel engines of the time were not compact enough to be practical so this engine instead runs on kerosene,\n which is a much weaker alternative and forces them to carry more fuel to compensate.\n This requirement of more fuel for the U-1 forced it to only be permitted to be operable near coasts.\n This engine had two functions, powering the propellers, and turning the electric engine.")
            

        def AbElectricEngine():
            InfoLabel.config(text = "This engine has an output of 200 horsepower which is used to power all functions of the submarine that the kerosene engine does not power.\n Meaning that anything other than running the propellers it is in charge of.")

        def AbSwitchboard():
            InfoLabel.config(text = "The switchboard allowed the crew to prioritize different functions of the ship that were powered by the electric engine.\n This was so they could more accurately disperse their power,\n which saved power consumption on currently unavailable functions.")

        def TourScreen():
            We.destroy()
            W.deiconify()
            
            



        #screenProcess
        PictureLabel = Label(We, image = EngineRoomP)
        B1 = Button(We, text = "Engine", command = AbEngine)
        B2 = Button(We, text = "Electric engine", command = AbElectricEngine)
        B3 = Button(We, text = "Switchboard", command = AbSwitchboard)
        B4 = Button(We, text = "Go back", command = TourScreen)
        PictureLabel.grid(row = 0, column = 0, columnspan = 3)
        B1.grid(row = 1, column = 0)
        B2.grid(row = 1, column = 1)
        B3.grid(row = 1, column = 2)
        B4.grid(row = 1, column = 3)
        InfoLabel = Label(We)
        InfoLabel.grid(column = 4, row = 0)

    def CrewCabin():
        W.withdraw()

        #base variables
        Wcc = Toplevel()
        Wcc.title("Crew's Cabin")
        global CrewQuartersP
        def TourScreen():
            Wcc.destroy()
            W.deiconify()
        ImageLabel = Label(Wcc, image = CrewQuartersP)
        InfoLabel = Label(Wcc, text = "The crew’s quarters are incredibly cramped,\n especially considering that a U-1 was made to have a crew of twelve at all times.")
        ImageLabel.grid(row = 0, column = 0)
        InfoLabel.grid(row = 0, column = 1)
        B1 = Button(Wcc, text = "Go back", command = TourScreen)
        B1.grid(row = 1, column = 1)

    def OfficerQuarters():
        W.withdraw()

        #base variables
        Wcc = Toplevel()
        Wcc.title("Officer's Cabin")
        global OfficerQuartersP
        def TourScreen():
            Wcc.destroy()
            W.deiconify()
        ImageLabel = Label(Wcc, image = OfficerQuartersP)
        InfoLabel = Label(Wcc, text = "Though not as lavish as the Commander’s,\n officer’s quarters are still relatively lavish compared to the crew’s accommodation.")
        ImageLabel.grid(row = 0, column = 0)
        InfoLabel.grid(row = 0, column = 1)
        B1 = Button(Wcc, text = "Go back", command = TourScreen)
        B1.grid(row = 1, column = 1)

    def ControlRoom():
        W.withdraw()
        #Base Variables
        global ControlRoomP
        Wt = Toplevel()
        Wt.title("ControlRoom")

        #definitions
        def Wheels():
            InfoLabel.config(text = "These wheels are directly linked to the movement of the\n fins in order to steer the U-Boat")
            

        def DepthGauge():
            InfoLabel.config(text = "This depth gauge only goes to 25 meters since this prototype was\n only meant to be able to go depths of thirty meters.")

        def TourScreen():
            Wt.destroy()
            W.deiconify()



        #screenProcess
        PictureLabel = Label(Wt, image = ControlRoomP)
        B1 = Button(Wt, text = "Wheels", command = Wheels)
        B2 = Button(Wt, text = "DepthGauge", command = DepthGauge)
        B3 = Button(Wt, text = "Go back", command = TourScreen)
        PictureLabel.grid(row = 0, column = 0, columnspan = 3)
        B1.grid(row = 1, column = 0)
        B2.grid(row = 1, column = 1)
        B3.grid(row = 1, column = 2)
        InfoLabel = Label(Wt)
        InfoLabel.grid(column = 4, row = 0)

    def CommanderCabin():
        W.withdraw()

        #base variables
        Wcc = Toplevel()
        Wcc.title("Comander's cabin")
        global CommanderCabinP
        def TourScreen():
            Wcc.destroy()
            W.deiconify()
        ImageLabel = Label(Wcc, image = CommanderCabinP)
        InfoLabel = Label(Wcc, text = "Despite its looks, the commander’s cabin is the most luxurious housing accommodation found on the U-1,\n providing as much comfort as possible in the small space. The commander's cabin was placed directly behind the torpedo room to prevent any torpedoes\n from being launched without his permission and the commander had direct access to the torpedoes since it was usually the commander who launched them.")
        ImageLabel.grid(row = 0, column = 0)
        InfoLabel.grid(row = 0, column = 1)
        B1 = Button(Wcc, text = "Go back", command = TourScreen)
        B1.grid(row = 1, column = 1)

    def TorpedoRoom():
        W.withdraw()
        #Base Variables
        global TorpedoRoomP
        Wt = Toplevel()
        Wt.title("Torpedo Room")

        #definitions
        def ThreeTubes():
            InfoLabel.config(text = "Despite appearing to have three 45 mm torpedo tubes, the U-1 only has one actual launching tube.\n The other two tubes were used for watertight storage of the torpedoes.")
            

        def Torpedoes():
            InfoLabel.config(text = "The type of torpedoes that were tested in the U-1 were the C03 torpedoes.\n Originally meant only to be launched by surface ships.\n These torpedoes had a range of 1.5 to 3 Kilometers (or about 1.86 miles for us Americans).")

        def TourScreen():
            Wt.destroy()
            W.deiconify()



        #screenProcess
        PictureLabel = Label(Wt, image = TorpedoRoomP)
        B1 = Button(Wt, text = "Three tubes at the front?", command = ThreeTubes)
        B2 = Button(Wt, text = "Torpedoes", command = Torpedoes)
        B3 = Button(Wt, text = "Go back", command = TourScreen)
        PictureLabel.grid(row = 0, column = 0, columnspan = 3)
        B1.grid(row = 1, column = 0)
        B2.grid(row = 1, column = 1)
        B3.grid(row = 1, column = 2)
        InfoLabel = Label(Wt)
        InfoLabel.grid(column = 4, row = 0)

    #Screen Process
    PictureLabel = Label(W, image = TourPicture)
    B1 = Button(W, text = "Engine room", command = EngineRoom)
    B2 = Button(W, text = "Crew cabin", command = CrewCabin)
    B3 = Button(W, text = "Officer's quarters", command = OfficerQuarters)
    B4 = Button(W, text = "Control room", command = ControlRoom)
    B5 = Button(W, text = "Commander's cabin", command = CommanderCabin)
    B6 = Button(W, text = "Torpedo room", command = TorpedoRoom)
    B7 = Button(W, text = "Go back", command = HomeScreenF)
    B1.grid(row = 1, column = 0)
    B2.grid(row = 1, column = 1)
    B3.grid(row = 1, column = 2)
    B4.grid(row = 1, column = 3)
    B5.grid(row = 1, column = 4)
    B6.grid(row = 1, column = 5)
    B7.grid(row = 2, column = 6)

    PictureLabel.grid(row = 0, column = 0, columnspan = 6)

def LetterToHome():
    global LetterToHomeP
    main.withdraw()
    W = Toplevel()
    def Exit():
        W.destroy()
        main.deiconify()
    PictureLabel = Label(W, image = LetterToHomeP)
    B1 = Button(W, text = "Exit", command = Exit)
    PictureLabel.pack()
    B1.pack()

def AboutTheUBoat():
    main.withdraw()
    W = Toplevel()
    
    def DifferentTypes():
        W.withdraw()
        W1 = Toplevel()

        def Exit():
            W1.destroy()
            W.deiconify()

        B1 = Button(W1, text = "Exit", command = Exit)
        ImageLabel = Label(W1, image = DifferentTypesP)
        ImageLabel.pack()
        B1.pack()

    def WhoAndHow():
        W.withdraw()
        W1 = Toplevel()

        def Exit():
            W1.destroy()
            W.deiconify()

        B1 = Button(W1, text = "Exit", command = Exit)
        ImageLabel = Label(W1, image = UsesP)
        ImageLabel.pack()
        B1.pack() 

    def HistoryNew():
        W.withdraw()
        W1 = Toplevel()

        def Exit():
            W1.destroy()
            W.deiconify()

        B1 = Button(W1, text = "Exit", command = Exit)
        ImageLabel = Label(W1, image = NewP)
        ImageLabel.pack()
        B1.pack()

    def Effect():
        W.withdraw()
        W1 = Toplevel()

        def Exit():
            W1.destroy()
            W.deiconify()

        B1 = Button(W1, text = "Exit", command = Exit)
        ImageLabel = Label(W1, image = WarEffectP)
        ImageLabel.pack()
        B1.pack()

    def MainMenu():
        W.destroy()
        main.deiconify()

    B1 = Button(W, text = "Different types", command = DifferentTypes)
    B2 = Button(W, text = "Who used it and how?", command = WhoAndHow)
    B3 = Button(W, text = "History and what made it new", command = HistoryNew)
    B5 = Button(W, text = "How did it effect WW1?", command = Effect)
    B6 = Button(W, text = "Main menu", command = MainMenu)
    B1.grid(column = 0, row = 0)
    B2.grid(column = 0, row = 1)
    B3.grid(column = 0, row = 2)
    B4.grid(column = 0, row = 3)
    B5.grid(column = 0, row = 4)
    B6.grid(column = 0, row = 5)

def Credits():
    main.withdraw()
    W = Toplevel(background = "black")
    Credit = "Credits\n\nHead of research -- Caiden Unruh\n\nLead creative/software developer -- Noah Bothell\n\nProperty of MonKKeys incorporated"

    def MainMenu():
        main.deiconify()
        W.destroy()

    CreditLabel = Label(W, text = Credit, foreground = "white", background="black")
    B1 = Button(W, text = "Main menu", command = MainMenu, background="White")
    CreditLabel.pack()
    B1.pack()

#Screen functions

PictureLabel = Label(main, image = HomeScreen)
B1 = Button(main,  text = "Tour", command = Tour)
B2 = Button(main, text = "Letter to home", command = LetterToHome)
B3 = Button(main, text = "About the U-boat", command = AboutTheUBoat)
B4 = Button(main, text = "Credits", command = Credits)
B1.grid(row = 1, column = 0)
B2.grid(row = 1, column = 2)
B3.grid(row = 1, column = 1)
B4.grid(row = 1, column = 3)
PictureLabel.grid(row = 0, columnspan = 4)

#mainloop
main.mainloop()