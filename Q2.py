def calculate_original_distribution():
    """Calculate the sum distribution for the original dice."""
    distribution = {i: 0 for i in range(2, 13)}
    for i in range(1, 7):
        for j in range(1, 7):
            distribution[i + j] += 1
    return distribution

def find_new_die_b(new_die_a, original_distribution):
    """Find a New_Die_B configuration that matches the original sum distribution."""
    new_die_b = [1] * 6  # Initial guess for New_Die_B
    max_value_b = 20     # Upper limit for values on New_Die_B

    # Function to calculate distribution for current dice configuration
    def current_distribution():
        distribution = {i: 0 for i in range(2, max(new_die_a) + max_value_b + 1)}
        for a in new_die_a:
            for b in new_die_b:
                distribution[a + b] += 1
        return distribution

    # Iteratively adjust New_Die_B
    for index in range(6):
        for value in range(1, max_value_b + 1):
            new_die_b[index] = value  # Set current face value
            if current_distribution() == original_distribution:
                break  # Stop if the distribution matches

    return new_die_b

# Define New_Die_A as per Loki's restrictions
new_die_a = [1, 2, 3, 4, 4, 4]

# Calculate the original distribution
original_distribution = calculate_original_distribution()

# Find a suitable New_Die_B
new_die_b = find_new_die_b(new_die_a, original_distribution)

print("New_Die_A:", new_die_a)
print("New_Die_B:", new_die_b)
