board= ["-","-","-",
        "-","-","-",
        "-","-","-"]
currentPlayer="X"
winner=None     
sayilar=("1","2","3","4","5","6","7","8","9")

currentPlayer== "X"
while True:
    x=(input(currentPlayer+" "+ "oyuncusu 1 ile 9 arası bir doğal sayı giriniz:"))
    while True:
        if x not in sayilar or (board[int(x)-1]!="-"):
            x=(input(currentPlayer+" "+ "oyuncusu 1 ile 9 arası bir doğal sayı giriniz:"))
        else:
            break
    board[int(x)-1]=currentPlayer
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("------")
    print(board[6]+"|"+board[7]+"|"+board[8])

    if board[0]==board[3]==board[6] and board[0] !="-":
        print("KAZANAN  "+board[0])
        break
        
    elif board[1]==board[4]==board[7] and board[1] !="-":
        print("KAZANAN  "+board[1])
        break
        
    elif board[2]==board[5]==board[8] and board[2] !="-":
        print("KAZANAN  "+board[2])
        break
    elif board[0]==board[1]==board[2] and board[0] !="-":    
        print("KAZANAN  "+board[0])
        break
    elif board[3]==board[4]==board[5] and board[3] !="-":    
        print("KAZANAN  "+board[3])
        break
    elif board[6]==board[7]==board[8] and board[6] !="-":    
        print("KAZANAN  "+board[6])
        break
    elif board[0]==board[4]==board[8] and board[0] !="-":    
        print("KAZANAN  "+board[0])
        break
    elif board[2]==board[4]==board[6] and board[2] !="-":    
       print("KAZANAN  "+board[2])
       break
  
    elif "-" not in board:
        print("Berabere")    
        break
    if currentPlayer =="X":
        currentPlayer ="O"
    else:
        currentPlayer = "X"
   