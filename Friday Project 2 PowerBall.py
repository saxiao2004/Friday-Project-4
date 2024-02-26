import random  # Import the random module

def generate_powerball_numbers():
    # Greeting
    print("Welcome to the PowerBall number generator!")

    # Ask the user if they want PowerBall numbers
    user_input = input("Would you like some PowerBall numbers? (yes/no): ").lower()

    if user_input == "yes":
        # Generate six random numbers for PowerBall
        white_ball_1 = random.randint(1, 69)
        white_ball_2 = random.randint(1, 69)
        white_ball_3 = random.randint(1, 69)
        white_ball_4 = random.randint(1, 69)
        white_ball_5 = random.randint(1, 69)
        red_ball = random.randint(1, 26)

        # Display the generated numbers with proper spacing
        powerball_numbers = f"{white_ball_1}  {white_ball_2}  {white_ball_3}  {white_ball_4}  {white_ball_5}    {red_ball}"
        print(f"Your PowerBall numbers are: {powerball_numbers}")

        # Farewell message
        print("Thank you for stopping by.")

    else:
        # Farewell message if the user declines
        print("Maybe next time.")

if __name__ == "__main__":
    generate_powerball_numbers()
