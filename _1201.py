def answer(inputs):                                                    
     seen = set()                                                       
     for inp in inputs:                                                 
         if 2020 - inp in seen:                                         
             return inp * (2020 - inp)                                  
         else:                                                          
             seen.add(inp) 

def answer2(inputs):                                                   
     seen = {}                                                          
     for inp in inputs:                                                 
         if 2020 - inp in seen:                                         
             return inp * seen[2020 - inp][0] * seen[2020 - inp][1]     
         else:                                                          
             for inp2 in inputs:                                        
                 seen[inp + inp2] = inp, inp2 
