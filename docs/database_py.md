# Database Package

Realtime Monitor의 pymysql 관련 라이브러리를 쉽게 사용하기 위하여 작성한 패키지이다. `connection.py` 파일과 `load_config.py` 파일로 이루어져 있다.

## `connection.py`

### `Connection`

서버, 계정 정보를 담은 사전형 객체를 기반으로 connection을 생성해 주는 클래스이다.

- `__init__(self, config)`

    `config`는 루트 폴더의 `config.json`을 사전형으로 읽어들인 객체이다.

- `getCursor()`

    생성된 connection에서 커서를 반환해 준다.

- `commit()`

    `insert`, `update`문 등 데이터베이스를 수정하는 쿼리의 경우 Connection에서 반드시 커밋을 해 주어야 변경사항이 제대로 반영된다. `insert/`페이지에서 사용례를 확인할 수 있다.

## `load_config.py`

- `loadConfig(filename)`

    해당 이름을 가진 파일을 불러와서 python dictionary형으로 변환하여 반환하는 함수이다. 여기에서 나온 반환값이 `Connection` 클래스의 `config`에 해당한다.
