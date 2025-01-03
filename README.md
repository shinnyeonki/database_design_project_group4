# 데이타베이스 설계 프로젝트
2024-2 데이터베이스 설계 프로젝트

## 시연
<p align="center">
  <img src="media/시연.gif">
</p>

## git branch 전략
- master : 최종 릴리즈 버전
- dev : 개발 버전

## 개발환경

flask 개발환경입니다
python 3.12 버전 아래의 버전에서는 동작하지 않을 수 있습니다.
vscode 개발환경 기준입니다


#### python 패키지 설치
2개의 패키지를 설치해야 합니다.
```bash
pip install flask cx_Oracle;
```

#### 연결 driver 설정
jsp 실습시 사용한 ojdbc.jar 파일과 같이 python에서도 cx_Oracle을 사용하기 위해서는 Oracle Instant Client가 필요합니다.
아래 링크에서 다운로드 받아서 설치해주세요.
Oracle Instant Client 다운로드 <br>
[윈도우 버전 링크](https://download.oracle.com/otn_software/nt/instantclient/2360000/instantclient-basic-windows.x64-23.6.0.24.10.zip) <br>
[리눅스 버전 링크](https://download.oracle.com/otn_software/linux/instantclient/2360000/instantclient-basic-linux.x64-23.6.0.24.10.zip) <br>
[osx 버전 링크](https://download.oracle.com/otn_software/mac/instantclient/233023/instantclient-basic-macos.arm64-23.3.0.23.09-1.dmg) <br>

다운로드 받은 파일을 압축을 풀고 
프로젝트 최상위에 넣어주세요
일반적으로 instantclient_23_6 폴더명입니다
<p align="center">
  <img src="media/image.png">
</p>

#### app.py 실행
```bash
python app.py 또는 flask run
```

### 할일
- PK id 의 경우 자동으로 증가되도록 설정하도록 database 수정 ???
- 어떤 기능을 개발할 지 명확하게 정하기
- 프로젝트 구조 개선 ??










