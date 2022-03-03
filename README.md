# image-classifier-tf

## Image Classification via TensorFlow
### Installation 
To install all neccessary module in order to use project run `pip install requirements.txt` in console, make sure to `cd` to the project's directory. 


### Usage 
This project predicts what is drawn on any submitted image file. 
- Drop any chosen image to the file input of the form
- Submit the form the to see the outcome 
- As the result prediction array will be shown to the user 
- The outcome and the image url will be stored inside db (postgresql)

`Prediction array` shows the most possible outcome of what's drawn on the picture that was submitted, it consists of two parts the item and the possibility of that item.
All the output of the prediction and the image path is being stored on `postgreSQL` DBMS. 

### Example
#### Starter page:
![alt text](https://gm1.ggpht.com/EoUsm6G-449MdP889POMqv42T7fFrvMQuxrDOwHEGRJ7rpr7g1mzrZNjEhBSc3bXByZ1xgVqBdhsy8mBzfEkycfs1MRBhmafErWTsm6WWTF7uxACmyxlZ9s1UjXsnZLk0zSySXE9wqtSD9OVxNpypCxA0naYupX28M9JGQjT0PvVpm9bzK2QcL8T48FS1EwOYg5qVk33bvyCqxegX3BjfLg1Zdi7YDjRIqXwzqCcqQganFDMUcTE-8XuLBukXRwapZNyaQhL3ZQ1rtfSaVxKhh_yg9FLEfTPjHZVo5xJz5ZE1dE50OKk5gZaGaZVzU2zRPD6aZRd5gDDB5TNnW4On7WXNarXKu7gqetKJFWXgMYMRe4YthVkMxpEqnjJ9Q5dPeOtbxQQnkF-BoFwTm7qzXExP2oLHIiWOnK3NSrF0rXwGGQinGfd907GTcJZ9hfKig1FGEuBQAU4hfTz-N_CBR-kmOXB5Ne_FKxMfG6Iucbb8xlLE_jtRDeVZzerFUDjuOWfHfB1r_KxsYIltdSxekWAHIWENnpoGDAxzwvcbmmpXMUF5jbCJMwEu7nlsr3Cqa_qAKuWNc7YhBZByFXfRS7MpIvRrClqFcVuqkDgPvQM27Hso04wuBe7UE64NprNxE2CiYzl8dPhbQheRemBjlQIACvebTZmeL4Cb-dId8nQpf2Zw3ytypRl3gqHOoF1pgxu3k-LSEeUtraR8XDcd7uYLYZLhWI=s0-l75-ft-l75-ft)

#### Execution result:
![alt text](https://gm1.ggpht.com/JqIo3vM7ZwfmGP1mu8Y-4xx9g_MQrV5F_mgzufU7nTfcLGrkBoSVoiS7-vDD1pBop_oxSisydKz2XNebgxm0IAOrwyez9eA7N_1id5EbZ5xC-MX0m3-oWiQEpwvwOrRve5WGT_tAHaJrIOtCQZ3HWH1sndIsIfO1PBr5Jy-pPtvLfF14o6MlZGxkjt6UV8hmOM8svEONWXV0nO9HyEF64tRBm128eMOCWaHe71E-80C9N7W8bxNUSNI2HzgOaV-LqMI68iqDMlxRh0Ux2Ljw_B4P0j_BoZoaW5prUlWmUli5PId2Jg2UIw3a26_kFeD1z5r7spv6QYg2TKN9_SW9MehKsUhoKG2W-ygfJa8hWyF6zUdajJIqEuLfBwNgZEBbr9ahAHvhenGgOjNH2xo1C7UHOWIYlo9SYm8px0MFW6irdU6SVyPhZs-Q616C3a3Wh3iDuZ6x9Qrt9ubA059lSl7LdbTa7fYsjKkNkqgLtnrp1ud_0chidQ16nUbg_F2AczArBHx9T7RfwKquZnc1sp4-Uo3ylYFrjQidEvV-xSw0FUpNnVh7ypBQYiPBBMDrc2RVzsaNZvglxkB0WTsTIm5fsmR71aPAMhr1346UpakMny4zJgHh4u1njMHC6Vohom9-1P1pdpnAWoQdOr99IVOnYi9XxKU7yuoWKIbniFQi-gogvcbnCpd6ITPAQPRmB6b0ogbKKLwG141_XLPzWRaQnlrNv_dawQ=s0-l75-ft-l75-ft)
