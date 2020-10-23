#
# © 2020 Nabeel Albishry (nalbishry@kau.edu.sa)
#

class NumberConv(object):

	def __init__(self):
		pass

	def validate(self,user_input, input_base, output_base):
		validation_dict = {
			2:'.01',
			8:'.01234567',
			10:'.0123456789',
			16:'.0123456789abcdef'
		}

		# 1) Check sign
		if str(user_input)[0]=='-':
			user_input = user_input[1:]

		# 2) Validate input base
		if int(input_base) not in validation_dict.keys():
			print('The input base is not permitted. Only 2, 8, 10 and 16 are accepted')
			return False

		# 3) Validate output base
		if int(output_base) not in validation_dict.keys():
			print('The Output base is not permitted. Only 2, 8, 10 and 16 are accepted')

		# 4) Validate input alignment with base
		for i in str(user_input):
			if i not in validation_dict[input_base]:
				print('The input number does not match with the input base you entered')
				return False
        
		return True

	def decimal_to_any(self, user_input, output_base):
		hex_helper_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

		# conver input to string
		user_input = str(user_input)

		# results accomulator
		results = ""

		# check if it real number and split if so
		parts = user_input.split('.')
		integer = int(parts[0])
		remainder = 0

		if len(parts) > 1:
			fractional = float('0.' + parts[1])
		else:
			fractional = 0

		print('\nConverting {} from base {} to base {}'.format(user_input, 10, output_base))
		print('\nIntegral part:', integer)
		print('Fractional part:', fractional)
		print('\n------------- Integral --------------')

		# Integeral part
		i = 0
		while integer >= output_base:

			integer0 = integer

			remainder = integer % output_base
			integer = int(integer / output_base)
			if remainder > 9 and output_base == 16:
				results += str(hex_helper_dict[remainder])
			else:
				results += str(remainder)
			print('index->', i, ', input->', integer0, ', output->', integer, 'remainder->', remainder)
			i += 1
		if integer > 9 and output_base == 16:
			results += str(hex_helper_dict[int(integer)])
		else:
			results += str(integer)

		results = results[::-1]

		# Fractional part
		if fractional > 0:
			results += '.'
			print('\n------------- Fractional --------------')
			for i in range(10):
				fractional0 = round(fractional, 6)
				fractional *= output_base
				fractional = round(fractional, 6)

				if int(fractional) > 9 and output_base == 16:
					results += str(hex_helper_dict[int(fractional)])
				else:
					results += str(int(fractional))

				print('index->', i * -1 - 1, ', input->', fractional0, ', output->', results)
				fractional -= int(fractional)
				if fractional == 0:
					break

		return results

	def any_to_decimal(self, user_input, input_base):

		hex_helper_dict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

		user_input = str(user_input)
		parts = user_input.split('.')
		integer = parts[0]
		# print(integer)
		remainder = 0

		results = 0

		if len(parts) > 1:
			fractional = str(parts[1])
		else:
			fractional = None
		print('\nConverting {} from base {} to base {}'.format(user_input, input_base, 10))
		print('Integral part:', integer)
		print('Fractional part:', fractional)
		print('\n------------- Integral --------------')

		# print('initial frac:',fractional)
		integer = integer[::-1]
		for index, i in enumerate(integer):
			if input_base == 16 and i.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
				i = hex_helper_dict[i.lower()]
				print(i)
			else:
				integer = int(i)

			t = (input_base ** index) * int(i)
			print('index->', index, ', input->', i, ', output->', t)
			results += (input_base ** index) * int(i)
		print('Results for integer:', results)

		if fractional:
			print('\n------------- Fractional --------------')
			results_fr = 0
			for index, i in enumerate(fractional):

				if i == '.':
					continue
				if input_base == 16 and i.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
					i = hex_helper_dict[i.lower()]
				else:
					fractional = int(i)

				t = round((1 / (input_base ** (index + 1))) * int(i), 10)
				print('index->', index * -1 - 1, ', input->', i, ', output->', t)
				results_fr += t
			print('Results for fractional:', results_fr)
			results += results_fr

		return results

