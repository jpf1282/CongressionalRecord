import sys

def main(*args):
	for count, thing in enumerate(args):
		print '{0}. {1}'.format(count, thing)
	print args
	print args[0]
	print type(args[0])
	print type(args[0][0])

	print 'Testing'

if __name__ == "__main__":
	main(sys.argv)
