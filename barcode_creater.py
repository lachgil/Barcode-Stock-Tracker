import barcode
from barcode.writer import ImageWriter
while True:
	name = raw_input("Input Barcode Label:")
	name = name.rstrip('\n')
	name="reset"
	code39 = barcode.get('code39',name,writer=ImageWriter() )
	save = code39.save(name)

