# Dates for m day classes
mdays = [20230810, 20230814, 20230816, 20230818, 20230822, 
         20230824, 20230828, 20230830, 20230901, 20230906, 
         20230908, 20230912, 20230914, 20230918, 20230920, 
         20230922, 20230926, 20230929, 20231003, 20231005, 
         20231010, 20231012, 20231016, 20231018, 20231020, 
         20231024, 20231026, 20231030, 20231101, 20231103, 
         20231107, 20231109, 20231114, 20231116, 20231120, 
         20231127, 20231129, 20231201, 20231205, 20231207]

mdayA = [20230810, 20230814, 20230816, 20230818, 20230822, 
         20230824, 20230828, 20230830, 20230901, 20230906]
mdayB = [20230908, 20230912, 20230914, 20230918, 20230920, 
         20230922, 20230926, 20230929, 20231003, 20231005]
mdayC = [20231010, 20231012, 20231016, 20231018, 20231020, 
         20231024, 20231026, 20231030, 20231101, 20231103]
mdayD = [20231107, 20231109, 20231114, 20231116, 20231120, 
         20231127, 20231129, 20231201, 20231205, 20231207]

# Dates for t day classes
tdays = [20230811, 20230815, 20230817, 20230821, 20230823,
         20230825, 20230829, 20230831, 20230905, 20230907,
         20230911, 20230913, 20230915, 20230919, 20230921,
         20230925, 20230928, 20231002, 20231004, 20231006,
         20231011, 20231013, 20231017, 20231019, 20231023,
         20231025, 20231027, 20231031, 20231102, 20231106,
         20231108, 20231113, 20231115, 20231117, 20231121,
         20231128, 20231130, 20231204, 20231206, 20231208]

tdayA = [20230811, 20230815, 20230817, 20230821, 20230823,
         20230825, 20230829, 20230831, 20230905, 20230907]
tdayB = [20230911, 20230913, 20230915, 20230919, 20230921,
         20230925, 20230928, 20231002, 20231004, 20231006]
tdayC = [20231011, 20231013, 20231017, 20231019, 20231023,
         20231025, 20231027, 20231031, 20231102, 20231106]
tdayD = [20231108, 20231113, 20231115, 20231117, 20231121,
         20231128, 20231130, 20231204, 20231206, 20231208]

# class period times zulu [start, end]
periods = [["T133000Z", "T142300Z"],
           ["T143000Z", "T152300Z"],
           ["T153000Z", "T162300Z"],
           ["T163000Z", "T172300Z"],
           ["T184500Z", "T193800Z"],
           ["T194500Z", "T203800Z"],
           ["T204500Z", "T213800Z"],
           ["T133000Z", "T152300Z"],
           ["T153000Z", "T172300Z"],
           ["T194500Z", "T213800Z"]]

# Prompt to generate event for M1 - T40
print("\nWelcome to the Schedule Generator for USAFA Fall Semester of 2023!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Follow all prompts to create 'schedule.ics', a file you can import")
print("into Outlook to populate your calender for the semester.")
print("\nThe first question you will be asked is if you'd like to add 80 events")
print("of Minutes to your calender. (Helpful for C4C's or Training Staff)\n")
print("Generate 80 events for Minutes? (y/n): ", end="")
generateMinutes = input()

print("\nThe next prompt asks if you'd like a reminder of the Academic Day")
print("It will create an all day event that shows as free for M1, T1, etc.")
print("\nGenerate 80 events for M1 - T40? (y/n): ", end="")
generateMTDays = input()

# Create array for class info
print("\nNext we will import your individual academic schedule, the next question")
print("asks the number of classes you'd like to import. Be sure to include your")
print("PE and Lead classes as the program will clarify if the specific class is")
print("a 10 lesson class shortly.")

print("\nNumber of classes: ", end="")
numClasses = int(input())
print()
classes = [[0 for x in range(6)] for y in range(numClasses)]

# Get class info
for i in range(numClasses):
    print("Class " + str(i+1) + " Name: ", end="")
    classes[i][0] = input()
    print("\nPeriods 1 - 7 are the usual periods")
    print("Period 8 = double period during 1&2")
    print("Period 9 = double period during 3&4")
    print("Period 10 = double period during 6&7\n")
    print("Class " + str(i+1) + " Period (1-10): ", end="")
    classes[i][1] = input()
    print("Class " + str(i+1) + " Day (m/t): ", end="")
    classes[i][2] = input()
    print("Add a reminder 15 min before this class? (y/n): ", end="")
    classes[i][3] = input()
    print("Is this a 10 period class? (y/n): ", end="")
    classes[i][4] = input()
    if (classes[i][4] == 'y') | (classes[i][4] == 'Y'):
        print("Type the letter -GO of your 10 period class (A/B/C/D): ", end="")
        classes[i][5] = input()
    else:
        classes[i][5] = 'Z'
    print()

