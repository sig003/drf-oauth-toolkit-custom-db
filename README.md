# DRF Oauth Toolkit Example   
- Custom User Table  
- Request Create Token
```
curl -X POST -d 'grant_type=password&username=test1@staybility.co.kr&password=1111&client_id=<client_id>&client_secret=<client_secret>' http://<domain>/o/token/ 
```   
- Request Revoke Token 
```
curl --data "token=XXXX&client_id=XXXX&client_secret=XXXX" http://localhost:8000/o/revoke_token/
```
## Reference
https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
