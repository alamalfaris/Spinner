def counterclockwise(data):   # Buat nama function dan parameter. Input berupa list/matrix 3x3
    temp1 = data[0][0]        # Swap value pertama adalah menukar nilai data[0][0] dgn data[2][0]
    data[0][0] = data[2][0]   # Dengan memuat data[0][0] dlm var temp1, lalu menukar nilai data[0][0] dgn data[2][0]
    data[2][0] = temp1        # Lalu nilai data[2][0] ditukar dengan nilai var temp1
    
    temp2 = data[1][0]        # Swap value kedua adalah menukar nilai data[1][0] dgn data[2][1]
    data[1][0] = data[2][1]   # Dengan memuat data[1][0] dlm var temp2, lalu menukar nilai data[1][0] dgn data[2][1]
    data[2][1] = temp2        # Lalu nilai data[2][0] ditukar dengan nilai var temp2
    
    temp3 = data[0][0]        # Swap value ketiga adalah menukar nilai data[0][0] dgn data[2][2]
    data[0][0] = data[2][2]   # Dengan memuat data[0][0] dlm var temp3, lalu menukar nilai data[0][0] dgn data[2][2]
    data[2][2] = temp3        # Lalu nilai data[2][2] ditukar dengan nilai var temp3
    
    temp4 = data[1][0]        # Swap value keempat adalah menukar nilai data[1][0] dgn data[1][2]
    data[1][0] = data[1][2]   # Dengan memuat data[1][0] dlm var temp4, lalu menukar nilai data[1][0] dgn data[1][2]
    data[1][2] = temp4        # Lalu nilai data[1][2] ditukar dengan nilai var temp4
    
    temp5 = data[0][1]        # Swap value kelima adalah menukar nilai data[0][1] dgn data[1][0]
    data[0][1] = data[1][0]   # Dengan memuat data[0][1] dlm var temp5, lalu menukar nilai data[0][1] dgn data[1][0]
    data[1][0] = temp5        # Lalu nilai data[1][0] ditukar dengan nilai var temp5
    
    temp6 = data[0][0]        # Swap value keenam adalah menukar nilai data[0][0] dgn data[0][2]
    data[0][0] = data[0][2]   # Dengan memuat data[0][0] dlm var temp6, lalu menukar nilai data[0][0] dgn data[0][2]
    data[0][2] = temp6        # Lalu nilai data[0][2] ditukar dengan nilai var temp6
    
    return data               # Lalu mengembalikan nilai dari var data, setelah dilakukannya swap value

data = [[1,2,3],[4,5,6],[7,8,9]]
print(counterclockwise(data))