import os
from tika import parser 
import re


PAPER_DIRECTORY = 'downloaded_papers'

total = 0
ros_specific = 0

output_file = open("selected_papers.txt", "w")


for paper_name in os.listdir(PAPER_DIRECTORY):
    if paper_name.endswith(".pdf"):
        total = total + 1
        paper_obj = parser.from_file(os.path.join(PAPER_DIRECTORY, paper_name))
        paper_content = paper_obj['content']
        
        # 'Robot Operating System' in searched as case insensitive
        if re.search('Robot Operating System', paper_content, re.IGNORECASE):
            ros_specific = ros_specific + 1
            output_file.write(paper_name.replace('@', '/')[:-4])
            output_file.write('\n')
        # 'ROS' in searched as case sensitive
        elif re.search('ROS', paper_content):
            ros_specific = ros_specific + 1
            output_file.write(paper_name.replace('@', '/')[:-4])
            output_file.write('\n')


output_file.close()
print(f"Total: {total}")
print(f"ROS specific: {ros_specific}")
