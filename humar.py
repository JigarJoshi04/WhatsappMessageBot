

class ReturnListOfNumbers:
    def return_list(self,path):
        List_of_ten_digit_code=[]
        file_pointer= open(path,'rb')
		
		num_lines =0
		with filepointer as f:
			for line in f:
				num_lines = num_lines+1


        for i in range(0, num_lines):
            line = file_pointer.readline()
            line= str(line)
            line= line[2:12]
            List_of_ten_digit_code.append(line)
        return List_of_ten_digit_code

            


vim = ReturnListOfNumbers()
final_list =vim.return_list('ASIN.txt')
print(final_list)
