!mkdir ~/.kaggle
!touch ~/.kaggle/kaggle.json

api_token = {"username":"username","key":"api-key"}

import json

with open('/root/.kaggle/kaggle.json', 'w') as file:
    json.dump(api_token, file)

!chmod 600 ~/.kaggle/kaggle.json

# use command kaggle datasets download -d raddar/chest-xrays-indiana-university
# Refer to: https://www.kaggle.com/datasets/raddar/chest-xrays-indiana-university/