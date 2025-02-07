import math

def grams_to_ounces(grams):
    return grams * 28.3495231

def main():
    grams = float(input("Enter the weight in grams: "))
    print(grams_to_ounces(grams))

if __name__ == "__main__":
    main()