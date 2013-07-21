import os

songfolders = os.listdir("C:\\Program Files (x86)\\osu!\\Songs")

f = open('Song_Download_Links.txt', 'w+')
for x in range(0,len(songfolders)):

    current_file = songfolders[x]
    if(" "  in current_file):
        sp_index = current_file.index(" ")
        if(len(str(sp_index))<6):
                remain = 6-len(str(sp_index))
                
        
        id_part = current_file[0:sp_index]
        name_part = current_file[sp_index:]

        if id_part.isdigit:
            f = open('Song_Download_Links.txt', 'a')
            f.write("http://osu.ppy.sh/d/"+id_part+(" "*remain)+"\t"+name_part+"\n")
            print "http://osu.ppy.sh/d/"+id_part+"\t"+name_part
