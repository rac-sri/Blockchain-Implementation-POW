# Blockchain-Implementation
A simple implementation of Blockchain system.

##### Stack Used
* Flask
* Html
* CSS
* Javascript
* JQuery,Ajax
* pycryptodome library

##### Installation

1. Install dependencies
   ```
   python3 install requirements.txt
   ```
2. Go to blockchain folder (create as many required number of nodes you desire)
 ```
  python3 blockchain.py -p 5001
 ```
3. Create clients, go to blockchain client drectory.(Create as many required clients you require)
 ```
 python3 blockchainclient.py -p 8001
```

##### Demostration

We create 3 nodes instances, and 2 client instances.

1. Client Wallet:
   ![](https://i.imgur.com/KFFA6ZL.png)
2. Node's View :
   ![](https://i.imgur.com/GzFeL4V.png)
3. Create Transaction:
   ![](https://i.imgur.com/n8j9uRe.png)
4. Get Transaction on specified node:
   ![](https://i.imgur.com/5sevlYA.png)
5. Notify each about other nodes:
   ![](https://i.imgur.com/4P524UC.png)
6. Mine and complete the transaction:
   ![](https://i.imgur.com/8j9VqWa.png)