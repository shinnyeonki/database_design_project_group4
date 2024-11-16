# 데이타베이스 설계 프로젝트
2024-2 데이터베이스 설계 프로젝트

## 개발환경

flask 개발환경입니다
python 3.12 버전 아래의 버전에서는 동작하지 않을 수 있습니다.
vscode 개발환경을 권장합니다.


#### python 패키지 설치
2개의 패키지를 설치해야 합니다.
```bash
pip install flask cx_Oracle;
```

#### 연결 driver 설정
jsp 실습시 사용한 ojdbc.jar 파일과 같이 python에서도 cx_Oracle을 사용하기 위해서는 Oracle Instant Client가 필요합니다.
아래 링크에서 다운로드 받아서 설치해주세요.
Oracle Instant Client 다운로드
[윈도우 버전 링크](https://download.oracle.com/otn_software/nt/instantclient/2360000/instantclient-basic-windows.x64-23.6.0.24.10.zip)
[리눅스 버전 링크](https://download.oracle.com/otn_software/linux/instantclient/2360000/instantclient-basic-linux.x64-23.6.0.24.10.zip)
[osx 버전 링크](https://download.oracle.com/otn_software/mac/instantclient/233023/instantclient-basic-macos.arm64-23.3.0.23.09-1.dmg)

다운로드 받은 파일을 압축을 풀고 
프로젝트 최상위에 넣어주세요
instantclient_23_6 폴더명이 일반적입니다.

#### 






