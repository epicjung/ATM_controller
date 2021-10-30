# ATM_controller


ATM controller (withdraw/deposit/see balance) in Python. 

Assume that there is a database with bank account information as in the directory `./private/database.csv`. A bank account has **name**, **card number**, **expiration month**, **expiration year**, **CVV**, **PIN number**, and **balance** as its attribute. 


## Environment
- Python >= 3
## Installation
- Pandas: 

	```
	$ pip install pandas
	```
## How to use
- **Git clone** 
	```
	$ git clone https://github.com/epicjung/ATM_controller.git
	```

- **Run main.py**

	```
	$ python main.py
	```
	
- **Insert card**

	In reality, the ATM controller will recognize a user's card information if a user inserts his/her card. Instead, this program requires a user to type in his/her card information.
	
	![alt text](https://github.com/epicjung/ATM_controller/blob/main/images/insert_card.PNG?raw=true)

- **Withdraw / Deposit / See Balance**
	
	A user can withdraw/deposit money or see the balance by choosing an option by number. As a user withdraws/deposits money, the database (.csv file) will be updated. 
	
	![alt text](https://github.com/epicjung/ATM_controller/blob/main/images/options.PNG?raw=true)

	
