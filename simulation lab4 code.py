def initialize():
def timing():
def arrive():
def depart():
def report():
def update_time_avg_state():


infile = open("file1.txt", "r")
outfile = open("file1.txt", "w")
    
number_events = 2

mean_interarrival , mean_service,number_delays_required = input().trim(',')

print(outfile+"single system Queuing system")
print(outifile+"mean interarrival time=",mean_interarrival)


print(outfile,"Single server queuing system")
print(outfile,"Number of customers",number_delays_required)



initialize();    # its a function initialize before this program

while(num_custs_delayed<number_delays_required):
    timing()
    update_time_avg_state()
    if(next_event_type == 1):
        arrive()
        break
    elif(next_event_type==2):
        depart()
        break


report()

infile.close()
outfile.close()
    
