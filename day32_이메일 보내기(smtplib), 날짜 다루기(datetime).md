
### [[SMTP]]
Simple Mail Transefer Protocol
이메일을 메일 서버가 어떻게 받고, 인터넷을 통해 다음 메일 서버로 어떻게 전달하는 지를 결정하는 규칙이 담겨있음

sender -> (Gmail Mail Server) -> (Yahoo Mail Server) -> Timmy's Computer

smtplib
```
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="storm6781@naver.com",
        msg="Subject:Hello\n\nThis is the body of my email"
        )
```

### [[datetime]]
```
import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)
print(type(year))
if year == 2023:
    print("Wear a face mask") 

day_of_week = now.weekday()
print(day_of_week)
```
![[Pasted image 20231120170837.png]]

```
date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)
```
![[Pasted image 20231120171202.png]]

