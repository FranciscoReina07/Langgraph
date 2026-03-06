import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from chat import run_chat_loop

if __name__ == "__main__":
   run_chat_loop()
   
   
