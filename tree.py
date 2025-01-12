import os

#credit given to https://cyluun.github.io/blog/manipulating-python-oswalk
#however I will try to explain the code itself
#os.walk recursively searches through a directory and brings back the root, dirs, and files
#at each directory, os walk returns a tuple with the current directory's dirs and files
#if we were to print out root, dirs, files while in the for statement, we would get all the hidden files,
#so we only take the values in the tuple that don't start with '.', (ergo not hidden)
#and then at each level of the directory, we add to the txt file the directory, and then the files 


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