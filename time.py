import time
#input time in seconds


def countdown_timer(seconds):
    while seconds >0:
        mins=int(seconds/60)
        secs=int(seconds%60)

        timer=f'{mins}:{secs}'
        
        print(timer,end='\r')
        time.sleep (1)
        seconds-=1
    print('times up !')


seconds=input("enter the time in number of secondes:")

countdown_timer(int(seconds))
