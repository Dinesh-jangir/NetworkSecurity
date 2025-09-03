# # status = True 

# # if not  status:
# #     print("yes")
# # else:
# #     print("no")



# # replace  = False

# # if replace:
# #     print("true")
# # else:
# #     print('no')

# # import os
# # data = "Dinesh"

# # dir_path = os.path.dirname(data)

# # print(dir_path)



# import os 

# a = "a"

# b= "b" 

# c = "c"


# data = os.path.join(a,b)

# import pandas as pd 

# arr = [[2,2,2],[2,2,1]]

# df = pd.DataFrame(arr)


# # df.to_csv(data)





import logging as lg
import os 

from datetime import datetime 

Jangir = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

djangir = os.path.join(os.getcwd(),"Dinesh",Jangir)

os.makedirs(djangir,exist_ok=True)

LOG_FILE_PATH = os.path.join(djangir,Jangir)

os.makedirs(LOG_FILE_PATH)

lg.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=lg.INFO,

)

if __name__=='__main__':
    try:
        lg.info("Enter the try block")
        a=1/0
        print("This will not be printed")
    except Exception as e:
        print("Not logging") 