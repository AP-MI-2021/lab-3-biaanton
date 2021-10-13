from typing import List


def menu():
        print('1.Citire date')
        print('2.Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame')
        print('3.Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele se pot scrie ca x**k, k citit, x intreg pozitiv')
        print('4.Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt in progresie aritmetica')
        print('5.Iesire din program')


def citire_lista() -> List[int]:
        lst = []
        lst_str = input('Dati numerele separate prin spatiu: ')
        lst_str_split = lst_str.split(' ')
        for num_str in lst_str_split:
                lst.append(int(num_str))
        return lst


def get_palindrome(nr: int):
        '''
        Determina palindromul unui numar dat
        nr: numarul pe care il verificam daca este palindrom
        returnam valoarea 1 daca numarul este palindrom, respectiv 0 in caz contrar
        '''
        cop=nr
        palindrome=0
        while cop>0:
                palindrome=palindrome*10+cop%10
                cop=cop//10
        if palindrome==nr:
                return 1
        return 0


def get_longest_all_palindromes(lst: List[int]) -> List[int]:
        '''
        Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame
        :param lst: lista in care cautam subsecventa
        :return: returnam subsecventa cautata
        '''
        n=len(lst)
        result=[]
        for left in range(n):
                for right in range(left,n):
                        all_palindromes=True
                        for num in lst[left:right+1]:
                                if get_palindrome(num)==0:
                                        all_palindromes=False
                                        break
                        if all_palindromes:
                                if right-left+1>len(result):
                                        result= lst[left:right+1]
        return result


def test_get_longest_all_palindromes():
        assert get_longest_all_palindromes([1221,14,12321,1221,131])==[12321,1221,131]
        assert get_longest_all_palindromes([14,15,121,17,19])==[121]
        assert get_longest_all_palindromes([11,141,151,13,171,181])==[11,141,151]


def get_power_of_k(nr: int,k: int):
        '''
        Determina daca un numar se poate scrie ca x la puterea k
        :param nr: numarul pe care il verificam
        :return: valoarea 1 daca numarul se poate scrie ca x la puterea k, respectiv 0 in caz contrar
        '''
        if nr==1 and k==0: return 1
        for i in range(2,nr):
                nou=1
                putere=0
                while nou<nr:
                        nou=nou*i
                        putere=putere+1
                if nou==nr and putere==k:
                        return 1
        return 0


def get_longest_powers_of_k(lst: List[int], k:int) -> List[int]:
        '''
        Determina cea mai lunga subsecventa cu proprietatea ca toate numerele se pot scrie ca x la puterea k
        :param lst: lista in care cautam subsecventa
        :param k: cifra dupa care vom selecta subsecventa
        :return: subsecventa cautata
        '''
        n=len(lst)
        result=[]
        for left in range(n):
                for right in range(left,n):
                        all_powers_of_k=True
                        for num in lst[left:right+1]:
                                if get_power_of_k(num,k)==0:
                                        all_powers_of_k=False
                                        break
                        if all_powers_of_k:
                                if right-left+1>len(result):
                                        result=lst[left:right+1]
        return result


def test_get_longest_powers_of_k():
        assert get_longest_powers_of_k([8,9,16,25,3,4,49],2)==[9,16,25]
        assert get_longest_powers_of_k([1,8,27,64,2,27],3)==[8,27,64]


def get_progresie_aritmetica(lst: List[int])->List[int]:
        '''
        Verifica daca elementele din lista sunt in progresie aritmetica
        :param lst: lista din care verificam numerele
        :return: valoarea 1 daca elementele din lista sunt in progresie aritmetica, respectiv 0 in caz contrar
        '''
        n=len(lst)
        for i in range (1,n-1):
                if lst[i]!= (lst[i-1]+lst[i+1])/2: return 0
        return 1


def get_longest_arithmetic_progression(lst: List[int]) -> List[int]:
        '''
        Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt in progresie aritmetica
        :param lst: lista in care cautam subsecventa
        :return: returnam subsecventa dorita
        '''
        n = len(lst)
        lista=[]
        result = []
        for left in range(0,n-2):
                for right in range(left+3, n+1):
                        if get_progresie_aritmetica(lst[left:right])== 1:
                                lista.append(lst[left:right])
        for num in lista:
                if(len(num)>len(result)):
                        result= num
        return result

def test_get_longest_arithmetic_progression():
        assert get_longest_arithmetic_progression([1,2,3,5,9,10,11,12,13])==[9,10,11,12,13]
        assert get_longest_arithmetic_progression([3,2,5,6,7,8,10,11,12])==[5,6,7,8]
        assert get_longest_arithmetic_progression([3,1,2,1,5,7,8,9])==[7,8,9]

def main():
        lst = []
        while True:
                menu()
                opt = input('Optiunea: ')
                if opt == '1':
                        lst=citire_lista()
                elif opt == '2':
                        print(f'Cea mai lunga subsecventa de numere palindroame este: {get_longest_all_palindromes(lst)}.')
                elif opt == '3':
                        putere=int(input('Dati valoarea lui k: '))
                        print(f'Cea mai lunga subsecventa de numere care se pot scrie sub forma x la k este: {get_longest_powers_of_k(lst,putere)}.')
                elif opt== '4':
                        print(f'Cea mai lunga subsecventa cu proprietatea ca toate numerele sunt in progresie aritmetica este: {get_longest_arithmetic_progression(lst)}.')
                elif opt == '5':
                        break
                else: print('Optiune invalida.')


if __name__ == '__main__':
        main()
        test_get_longest_all_palindromes()
        test_get_longest_powers_of_k()
        test_get_longest_arithmetic_progression()


