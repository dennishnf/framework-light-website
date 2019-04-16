import os
from fnmatch import fnmatch



#Convertion file from Markdown to Html for my website
#By Dennis Nunez


from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

from shutil import copyfile

from time import gmtime, strftime


import re

import argparse




def replace(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close()


def convert(pathh):
    path_in=pathh+'.md'
    path_out=pathh+'.html'

    copyfile(path_in, path_out)

    ##alternative <p> </p>
    replace(path_out, '\n\n0', '\n\n<p align="justify">0')
    replace(path_out, '\n\n1', '\n\n<p align="justify">1')
    replace(path_out, '\n\n2', '\n\n<p align="justify">2')
    replace(path_out, '\n\n3', '\n\n<p align="justify">3')
    replace(path_out, '\n\n4', '\n\n<p align="justify">4')
    replace(path_out, '\n\n5', '\n\n<p align="justify">5')
    replace(path_out, '\n\n6', '\n\n<p align="justify">6')
    replace(path_out, '\n\n7', '\n\n<p align="justify">7')
    replace(path_out, '\n\n8', '\n\n<p align="justify">8')
    replace(path_out, '\n\n9', '\n\n<p align="justify">9')
    replace(path_out, '\n\nA', '\n\n<p align="justify">A')
    replace(path_out, '\n\nB', '\n\n<p align="justify">B')
    replace(path_out, '\n\nC', '\n\n<p align="justify">C')
    replace(path_out, '\n\nD', '\n\n<p align="justify">D')
    replace(path_out, '\n\nE', '\n\n<p align="justify">E')
    replace(path_out, '\n\nF', '\n\n<p align="justify">F')
    replace(path_out, '\n\nG', '\n\n<p align="justify">G')
    replace(path_out, '\n\nH', '\n\n<p align="justify">H')
    replace(path_out, '\n\nI', '\n\n<p align="justify">I')
    replace(path_out, '\n\nJ', '\n\n<p align="justify">J')
    replace(path_out, '\n\nK', '\n\n<p align="justify">K')
    replace(path_out, '\n\nL', '\n\n<p align="justify">L')
    replace(path_out, '\n\nM', '\n\n<p align="justify">M')
    replace(path_out, '\n\nN', '\n\n<p align="justify">N')
    replace(path_out, '\n\nO', '\n\n<p align="justify">O')
    replace(path_out, '\n\nP', '\n\n<p align="justify">P')
    replace(path_out, '\n\nQ', '\n\n<p align="justify">Q')
    replace(path_out, '\n\nR', '\n\n<p align="justify">R')
    replace(path_out, '\n\nS', '\n\n<p align="justify">S')
    replace(path_out, '\n\nT', '\n\n<p align="justify">T')
    replace(path_out, '\n\nU', '\n\n<p align="justify">U')
    replace(path_out, '\n\nV', '\n\n<p align="justify">V')
    replace(path_out, '\n\nW', '\n\n<p align="justify">W')
    replace(path_out, '\n\nX', '\n\n<p align="justify">X')
    replace(path_out, '\n\nY', '\n\n<p align="justify">Y')
    replace(path_out, '\n\nZ', '\n\n<p align="justify">Z')
    replace(path_out, '\n\na', '\n\n<p align="justify">a')
    replace(path_out, '\n\nb', '\n\n<p align="justify">b')
    replace(path_out, '\n\nc', '\n\n<p align="justify">c')
    replace(path_out, '\n\nd', '\n\n<p align="justify">d')
    replace(path_out, '\n\ne', '\n\n<p align="justify">e')
    replace(path_out, '\n\nf', '\n\n<p align="justify">f')
    replace(path_out, '\n\ng', '\n\n<p align="justify">g')
    replace(path_out, '\n\nh', '\n\n<p align="justify">h')
    replace(path_out, '\n\ni', '\n\n<p align="justify">i')
    replace(path_out, '\n\nj', '\n\n<p align="justify">j')
    replace(path_out, '\n\nk', '\n\n<p align="justify">k')
    replace(path_out, '\n\nl', '\n\n<p align="justify">l')
    replace(path_out, '\n\nm', '\n\n<p align="justify">m')
    replace(path_out, '\n\nn', '\n\n<p align="justify">n')
    replace(path_out, '\n\no', '\n\n<p align="justify">o')
    replace(path_out, '\n\np', '\n\n<p align="justify">p')
    replace(path_out, '\n\nq', '\n\n<p align="justify">q')
    replace(path_out, '\n\nr', '\n\n<p align="justify">r')
    replace(path_out, '\n\ns', '\n\n<p align="justify">s')
    replace(path_out, '\n\nt', '\n\n<p align="justify">t')
    replace(path_out, '\n\nu', '\n\n<p align="justify">u')
    replace(path_out, '\n\nv', '\n\n<p align="justify">v')
    replace(path_out, '\n\nw', '\n\n<p align="justify">w')
    replace(path_out, '\n\nx', '\n\n<p align="justify">x')
    replace(path_out, '\n\ny', '\n\n<p align="justify">y')
    replace(path_out, '\n\nz', '\n\n<p align="justify">z')
    replace(path_out, '\n\n-', '\n\n<p align="justify">-')
    replace(path_out, '\n\n,', '\n\n<p align="justify">,')
    replace(path_out, '\.\n\n', '.</p>\n')
    replace(path_out, '\:\n\n', ':</p>\n')

    replace(path_out, '\n#### ', '\n<br/> \n<h4>')
    replace(path_out, ' ####\n', '</h4>\n <br/>\n')
    replace(path_out, '\n### ', '\n<br/> \n<h3>')
    replace(path_out, ' ###\n', '</h3>\n <br/>\n')
    replace(path_out, '\n## ', '\n<h2>')
    replace(path_out, ' ##\n', '</h2>\n <br/>\n')

    #Translate text from markdown to html
    #replace(path_out, '\n\n', '\n<br/>\n')
    #replace(path_out, '\n \n', '\n<br/><br/>\n')

    replace(path_out, '```\n\n```\n', '```\n\n<p><code class="barcode">')
    replace(path_out, '</p>\n```\n', '</p>\n<p><code class="barcode">')
    replace(path_out, '</h2>\n\n```\n', '</h2>\n\n<p><code class="barcode">')
    replace(path_out, '</h3>\n\n```\n', '</h3>\n\n<p><code class="barcode">')
    replace(path_out, '</h4>\n\n```\n', '</h4>\n\n<p><code class="barcode">')
    replace(path_out, '```\n', '</code></p>\n')

    replace(path_out, '<<x>', '&lt;')
    replace(path_out, '<x>>', '&gt;')

    #replace(path_out, '<br/>\n\n', '<br/>\n')
    #replace(path_out, '\n\n<br/>', '\n<br/>')
    #replace(path_out, '<br/>\n<br/>\n', '<br/>\n')
    replace(path_out, ' ```', ' <custom_code>')
    replace(path_out, '```', '</custom_code>')

    #replace(path_out, ' \*\*', ' <strong>')
    #replace(path_out, '\*\*', '</strong>')

    replace(path_out, '\!\[image\]\(', '\n<center><img src=\"https://dennishnf.github.io/framework-light-website')
    replace(path_out, '.png\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, '}!', '\"/></center>\n')
    replace(path_out, '.jpg\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, '}!', '\"/></center>\n')
    replace(path_out, '.jpng\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, '}!', '\"/></center>\n')
    replace(path_out, '.jpeg\){', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\"  width=\"')
    replace(path_out, '}!', '\"/></center>\n')
    replace(path_out, '.png\)', '.png\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, '.jpg\)', '.jpg\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, '.jpng\)', '.jpng\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, '.jpeg\)', '.jpeg\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')
    replace(path_out, '.gif\)', '.gif\" style=\"padding-top:8px; padding-bottom: 8px;\" /></center>\n')

    replace(path_out, '\!{', '\n<center style=\"padding-bottom: 8px; padding-top: 8px;\" ><video width=\"')
    replace(path_out, '}\[video\]\(', '\" controls><source src=\"https://dennishnf.github.io/framework-light-website')
    replace(path_out, '\!\[video\]\(', '\n<center style=\"padding-bottom: 8px; padding-top: 8px;\" ><video controls><source src=\"https://dennishnf.github.io/framework-light-website')
    replace(path_out, '.mp4\)', '.mp4\" type=\"video/mp4\"> Your browser does not support the video tag.</video></center>\n')

    replace(path_out, '\[htt', '<a target=\"_blank\" href=\"htt')
    replace(path_out, '\]\(', '\">')
    replace(path_out, '\)!', '</a>')

    replace(path_out, 'https://dennishnf.github.io/framework-light-website/website/', 'https://dennishnf.github.io/framework-light-website/')

    ##replace(path_out, 'xxxx', 'xxxx')

    with open(path_out, "a") as myfile:
          myfile.write("\n<br/>\n")
          

    ##COPYING PRE

    with open('pre.html', 'r') as myfile:
          data1=myfile.read()

    f = open(path_out,'r+')
    lines = f.readlines() # read old content
    f.seek(0) # go back to the beginning of the file
    f.write(data1) # write new content at the beginning
    for line in lines: # write old content after new
          f.write(line)
    f.close()

    ## COPYING POST

    with open(path_out, 'a') as output, open('post.html', 'r') as input:
          while True:
              data = input.read(100000)
              if data == '':  # end of file reached
                  break
              output.write(data)
    
    










root = '/home/dennis/Desktop/framework-light-website'
pattern = "*.md"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print os.path.splitext(os.path.join(path, name))[0]
            print os.path.join(path)
            convert(os.path.splitext(os.path.join(path, name))[0])
            









