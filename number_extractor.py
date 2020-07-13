class Number_Extractor:
    def number_extractor_list_return(self,path):
        List_of_numbers=[]
        file_point= open(path,'rb')
		with file_point as f:
			for line in f:
				num_lines = num_lines+1

        for i in range(0,num_lines):
            line= file_point.readline()
            line= str(line)
            line= line[2:12]
            List_of_numbers.append(line)
            print(line)
        return List_of_numbers
        
class_obj = Number_Extractor()
class_obj.number_extractor_list_return('numbers.txt')
