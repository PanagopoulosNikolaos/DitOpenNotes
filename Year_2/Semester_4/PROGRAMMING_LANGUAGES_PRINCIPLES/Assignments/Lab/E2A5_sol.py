import random
from faker import Faker


def generateFakeData():
    """
    Generates 100 fake profiles with specific age constraints and saves to a file.

    Uses the Faker library with a fixed seed to ensure reproducible results.
    Each profile includes a name, address, and birth date for individuals aged 
    between 18 and 90 years. Results are stored in 'fake100.txt' separated by 
    semicolons.
    """
    # Initializes the Faker generator for generating synthetic identity data.
    fake_generator = Faker()
    
    # Seeds both random and fake_generator to ensure the output remains constant.
    Faker.seed(42)
    random.seed(42)

    # Prepares to store the generated personal data records in a local text file.
    output_filename = "/home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROGRAMMING_LANGUAGES_PRINCIPLES/Exercises/fake100.txt"
    
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for _ in range(100):
            # Generates a random birth date restricted to the specified age range.
            # Ages between 18 and 90 correspond to birth years today - 90 to today - 18.
            birth_date = fake_generator.date_of_birth(minimum_age=18, maximum_age=90)
            
            # Constructs a semicolon-delimited string containing name, address, and date.
            record_row = f"{fake_generator.name()};{fake_generator.address().replace('\n', ', ')};{birth_date}\n"
            
            # Persists the generated row into the target text document.
            output_file.write(record_row)

    # Confirms completion of the data generation process to the console.
    print(f"Successfully generated 100 profiles in {output_filename}")


if __name__ == "__main__":
    try:
        generateFakeData()
    except ImportError:
        # Notifies the user if the required Faker package has not been installed.
        print("Error: The 'faker' library is not installed. Please run 'pip install faker'.")
