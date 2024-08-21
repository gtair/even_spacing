def find_all_options(fence_length, exclude_ends=False):
    adjusted_length = fence_length + 2 if exclude_ends else fence_length
    options = []

    for num_objects in range(2, adjusted_length + 1):
        if (adjusted_length - num_objects) % (num_objects - 1) == 0:
            space_between = (adjusted_length - num_objects) // (num_objects - 1)
            actual_num_objects = num_objects - (2 if exclude_ends else 0)

            if actual_num_objects >= 2 and actual_num_objects != fence_length:
                options.append((actual_num_objects, space_between))

    return options

def main():
    fence_length = int(input("Enter the total length (number of blocks): "))
    exclude_ends = input("Do you want objects on the edge? (yes/no): ").strip().lower() == 'no'

    options = find_all_options(fence_length, exclude_ends)

    if options:
        print(f"\nPossible options for placing objects:")
        for i, (num_objects, space_between) in enumerate(options, start=1):
            positions = [1 + j * (space_between + 1) for j in range(num_objects + (2 if exclude_ends else 0))]

            if exclude_ends:
                positions = positions[1:-1]

            print(f"\nOption {i}:")
            print(f"  Number of objects: {num_objects}")
            print(f"  Space between each object: {space_between}")
            print(f"  Positions for each object: {positions}")
    else:
        print("No valid options found for even spacing.")

if __name__ == "__main__":
    main()
