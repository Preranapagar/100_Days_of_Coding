def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Ans = 0

    try:
        Ans = No1 / No2
    except Exception as zobj:
        print(zobj)

    print("Answer is :", Ans)

if __name__=="__main__":
    main()