def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             D. Display the sum of two binary numbers.
             E. Compress an image.
             U. Uncompress an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    print(MENU)
    
def numtobase( N, B ): #this converst decimal number to another number certain base
    rem = ""
    while N > 0:
        rem1 = N%B
        rem = str(rem1)+rem
        N = N//B
    return rem
    
def basetonum(S, B): #converts number in certain base to decimal (if i remember correctly)
    S = str(S)
    S1 = len(S)
    power = 0
    sum1 = 0
    for i in range(S1-1, -1, -1):
        i = int(S[i])
        sum1 += i*B**power
        power += 1  
    return sum1

def basetobase(B1,B2,s_in_B1): #converts number in given base1 to another number in Base2
    dec_val = basetonum(s_in_B1, B1)
    s_in_B2 = numtobase(dec_val, B2)
    return s_in_B2

def addbinary(S, T): #add binary together and results in the sum as a decimal
    sval = basetonum(S,2)
    tval = basetonum(T,2)
    sum2 = (tval+sval)
    return numtobase(sum2,2)
    
def compress(S): #compresses binary number into something smaller, also in binary
    if S == '':
        final = S
        return final
    
    final = ''
    count = 1
    
    for i in range(1,len(S)):
        if S[i-1] == S[i]:
            count += 1
        elif S[i-1] != S[i]:
             final = final + S[i-1] + numtobase(count, 2).zfill(7)
             count = 1
        if i == len(S)-1:
            final = final + S[i-1] + numtobase(count, 2).zfill(7)
    count = 1
    return final   
            


def uncompress(S): #the opposite of binary.
    S = str(S)
    uncomp = ""
    binline = ""
    s_in_B2 = ""
    color = ""
    count = 1
    ibinline = 0
    
    for i in range(1,len(S)): #checks the whole string
        if i % 8 == 0: #this basically splits the strings into each segment for conversion
            color = S[ibinline] #identify the color
            binline = S[ibinline + 1: ibinline + 8] #find the binary number
            s_in_B2 = basetobase(2, 10, binline) #convert it into decimal
            uncomp = uncomp + (color * int(s_in_B2))
            ibinline = i #resets to find new color at given i
            count = 1
        if i == len(S)-1:
            color = S[ibinline]
            binline = S[ibinline + 1: ibinline + 8]
            s_in_B2 = basetobase(2, 10, binline)
            uncomp = uncomp + (color * int(s_in_B2))
            ibinline = i
            count = 1            
        else:
            count +=1
    return uncomp  



def main():
    BANNER = '''
        .    .        .      .             . .     .        .          .          .
         .                 .                    .                .
  .               A long time ago in a galaxy far, far away...   .
              .   A terrible civil war burns throughout the  .        .     .
                 galaxy: a rag-tag group of freedom fighters   .  .
     .       .  has risen from beneath the dark shadow of the            .
.        .     evil monster the Galactic Empire has become.                  .  .
    .      Outnumbered and outgunned,  the Rebellion burns across the   .    .
.      vast reaches of space and a thousand-thousand worlds, with only     .
    . their great courage - and the mystical power known as the Force -
     flaming a fire of hope. a                                   .

              .------.
            .'::::::' `.
            |: __   __ |
            | <__] [__>|
            `-.  __  .-'
              | |==| |
              | |==| |
           __.`-[..]-`\__
    _.--:``      ||   _``:::--._
   | |  |.      .:'  (o) ::|  | |
   |_|  |::..  // _       :|  |_|
    ===-|:``` // /.\       |-===
   |_| `:___//_|[ ]|_____.' |_| )
    l=l   |\V/_=======_==|   l=l/
  .-l=l   |`'==/=="======|  /|.:
  | l l   |=="======\=_==| `-T l
  `.l_l   |==============|   l_l
    [_]  [__][__]____[_]__]  [_]
    \\\ .'.--.- --   --. .`. |||.
    \\\\| |  |    |    |  || ||||
     \\\\   .'    |    |  |`.||||   
      \\\\  |  LS |    `.   |||||     


    
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~    
                
    '''

    print(BANNER)
    
