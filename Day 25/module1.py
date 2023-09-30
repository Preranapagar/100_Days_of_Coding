#display all running processes

import pinfo

def main():

    running_processes = pinfo.ProcessDisplay()

    pinfo.CreateLog(running_processes)

if __name__ == "__main__":
    main()
