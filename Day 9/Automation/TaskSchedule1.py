import datetime
import schedule
import time

def Schedule_Minute():
    print("Scheduler Schedules after minute...")
    print("Current time is :", datetime.datetime.now())

def Schedule_Hour():
    print("Scheduler Schedules after hour...")
    print("Current time is :", datetime.datetime.now())

def Schedule_Sunday():
    print("Scheduler Schedules on Sunday...")
    print("Current time is :", datetime.datetime.now())



def main():
    print("Automations using python")

    schedule.every(1).minutes.do(Schedule_Minute)
    schedule.every().hour.do(Schedule_Hour)
    schedule.every().sunday.do(Schedule_Sunday)


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