if __name__ == "__main__": 
    main()
    display_options()

while __name__ == '__main__':
    options = "ABCDEUM"  #setting the list of options that can be used, X not included
    uinput = (input("\n\tEnter option: ")).upper()
    if uinput in options:
        while uinput == "A":
            N = input("\n\tEnter N: ")
            if N.isdigit():
                N = int(N)
                while N < 0:
                    print("\n\tError: {} was not a valid non-negative integer.".format(N))
                    N = int(input("\n\tEnter N: "))
                B = int(input("\n\tEnter Base: "))
                while B < 2 or B > 10:
                    print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                    B = int(input("\n\tEnter Base: "))
                rem = numtobase(N, B)
                print("\n\t {} in base {}: {}".format(N, B, rem))
                break
            if not N.isdigit():
                print("\n\tError: {} was not a valid non-negative integer.".format(N))

        while uinput == "B":
            S = input("\n\tEnter string number S: ")
            if S.isdigit():
                S = int(S)
                while S < 0:
                     print("\n\tError: {} was not a valid non-negative integer.".format(S))
                     S= int(input("\n\tEnter N: "))
                B = int(input("\n\tEnter Base: "))
                while B < 2 or B > 10:
                    print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                    B = int(input("\n\tEnter Base: "))
                sum1 = basetonum(S, B)
                print("\n\t {} in base {}: {}".format(S, B, sum1))
                break
            else:
                S1 = 0
                B = int(input("\n\tEnter Base: "))
                while B < 2 or B > 10:
                    print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                    B = int(input("\n\tEnter Base: "))
                sum1 = basetonum(S1, B)
                print("\n\t {} in base {}: {}".format(S, B, sum1))
                break
        while uinput == 'C':
            B1 = int(input("\n\tEnter base B1: "))
            while B1 < 0:
                print("\n\tError: {} was not a valid non-negative integer.".format(B1))
                B1 = int(input("\n\tEnter base B1: "))
            while B1 < 2 or B1 > 10:
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B1))
                B1 = int(input("\n\tEnter base B1: "))
                
            B2 = int(input("\n\tEnter base B2: "))
            while B2 < 0:
                print("\n\tError: {} was not a valid non-negative integer.".format(B2))
                B1 = int(input("\n\tEnter base B2: "))
            while B2 < 2 or B2 > 10:
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B2))
                B2 = int(input("\n\tEnter base B2: "))

            s_in_B1 = int(input("\n\tEnter string number S: "))
            s_in_B2 = basetobase(B1,B2,s_in_B1)
            print("\n\t {} in base {} is {} in base {}...".format(s_in_B1, B1, s_in_B2, B2))
            break
        while uinput == 'D':
            S = int(input("\n\tEnter the first string number: "))
            T = int(input("\n\tEnter the second string number: "))
            binsum = addbinary(S, T)
            print("\n\tThe sum: " + binsum)    
            break
        while uinput == 'E':
            S = input("\n\tEnter a binary string of an image: ")
            comp = compress(S)
            print("\n\t Original image: {}".format(S))
            print("\n\t Run-length encoded image: {}".format(comp))   
            break
        while uinput == 'U':
            S = input("\n\tEnter a run-length encoded string of an image: ")
            uncomp = uncompress(S)
            print("\n\t Run-length encoded image: {}".format(S))
            print("\n\t Original image: {}".format(uncomp))       
            break
        while uinput == "M":
            display_options()
            break
        
    elif uinput == "X": #X written outside of options list to make the break work in my code
            print('May the force be with you.')
            break
    else: #if not an option, will have user input try again
        print("\n\tError:  unrecognized option [{}]".format(uinput))
        display_options()