class NumberRepresentations(object):

	def __init__(self):
		pass

	def validate(self, user_input, input_base):
		validation_dict = {
			2: '.01',
			8: '.01234567',
			10: '.0123456789',
			16: '.0123456789abcdef'
		}

		# 1) Validate input base
		if int(input_base) not in validation_dict.keys():
			print('The input base is not permitted. Only 2, 8, 10 and 16 are accepted')
			return False

		# 2) Validate input alignment with base
		for i in str(user_input):
			if i not in validation_dict[input_base]:
				print('The input number does not match with the input base you entered')
				return False

		return True

	# def format_number(self,input_number,format,input_base=2):
	# 	formats = ['unsigned','sign_and_mag','twos_comp']
	#
	# 	if self.validate(user_input,input_base):
	# 		if format in formats:
	# 			func = globals().get(format)
	# 			format(user_input)
	#
	# def unsigned(self,input_number):
	# 	pass
	#
	# def sign_and_mag(self,input_number):
	# 	pass

	def twos_comp(self, input_number):
		'''
		Conver a binary bit pattern (e.g. 1010110) to Two's Complement form
		:param input_number: binary bit pattern
		:return: 'xxxxx':string
		'''
		input_number = input_number[::-1]
		flip = False
		twos = ''
		for i in input_number:
			if int(i) == 1 and flip == False:
				flip = True
				twos += '1'
				continue
			if flip:
				twos += str(int(i) ^ 1)
			else:
				twos += str(i)
		return twos[::-1]

	def normalise_binary(self,input_number):
		'''
		Normalise binary number to the form on 1.xxxxx
		Return:
		[0] normalised_number:int
		[1] number of shifts made (-/+)
		'''
		if type(input_number) is not str:
			print('String format only')
			return False

		try:
			integer, fractional = input_number.split('.')
		except:
			integer = input_number
			fractional = ''
		if len(integer) > 1:
			shift = len(integer) - 1

			normalised = integer[0] + '.' + integer[1:] + fractional
			return normalised, shift

		else:
			if int(integer) == 1:
				normalised = input_number
				shift = 0
				return normalised, shift

			else:
				shift = 0
				for l in fractional:
					if int(l) == 0:
						shift += 1
						continue
					elif int(l) == 1:
						shift += 1
						normalised = '1.' + fractional[shift:]
						shift *= -1
						return normalised, shift

	def decimal_to_127(self, input_number):
		nc = NumberConv()


		if str(input_number)[0] == '-':
			s = '1'
			input_number = input_number[1:]
		else:
			s = '0'
		input_number = nc.decimal_to_any(input_number,2)
		a, shift = self.normalise_binary(str(input_number))

		e = shift + 127
		e = nc.decimal_to_any(e, 2)
		m = a.split('.')[1]
		m = m.ljust(23, '0')

		return '{} {} {}'.format(s, e.rjust(8, '0'), m)


