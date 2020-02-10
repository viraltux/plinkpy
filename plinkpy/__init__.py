import subprocess
import os
#os.chdir('/home/fran/workspace/plink/plinkpy-pkg/bin')
this_dir, this_filename = os.path.split(__file__)
os.chdir(this_dir+'/../bin')

def plink(args_string):
    #plink("--file toy --freq --out toy_analysis")
    args = ["./plink"] + args_string.split()
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    return(print(output.decode()))
    
