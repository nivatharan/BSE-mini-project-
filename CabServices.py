TravellingVehicles = {
    'car':
    {
        'Max_passengers': 4,
        'condition': ["AC", "Non AC"],

    },

    'van':
    {
        'Max_passengers': 8,
        'condition': ["AC", "Non AC"]
    },

    'threewheeler':
    {
        'Max_passengers': 3,
        'condition': ["Non AC"]
    },
}

RoadGoodVehicles = {
    'truck':
        {
            'size': ['7ft', '12ft']
        },

    'lorry':
        {
            'Max_Load': "3500kg"
        },
}


def Dashboard():

    print("""
    +-------------------------------------------------+
    | Press no [1] to (show) TRAVELLING VEHICLES List |
    | Press no [2] to (show) ROAD GOOD VEHICLES List  |
    | Press no [3] to (add) new TRAVELLING VEHICLES   |
    | Press no [4] to (add) new ROAD GOOD VEHICLES    |
    | Press no [5] to (Search) vehicles               |
    | Press no [6] to (Heire) Vehicle                 |
    | Press no [0] to (Exit) the program              |
    +-------------------------------------------------+
    """)


def show_TV_List():
    i = 1
    for vehicle, faclity in TravellingVehicles.items():
        print("\t", i, " Vehicle: ", vehicle)
        i += 1
        for key in faclity:
            print("\t", key + ':', faclity[key])
        print("\n")


def show_RGV_List():
    i = 1
    for vehicle, faclity in RoadGoodVehicles.items():
        print("\t", i, "Vehicle: ", vehicle)
        i += 1
        for key in faclity:
            print("\t", key + ':', faclity[key])
        print("\n")


while True:
    Dashboard()

# Print Vehicle list
    try:
        userInput = int(input("Enter your choice: "))
    except ValueError:
        print("!!! Give a valid input !!! ")
    else:

        if userInput != 0:

            if userInput == 1:
                show_TV_List()

            elif userInput == 2:
                show_RGV_List()

        # ADD Vehicle

            elif userInput == 3:
                vehicleName = input("Enter Vehicle name: ")
                TravellingVehicles[vehicleName] = {}

                Max_passengers = input("Maximum pessengers: ")
                TravellingVehicles[vehicleName]["Max_passengers"] = Max_passengers

                condition = input("condition [AC / Non AC]: ")
                TravellingVehicles[vehicleName]["condition"] = condition

            elif userInput == 4:
                RoadGoodVehicles = input("Enter Vehicle name: ")
                TravellingVehicles[RoadGoodVehicles] = {}

                size = input("size of the vehicel: ")
                TravellingVehicles[RoadGoodVehicles]["size"] = size

                Max_Load = input("Maximum Load of the vehicle: ")
                TravellingVehicles[RoadGoodVehicles]["Max_Load"] = Max_Load

                print(RoadGoodVehicles)

        # Search Vehicles

            elif userInput == 5:
                Vname = input("Which Vehicle do you want? ")
                SVname = Vname.lower()
                if SVname in TravellingVehicles.keys():
                    print(Vname, TravellingVehicles[SVname])
                elif SVname in RoadGoodVehicles.keys():
                    print(Vname, RoadGoodVehicles[SVname])
                else:
                    print("!!! Sorry Vehicle coudn't found !!!")

        # Heaire Vehicle
            elif userInput == 6:
                HVehicle = input("Which vehicle you want to heaire? ")
                SHVehicle = HVehicle.lower()
                if SHVehicle in TravellingVehicles.keys():
                    del TravellingVehicles[SHVehicle]
                    print("Vehicle ", HVehicle, " Ready to Heaire for you")
                elif SHVehicle in RoadGoodVehicles.keys():
                    del RoadGoodVehicles[SHVehicle]
                    print("Vehicle ", HVehicle, " Ready to Heaire for you")
                else:
                    print("!!! Vehicle is not avaliable in this time !!!")

            else:
                print("!!! Retry !!!")
        else:
            print("!!! Program Exit !!!")
            break
