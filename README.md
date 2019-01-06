# TechForJob-API

## Setting up 

### Installing Related Package 

`TechForJob-API`의 패키지들은 `PyPI`를 통해 관리되고 있다. 따라서 다음 명령을 통해 관련 패키지들을 설치하도록 한다.  

>$ pip install -r requriements.txt

### Migrating DB

`TechForJob-API`최초 기동 시 다음 명령을 통해 DB를 마이그레이션한다.  

>$ tfj_api/manage.py migrate

### Staring Infrastructure

`TechForJob-API`의 웹 서버, 데이터베이스, 캐쉬 서버등은 Docker를 통해 제공되고 있다.  
따라서 `TechForJob-API`를 실행시키기 위해서는 다음 명령을 통해 Docker Image들을 Container화 시켜주면 된다.   

>$ docker-compose up -d

