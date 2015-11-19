###########################################################################
# Number 2
# Usage: (python) group2_report1_question2.py <BitTorrent Sync folder>
###########################################################################

import sys
import re
import os

path = sys.argv[1]

channel_dict = {}

def get_channels(s):
	file_list = os.listdir(s)
	for f in file_list:
		channel = re.search('ch(\d+)_file', f)
		if channel:
			if channel.group(1) in channel_dict.keys():
				channel_dict[channel.group(1)] += 1
			else:		
				channel_dict[channel.group(1)] = 1
	return channel_dict

# For pass
channel_list = get_channels(''+path+'downloads/pass/')

# For fail
channel_list = get_channels(''+path+'downloads/fail/')

# Average
total = 0
for i in channel_list:
	total = total + channel_list[i]
avr = float(total)/len(channel_list)

file = open(‘Q2channeloutput.txt', 'w')

file.write('Average reads per channel: ' + str(avr) + '\nPore with most reads: ' + str(max(channel_list, key=channel_list.get)) + '\nNumber of reads: ' + str(channel_list[max(channel_list, key=channel_list.get)]))

file.close()



	
		





