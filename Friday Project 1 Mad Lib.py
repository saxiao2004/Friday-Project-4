def mad_libs():
    # Get words from the user
    adjective = input("Enter an adjective: ")  # Ask for an adjective
    large_objects_plural = input("Enter large objects (plural): ")  # Ask for plural large objects
    body_part = input("Enter a body part: ")  # Ask for a body part
    restaurant = input("Enter a restaurant: ")  # Ask for a restaurant name
    first_food = input("Enter a food: ")  # Ask for the name of a food
    second_food = input("Enter another food: ")  # Ask for the name of another food

    # Construct the Mad Lib story
    story = (
        f" I've had a very {adjective} day."
        f" This morning, I dropped a box of {large_objects_plural} on my {body_part}."
        f" Then, at lunch, I went to {restaurant} for their delicious {first_food},"
        f" But the waiter brought me {second_food}, which I was not hungry for."
        f" Finally, on my way home, I was cut off by a van with a large {large_objects_plural[:-1]} strapped to the roof."
    )

    # Display the generated Mad Lib story
    print(story)

if __name__ == "__main__":
    mad_libs()
