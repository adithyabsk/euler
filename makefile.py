#!/usr/bin/env python

import os, sys, stat

if len(sys.argv) == 2:
    file_name = sys.argv[1].replace(" ", "")
    
    if not os.path.isfile(os.getcwd()+"/"+file_name):
        with open(file_name,"w") as f:
            f.write("#!/usr/bin/env python\n\n")

        st = os.stat(file_name)
        os.chmod(file_name, st.st_mode | stat.S_IEXEC)
        os.system("subl "+file_name)
    else:
    	print "File already exists!"