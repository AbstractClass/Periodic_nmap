#!/usr/bin/python3
__author__ = "Connor MacLeod"


import nmap
import difflib
import sys
import os


def scan(range="192.168.1-3.*", options="-T4"):
	if os.path.isfile('results.xml'):
		os.rename('results.xml', 'compare.xml')
	
	nm = nmap.PortScanner()
	scan = nm.scan(hosts=range, arguments=options)
	
	with open('results.xml', 'w') as results:
		results.write(nm.get_nmap_last_output()


def find_diffs():
	try:
		with open('compare.xml', 'r') as compare:
			with open('results.xml', 'r') as results:
				diff = difflib.unified_diff(
					compare.readlines(),
					results.readlines(),
					fromfile='compare',
					tofile='results'
				)
				with open('diffs.txt', 'w') as diffs:
					for line in diff:
						diffs.write(line + '\n')
	except Exception as e:
		print("ERROR: ", e)


if __name__ == "__main__":
	ui = ""
	quits = ['q', 'Q', 'quit', 'Quit']

	while ui not in quits:
        	range = input("Enter the range you want to scan (default is 192168.1-3.*): ")
        	options = input("Enter the options you want to apply (default is -T4): ")

        	scan(range, options)
		print("Scan Complete.  Results are in results.xml")
        	find_diffs()

        	ui = input("Differences between scans are stores in diffs.txt, do you want to read it?[y/n]")
        	if ui == 'y':
                	with open('diffs.txt', 'r') as diffs:
                        	temp = diffs.read().splitlines()
                        	for line in temp:
                                	print(line)
                                	print("")

       	 	ui = input("Press 'q' to quit or press Enter to continue...")
