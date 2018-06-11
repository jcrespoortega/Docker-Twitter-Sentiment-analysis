./usr/src/app/files/up.sh

cd /usr/src/app/files

python t.py $DONWLOAD_TIME $TWEETER_ACCOUNT1 $TWEETER_ACCOUNT2 $TWEETER_ACCOUNT3 $TWEETER_ACCOUNT4 > z.json

python app.py -r hadoop z.json --file States-Usa.txt --file AFINN-111.txt



 
