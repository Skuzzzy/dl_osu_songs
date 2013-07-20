import os

songfolders = os.listdir("C:\\Program Files (x86)\\osu!\\Songs")

for x in range(0,len(songfolders)):

    current_file = songfolders[x]
    if(" "  in current_file):
        
        #print x
        sp_index = current_file.index(" ")
        #print sp_index
        
        id_part = current_file[0:sp_index]
        name_part = current_file[sp_index:]

        if id_part.isdigit():
            print "http://osu.ppy.sh/d/"+id_part+"\t"+name_part
        else:
            print "Operation not preformed on " + current_file

    else:
        print "Operation not preformed on " + current_file

