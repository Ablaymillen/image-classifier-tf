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
![alt text](https://gm1.ggpht.com/vft87pWEmFKx26hJPCs9ANZNE8p3zCCU4hiYbTlCcEAZGIovv5K_FhI5JtnD9sYtZYaRt0rNznpFtawlq_CJ9Admyn8fzhejP7W4PvXTEq_ZkxsL_AgaQlbMa2hy21dZg7Ldx-PSV4kh-v5Wp4oPZa5jKp0Y15j_LM8h7hUuuYIlAJMooAogV5J2N4PqHJD-GR3KFYNde0L2pXLaLx-dxlp-KTcew9_uAFi1gfmJ_ycK_Am6dcbxMPxNJ4c7i-5UCLdAeGolwUt-QHbMtYcsnjlAodp5j9fBPpxDPa-icH0YWs2d0pXYCxMkDdlfWth1Ly4yg32GGbOzySQPMohLsJaPgz85IDFMO8fmAEZqCaIxBNJYlM5-KUaCbgaNE8aXZa-5ukgkYg1fJz4ou35mY9p9wb-GXr17psvtO0cBRbViReezGV2kLCxtyeiA9k6JrdaDf2aITs3phgZeir_4GhdPiAKMPgU3GrgS0dXBfHcNqIp97Wl0RnFlMLKVMpzjpPPsSeen3-cp7DcO5D9YmtP9Hjrq4-6kUM06g8ysZCT0DRHEvGXaoOWJPpYlucbhCvwM_WrHwijjnrnj30QbdPywfQZzX8twiYE3x0cupCI4VvsmgKxlNsxKoqUDHt7crIZhK0I4woEImWUyPV0s5N3QKUCSc2-qvjgNfFnMmWjR3iaj7UD2kUuvjAnqBSr-u_K-2GI25hNotfehmkXztpMiFnU6J8Q=s0-l75-ft-l75-ft)

#### Execution result:
![alt text](https://gm1.ggpht.com/JqIo3vM7ZwfmGP1mu8Y-4xx9g_MQrV5F_mgzufU7nTfcLGrkBoSVoiS7-vDD1pBop_oxSisydKz2XNebgxm0IAOrwyez9eA7N_1id5EbZ5xC-MX0m3-oWiQEpwvwOrRve5WGT_tAHaJrIOtCQZ3HWH1sndIsIfO1PBr5Jy-pPtvLfF14o6MlZGxkjt6UV8hmOM8svEONWXV0nO9HyEF64tRBm128eMOCWaHe71E-80C9N7W8bxNUSNI2HzgOaV-LqMI68iqDMlxRh0Ux2Ljw_B4P0j_BoZoaW5prUlWmUli5PId2Jg2UIw3a26_kFeD1z5r7spv6QYg2TKN9_SW9MehKsUhoKG2W-ygfJa8hWyF6zUdajJIqEuLfBwNgZEBbr9ahAHvhenGgOjNH2xo1C7UHOWIYlo9SYm8px0MFW6irdU6SVyPhZs-Q616C3a3Wh3iDuZ6x9Qrt9ubA059lSl7LdbTa7fYsjKkNkqgLtnrp1ud_0chidQ16nUbg_F2AczArBHx9T7RfwKquZnc1sp4-Uo3ylYFrjQidEvV-xSw0FUpNnVh7ypBQYiPBBMDrc2RVzsaNZvglxkB0WTsTIm5fsmR71aPAMhr1346UpakMny4zJgHh4u1njMHC6Vohom9-1P1pdpnAWoQdOr99IVOnYi9XxKU7yuoWKIbniFQi-gogvcbnCpd6ITPAQPRmB6b0ogbKKLwG141_XLPzWRaQnlrNv_dawQ=s0-l75-ft-l75-ft)
