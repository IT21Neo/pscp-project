"""BloodDonation"""
def main(age, weight, donate):
    """Demo"""
    if age < 17 or age > 70 or weight < 45 or (donate == 0 and age > 55):
        print("No")
    else:
        if age == 17 or (age >= 60 and age <= 70) and weight >= 45:
            doc_cer = input()
            if doc_cer == "False":
                print("No")
            else:
                print("Yes")
        else:
            print("Yes")
main(int(input()), int(input()), int(input()))
