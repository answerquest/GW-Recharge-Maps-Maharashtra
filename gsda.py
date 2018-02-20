import json

def filewriter( content, filename ):
	f = open(filename, 'w', newline='\r\n', encoding='utf8') # newline parameter can be \r\n for windows CRLF. From https://stackoverflow.com/a/2642121/4355695
	f.write( content )
	f.close()
	print( 'Created', filename )


villagejson = json.load(open('villages.json'))
# Sample link to construct: https://gsda.maharashtra.gov.in/english/maps/Amravati/Akola/Akola/Agar.pdf

i = 0;
for region in villagejson:
	for district in villagejson[region]:
		outputfile = '' # Initiating district-wise URLs list

		for taluka in villagejson[region][district]:
			for village in villagejson[region][district][taluka]:
				
				pdfpath = 'https://gsda.maharashtra.gov.in/english/maps/' + region + '/' + district + '/' + taluka + '/' + villagejson[region][district][taluka][village]
				pdflocalpath = ( district.title() + '/' + taluka.title() + '/' + villagejson[region][district][taluka][village].title() ).replace(' ','_')
				outputfile += pdfpath + '\n out=' + pdflocalpath +'\n'
			
				# end of village loop
			# end of taluka loop
		# end of district loop
		filewriter(outputfile, district.replace(' ','_').title() + '-pdfs.txt')
	# end of region loop

print('Run this command to download: aria2c -x10 -j10 -k1M -c -i <district>-pdfs.txt')

