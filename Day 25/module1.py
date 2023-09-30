#display all running processes

import pinfo

def main():

    running_processes = pinfo.ProcessDisplay()

    for process in running_processes:
        print(process)

if __name__ == "__main__":
    main()
