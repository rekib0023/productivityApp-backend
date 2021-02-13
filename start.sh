source env/bin/activate
if [ $1 == "-l" ]
then
  killall python
  python run.py
else
  rm nohup.out
  nohup python run.py
fi