# create ics file
f = open("schedule.ics", "wb")

# ics header
f.write(b"BEGIN:VCALENDAR\n")
f.write(b"VERSION:2.0\n")
f.write(b"CALSCALE:GREGORIAN\n")
f.write(b"METHOD:PUBLISH\n\n")

# Generate events for Minutes
if (generateMinutes == "y") | (generateMinutes == "Y"):
    for i in range(40):
        # mdays
        f.write(b"BEGIN:VEVENT\n")
        f.write(b"SUMMARY:Minutes\n")
        f.write(b"DTSTART:" + str(mdays[i]).encode() + b"T122500Z\n")
        f.write(b"DTEND:" + str(mdays[i]).encode() + b"T124500Z\n")
        f.write(b"END:VEVENT\n\n")
        # tdays
        f.write(b"BEGIN:VEVENT\n")
        f.write(b"SUMMARY:Minutes\n")
        f.write(b"DTSTART:" + str(tdays[i]).encode() + b"T122500Z\n")
        f.write(b"DTEND:" + str(tdays[i]).encode() + b"T124500Z\n")
        f.write(b"END:VEVENT\n\n")

# Generate events for M1 - T40
if (generateMTDays == "y") | (generateMTDays == "Y"):
    for i in range(40):
        # mdays
        f.write(b"BEGIN:VEVENT\n")
        f.write(b"SUMMARY:M" + str(i+1).encode() + b"\n")
        f.write(b"DTSTART:" + str(mdays[i]).encode() + b"\n")
        f.write(b"DTEND:" + str(mdays[i]).encode() + b"\n")
        f.write(b"TRANSP:TRANSPARENT\n")
        f.write(b"X-MICROSOFT-CDO-BUSYSTATUS:FREE\n")
        f.write(b"X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY\n")
        f.write(b"X-MICROSOFT-CDO-ALLDAYEVENT:TRUE\n")
        f.write(b"END:VEVENT\n\n")
        # tdays
        f.write(b"BEGIN:VEVENT\n")
        f.write(b"SUMMARY:T" + str(i+1).encode() + b"\n")
        f.write(b"DTSTART:" + str(tdays[i]).encode() + b"\n")
        f.write(b"DTEND:" + str(tdays[i]).encode() + b"\n")
        f.write(b"TRANSP:TRANSPARENT\n")
        f.write(b"X-MICROSOFT-CDO-BUSYSTATUS:FREE\n")
        f.write(b"X-MICROSOFT-CDO-INTENDEDSTATUS:BUSY\n")
        f.write(b"X-MICROSOFT-CDO-ALLDAYEVENT:TRUE\n")
        f.write(b"END:VEVENT\n\n")

