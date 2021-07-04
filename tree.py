import os

a = [1, 2, 3]


def writeToText(directory):
    for root, dirs, files in os.walk(directory):
        files = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        with open('file to write to.txt', 'a') as f:
            for dir in dirs:
                f.write(dir + '\n')

                

            for file in files:
                f.write(os.path.join(root, file) + '\n')
                #print(os.path.join(root, file))

 
    
    #    with open('file to write to.txt', a) as f:
         #   f.write
        





first_dir = '/Users/sean/labs/PyPart8'
writeToText(first_dir)

#if __name__ == '__main__':
#    writeToText2(testDirectory)