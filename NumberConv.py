#
# © 2020 Nabeel Albishry (nalbishry@kau.edu.sa)
#

class NuumberConv(object):

	def __init__(self):
		pass

	def validate(self,user_input, input_base, output_base):
		validation_dict = {
			2:'.01',
			8:'.01234567',
			10:'.0123456789',
			16:'.0123456789abcdef'
		}

		# 1) Validate input base
		if int(input_base) not in validation_dict.keys():
			print('The input base is not permitted. Only 2, 8, 10 and 16 are accepted')
			return False

		# 2) Validate output base
		if int(output_base) not in validation_dict.keys():
			print('The Output base is not permitted. Only 2, 8, 10 and 16 are accepted')

		# 3) Validate input alignment with base
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

		print('Converting {} from base {} to base {}'.format(user_input, 10, output_base))
		print('Integral part:', integer)
		print('Fractional part:', fractional)
		print(color.RED + '-------Integral-------' + color.END)

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
			print(color.RED + '-------Fractional-------' + color.END)
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
		print('Converting {} from base {} to base {}'.format(user_input, input_base, 10))
		print('Integral part:', integer)
		print('Fractional part:', fractional)
		print(color.RED + '-------Integral-------' + color.END)

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
			print(color.RED + '-------Fractional-------' + color.END)
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

if __name__=='__main__':
    EnterMore = True
    nc = NuumberConv()

    while EnterMore:
        print('============================================')
        input_base = int(input('Input Base (2,8,16,10): '))
        output_base = int(input('Output Base (2,8,16,10): '))
        user_input = input('Number to convert: ')
        
        #output=None
        if nc.validate(user_input,input_base,output_base):
            if input_base==10:
                output = nc.decimal_to_any(str(user_input), output_base)
            else:
                output = nc.any_to_decimal(str(user_input), input_base)

            print('The output: ',output)
            print('============================================')
            repeatq = input('Do you want to continue?')
            if repeatq.lower() in ['1','y','yes','yep']:
                EnterMore=True
            else:
                EnterMore=False