# Generate class events
for i in range(numClasses):
    if (classes[i][4] == 'N') | (classes[i][4] == 'n'):
        for j in range(40):
            f.write(b"BEGIN:VEVENT\n")
            # class name
            f.write(b"SUMMARY:" + str(classes[i][0]).encode() + b"\n")
            # start time
            f.write(b"DTSTART:")
            if (classes[i][2] == "m") | (classes[i][2] == "M"):
                f.write(str(mdays[j]).encode())
            if (classes[i][2] == "t") | (classes[i][2] == "T"):
                f.write(str(tdays[j]).encode())
            f.write(str(periods[int(classes[i][1]) - 1][0]).encode() + b"\n")
            # end time
            f.write(b"DTEND:")
            if (classes[i][2] == "m") | (classes[i][2] == "M"):
                    f.write(str(mdays[j]).encode())
            if (classes[i][2] == "t") | (classes[i][2] == "T"):
                    f.write(str(tdays[j]).encode())
            f.write(str(periods[int(classes[i][1]) - 1][1]).encode() + b"\n")
            # set reminder
            if (classes[i][3] == "y") | (classes[i][3] == "Y"):
                f.write(b"BEGIN:VALARM\n")
                f.write(b"ACTION:DISPLAY\n")
                f.write(b"DESCRIPTION:REMINDER\n")
                f.write(b"TRIGGER:-PT15M\n")
                f.write(b"END:VALARM\n")
            f.write(b"END:VEVENT\n\n")
    else:
        for j in range(10):
            if (classes[i][5] == 'A') | (classes[i][5] == 'a'):
                f.write(b"BEGIN:VEVENT\n")
                # class name
                f.write(b"SUMMARY:" + str(classes[i][0]).encode() + b"\n")
                # start time
                f.write(b"DTSTART:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                    f.write(str(mdayA[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                    f.write(str(tdayA[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][0]).encode() + b"\n")
                # end time
                f.write(b"DTEND:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                        f.write(str(mdayA[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                        f.write(str(tdayA[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][1]).encode() + b"\n")
                # set reminder
                if (classes[i][3] == "y") | (classes[i][3] == "Y"):
                    f.write(b"BEGIN:VALARM\n")
                    f.write(b"ACTION:DISPLAY\n")
                    f.write(b"DESCRIPTION:REMINDER\n")
                    f.write(b"TRIGGER:-PT15M\n")
                    f.write(b"END:VALARM\n")
                f.write(b"END:VEVENT\n\n")
            if (classes[i][5] == 'B') | (classes[i][5] == 'b'):
                f.write(b"BEGIN:VEVENT\n")
                # class name
                f.write(b"SUMMARY:" + str(classes[i][0]).encode() + b"\n")
                # start time
                f.write(b"DTSTART:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                    f.write(str(mdayB[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                    f.write(str(tdayB[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][0]).encode() + b"\n")
                # end time
                f.write(b"DTEND:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                        f.write(str(mdayB[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                        f.write(str(tdayB[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][1]).encode() + b"\n")
                # set reminder
                if (classes[i][3] == "y") | (classes[i][3] == "Y"):
                    f.write(b"BEGIN:VALARM\n")
                    f.write(b"ACTION:DISPLAY\n")
                    f.write(b"DESCRIPTION:REMINDER\n")
                    f.write(b"TRIGGER:-PT15M\n")
                    f.write(b"END:VALARM\n")
                f.write(b"END:VEVENT\n\n")
            if (classes[i][5] == 'C') | (classes[i][5] == 'c'):
                f.write(b"BEGIN:VEVENT\n")
                # class name
                f.write(b"SUMMARY:" + str(classes[i][0]).encode() + b"\n")
                # start time
                f.write(b"DTSTART:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                    f.write(str(mdayC[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                    f.write(str(tdayC[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][0]).encode() + b"\n")
                # end time
                f.write(b"DTEND:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                        f.write(str(mdayC[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                        f.write(str(tdayC[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][1]).encode() + b"\n")
                # set reminder
                if (classes[i][3] == "y") | (classes[i][3] == "Y"):
                    f.write(b"BEGIN:VALARM\n")
                    f.write(b"ACTION:DISPLAY\n")
                    f.write(b"DESCRIPTION:REMINDER\n")
                    f.write(b"TRIGGER:-PT15M\n")
                    f.write(b"END:VALARM\n")
                f.write(b"END:VEVENT\n\n")
            if (classes[i][5] == 'D') | (classes[i][5] == 'd'):
                f.write(b"BEGIN:VEVENT\n")
                # class name
                f.write(b"SUMMARY:" + str(classes[i][0]).encode() + b"\n")
                # start time
                f.write(b"DTSTART:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                    f.write(str(mdayD[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                    f.write(str(tdayD[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][0]).encode() + b"\n")
                # end time
                f.write(b"DTEND:")
                if (classes[i][2] == "m") | (classes[i][2] == "M"):
                        f.write(str(mdayD[j]).encode())
                if (classes[i][2] == "t") | (classes[i][2] == "T"):
                        f.write(str(tdayD[j]).encode())
                f.write(str(periods[int(classes[i][1]) - 1][1]).encode() + b"\n")
                # set reminder
                if (classes[i][3] == "y") | (classes[i][3] == "Y"):
                    f.write(b"BEGIN:VALARM\n")
                    f.write(b"ACTION:DISPLAY\n")
                    f.write(b"DESCRIPTION:REMINDER\n")
                    f.write(b"TRIGGER:-PT15M\n")
                    f.write(b"END:VALARM\n")
                f.write(b"END:VEVENT\n\n")

f.write(b"END:VCALENDAR")

f.close()
print("Congratulations, you've created your 'schedule.ics'!\nHead over to Outlook to import your calender & Have a successful Fall Semester.\n")
print("\nIMPORTANT NOTES - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print(" - If you entered a PE class, there are only 8 classes during the GO you selected.\n   However 10 populated into your calender, ensure you delete the 2 calender events\n   created that do not occur during your PE go.")
print(" - If Minutes events were created, it was on days when academic classes occur.\n   It is your responsibility to ensure these events are up to date and accurate\n   according to the RO & your respective squadron schedule.")
print(" - Have any suggestions or improvements? Message C1C Breeden on Teams!")