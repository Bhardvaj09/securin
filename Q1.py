def calculate_combinations():
    """Generate all possible combinations of two dice rolls."""
    combinations = []
    for i in range(1, 7):
        for j in range(1, 7):
            combinations.append((i, j))
    return combinations

def calculate_distribution(combinations):
    """Calculate the distribution of sums of dice rolls."""
    distribution = {}
    for i, j in combinations:
        sum_ = i + j
        if sum_ not in distribution:
            distribution[sum_] = 0
        distribution[sum_] += 1
    return distribution

def calculate_probabilities(distribution, total_combinations):
    """Calculate the probabilities of each sum."""
    probabilities = {}
    for sum_, count in distribution.items():
        probabilities[sum_] = count / total_combinations
    return probabilities

def main():
    # Calculate combinations
    combinations = calculate_combinations()
    total_combinations = len(combinations)
    print(f"1. Total combinations: {total_combinations}\n")

    # Calculate and display distribution
    distribution = calculate_distribution(combinations)
    print("2. Distribution of combinations:")
    for sum_, count in distribution.items():
        print(f"Sum = {sum_}: {count} times")
    print("\n")
    # Calculate and display probabilities
    probabilities = calculate_probabilities(distribution, total_combinations)
    print("3. Probability of each sum:")
    for sum_, probability in probabilities.items():
        print(f"P(Sum = {sum_}): {probability:.4f}")
    

if __name__ == "__main__":
    main()
