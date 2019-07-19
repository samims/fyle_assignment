echo "=========================Login Response========================="
echo "Starting api calling..."
echo "================================================================"
resp=`curl -sS -X POST http://fyle-sam.herokuapp.com/api-token-auth/  -H 'Content-Type: application/json' -H 'cache-control: no-cache' -d '{"username": "samtest","password": "test@123"}'`
echo "=========================Login Response========================="
echo $resp
token=`echo $resp|python -c "import sys, json; print json.load(sys.stdin)['token']"`
echo "================================================================"

resp=`curl -sS -X GET 'http://fyle-sam.herokuapp.com/banks/?ifsc=ABHY0065003' -H 'Authorization: JWT '$token \-H 'Content-Type: application/x-www-form-urlencoded' -H 'cache-control: no-cache'`

echo "=========================/banks/?ifsc=ABHY0065003========================="
echo $resp
echo "================================================================"

resp=`curl -sS -X GET 'http://fyle-sam.herokuapp.com/banks/branch/?name=State%20Bank%20of%20India&limit=50&offset=100' -H 'Authorization: JWT '$token -H 'cache-control: no-cache'`

echo "=========================/banks/branch/?name=State%20Bank%20of%20India&limit=50&offset=100'========================="
echo $resp
echo "================================================================"
echo "=========================Login Response========================="
echo "Task completed"
echo "================================================================"