class Utilities(object):
	def __init__(self):
		pass

	def main_menue(self):
		functions = {1: 'Convert Number systems (bases:2,8,10,16)',
					 2: 'Unsigned Binary Representation',
					 3: 'Sign & Magnitude Representation',
					 4: "Two's Complement Representation",
					 5: 'Binary Normalisation (1.xxx)',
					 6: 'Floating-point representation (IEEE_127/32-bit)',
					 0: 'Quit'}
		colwidth = 55
		dashes = '-' * colwidth
		print('\n+{}+'.format(dashes))
		print('|{}|'.format('List of functions (choose by number)'.center(colwidth)))
		print('+{}+'.format(dashes))
		print('|{}|'.format(''.ljust(colwidth, ' ')))
		for i, f in functions.items():

			print('| [{}] {}|'.format(i, f.ljust(colwidth - 5, ' ')))
			print('|{}|'.format(''.ljust(colwidth, ' ')))
		#print('| [q] {}|'.format('Quit'.ljust(colwidth - 5, ' ')))
		print('+{}+\n'.format(dashes))

	def add_border(self,string,alignment='l',colwidth=55):
		dashes = '-' * colwidth
		print('\n+{}+'.format(dashes))
		# print('|{}|'.format(''.ljust(colwidth, ' ')))
		if alignment=='l':
			print('|{}|'.format(string.ljust(colwidth, ' ')))
		elif alignment=='c':
			print('|{}|'.format(string.centre(colwidth, ' ')))

		print('+{}+\n'.format(dashes))

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class UI(object):
	def __init__(self):

		self.main_flow()

	def main_flow(self):
		nc = NumberConv()
		utils = Utilities()
		nr = NumberRepresentations()

		EnterMore = True
		output=''
		while EnterMore:
			utils.main_menue()
			function_code = input('Please enter function code from the above menue: ')

			if int(function_code) == 1:
				input_base = int(input('Input Base (2,8,16,10): '))
				output_base = int(input('Output Base (2,8,16,10): '))
				user_input = input('Number to convert: ')

				if nc.validate(user_input, input_base, output_base):
					if input_base == 10:
						output = nc.decimal_to_any(str(user_input), output_base)
					elif output_base == 10:
						output = nc.any_to_decimal(str(user_input), input_base)
					else:
						result = nc.any_to_decimal(user_input, input_base)
						output = nc.decimal_to_any(result, output_base)

			elif int(function_code) == 2:
				input_base = int(input('Input Base (8,16,10): '))
				output_base = 2
				user_input = input('Number to convert: ')

				if nc.validate(user_input, input_base, output_base):
					if input_base == 10:
						output = nc.decimal_to_any(str(user_input), output_base)
					else:
						result = nc.any_to_decimal(user_input, input_base)
						output = nc.decimal_to_any(result, output_base)

			# SING AND MAGNITUDE
			elif int(function_code)==3:
				print('** Accepts only decimal for now **')
				input_base = 10 #int(input('Input Base (8,16,10): '))
				output_base = 2

				#Check sing of the input
				user_input = input('Number to convert: ')

				if user_input[0]=='-':
					user_input=user_input[1:]
					s='1'
				else:
					s='0'

				if nc.validate(user_input, input_base, output_base):
					if input_base == 10:
						output = nc.decimal_to_any(str(user_input), output_base)
					else:
						result = nc.any_to_decimal(user_input, input_base)
						output = nc.decimal_to_any(result, output_base)
				output = s+str(output)

			# TWO'S COMPLEMENT
			elif int(function_code)==4:
				print('** Accepts only Binary for now **')
				input_base = 2
				output_base = 2

				# Check sing of the input
				user_input = input('Number to format (Binary): ')

				if nc.validate(user_input, input_base, output_base):
					output = nr.twos_comp(user_input)

			# BIANRY NORMALISATION
			elif int(function_code)==5:
				input_base=2
				user_input = input('Number to normalise (Binary): ')

				try:
					i,f = user_input.split('.')
					input_to_check = i+f
				except:
					input_to_check = user_input

				if nc.validate(input_to_check, input_base, output_base=2):
					output,shift = nr.normalise_binary(user_input)
					output = '{} x 2^{}'.format(output,shift)


			# Floating-Point IEEE 127
			elif int(function_code)==6:
				print('** Accepts only decimal for now **')
				input_base = 10
				output_base = 2
				user_input = input('Number to format: ')

				if nc.validate(user_input, input_base, output_base):

					#Accept decimal only
					if input_base == 10:
						output = nr.decimal_to_127(user_input)
					else:
						print('Error: Accept only decimal')

			#EXIT
			elif int(function_code)==0:
				print('======== GOOD BYE ======')
				EnterMore = False
				break


			# PRINT FINAL OUTPUT
			utils.add_border('RESULTS|   {}'.format(output))

			# print('| [q] {}|'.format('Quit'.ljust(colwidth - 5, ' ')))
			#print('+{}+\n'.format(dashes))
			#print('Results: ', output)

			repeatq = input('Do you want to continue? y/n: ')
			if repeatq.lower() in ['1','y','yes','yep']:
				EnterMore=True
			else:
				EnterMore=False

			output=None
		return True



if __name__ == '__main__':
	UI()