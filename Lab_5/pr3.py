class UnderageError(Exception):
    pass

def check_voting_eligibility(age):
    if age < 18:
        raise UnderageError(f"Age {age} is invalid. You must be at least 18 to vote.")
    print("Success: You are eligible to vote!")

try:
    print("--- Testing with valid age ---")
    check_voting_eligibility(20)
    
    print("\n--- Testing with invalid age ---")
    check_voting_eligibility(15)

except UnderageError as e:
    print("Caught a Custom Exception:", e)