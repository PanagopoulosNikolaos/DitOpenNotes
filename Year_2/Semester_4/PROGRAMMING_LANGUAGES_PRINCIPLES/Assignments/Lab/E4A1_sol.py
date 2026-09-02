class Car:
    """
    Represents a vehicle with brand, model, and manufacturing year.

    This class stores basic information about a car and provides a string
    representation for easy display.
    - __init__: Initializes the car's brand, model, and year.
    - __str__: Returns a formatted string with the car's details.
    """

    def __init__(self, brand: str, model: str, year: int, door: int = 4):
        """
        Initializes a Car instance.
        Args:
            brand (str): The brand of the car.
            model (str): The model name.
            year (int): The year of production.
            door (int): The number of doors.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.door = door

    def __str__(self) -> str:
        """
        Provides a string representation of the car.
        Returns:
            str: Formatted string with year, brand, and model.
        """
        return f"{self.year}, {self.brand}, {self.model}"

def runExercise():
    """
    Parses car data, creates instances, and sorts them by year and brand.
    """
    cars_raw_data = """
#year,brand,model,door
1969,Dodge,Charger
1963,Corvette, Stingray
1974,Porsche,914
1969,Chevrolet,Camaro Z28
1967,Toyota,2000GT
1971,Ford,Thunderbird
1991,Dodge,Viper
1966,Lamborghini,Miura
1962,Ferrari,250 GTO
1954,Mercedes,300SL Gullwing"""

    car_objects = []
    # Extracts car attributes from each line of the raw string while ignoring headers.
    for line in cars_raw_data.strip().split("\n"):
        if line.startswith("#") or not line.strip():
            continue
        
        parts = line.split(",")
        year_val = int(parts[0].strip())
        brand_val = parts[1].strip()
        model_val = parts[2].strip()
        door_val = int(parts[3].strip()) if len(parts) > 3 and parts[3].strip() else 4
            
        car_objects.append(Car(brand_val, model_val, year_val, door_val))

    # Sorts the collection to prioritize chronological order, then alphabetical brand names.
    car_objects.sort(key=lambda car: (car.year, car.brand))

    # Iterates through the sorted list to display the finalized order.
    for car in car_objects:
        print(car)

if __name__ == "__main__":
    runExercise()
