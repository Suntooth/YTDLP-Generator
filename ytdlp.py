import subprocess

base = "yt-dlp.exe"

while True:
    url = ' "' + input("URL: ") + '"'
    clip = ""
    subs = ""


    pathChoice = True if input("[S]et path or [D]on't set path? ").lower() == "s" else False
    if pathChoice:
        path = ' -o "' + input("Path (with title format): ") + '"'
    else:
        path = ' -o "Output/%(title)s - %(id)s.%(ext)s"'


    clipChoice = True if input("[C]lip or [F]ull? ").lower() == "c" else False
    if clipChoice:
        start = input("Start: ")
        end = input("End: ")
        clip = ' --download-sections "*' + start + '-' + end + '"'
        
    
    audioChoice = True if input("[A]udio or [V]ideo? ").lower() == "a" else False
    if audioChoice:
        command = base + " -f ba" + path + clip
        

    else:
        subsChoice = True if input("[S]ubs or [N]o subs? ").lower() == "s" else False
        if subsChoice:
             subs = " --write-subs --convert-subs srt"

        command = base + path + clip + subs


    command = command + " " + input("Enter any additional arguments here, or press Enter to continue: ") + url
    
    print("")
    subprocess.run(command)
    print("Done.\n\n")
