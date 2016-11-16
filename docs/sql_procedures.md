# SQL Procedures

## Entity Set

### `device`
라벨의 대분류에 해당한다.

- `create_device()`

    새로운 디바이스를 하나 생성한다. `id`는 유일한 값으로 자동으로 정해지며, 이름은 'new device'가 기본값이다.

- `change_device_name(id, name)`

    해당 `id`를 가진 디바이스의 이름을 `name`에 전달된 문자열로 바꾼다. 최대 길이는 255바이트이다.

- `delete_device(id)`

    해당 `id`를 가진 디바이스를 삭제한다. 디바이스에 연결되어 있는 라벨과 데이터는 자동으로 삭제된다.


### `label`
데이터를 구분하는 가장 작은 카테고리이다. 그래프와 연동하여 데이터를 불러올 수 있다.

- `create_label(device_id)`

    `device_id`가 `id`인 디바이스를 부모로 갖는 라벨을 하나 생성한다. 이름은 'new label'로 정해진다.

- `change_label_name(id, name)`

    해당 `id`를 가진 라벨의 이름을 변경한다.

- `delete_label(id)`

    해당 `id`를 가진 라벨을 삭제한다. 라벨이 연결된 모든 데이터가 함께 삭제된다.


### `graph`
그래프의 기본 정보가 담긴 테이블이다.

- `create_graph()`

    새 그래프를 만든다. `id`는 유일한 값으로 자동으로 정해지며, 이름의 기본값은 'new graph'이다.

- `change_graph_name(id, name)`

    그래프의 이름을 변경한다.

- `delete_graph(id)`

    그래프를 삭제한다. 그래프와 연결된 데이터가 모두 삭제되나, 디바이스와 라벨, 라벨에 연결된 데이터는 삭제되지 않는다.

- `toggle_graph(id)`

    그래프를 대시보드에 나타나게 할지 여부를 결정한다. 그래프의 `activated`가 1일 경우 대시보드에 나타나며, 실시간으로 20초 내의 데이터가 나타나도록 기본값이 설정되어 있다.

- `change_ordering(id, ordering)`

    활성화된 그래프의 순서를 변경한다. 영향이 있는 그래프들의 순서는 자동으로 갱신된다.

- `set_duration(id, duration)`

    그래프의 값을 가져올 때, 지금으로부터 몇 초 전까지의 데이터를 가져올지를 결정한다. 이 프로시저를 실행하면, 자동으로 `start`와 `finish`는 `NULL`로 변경된다.

- `set_start_and_finish(id, start, finish)`

    그래프가 데이터를 가져올 구간을 결정할 수 있다. `duration`을 `NULL`로 변경한다.


### `data`
디바이스로부터 입력받은 데이터가 순차적으로 쌓이는 테이블이다.

- `insert_data(label_id, value, updated)`

    `label_id`에 해당하는 라벨에 데이터를 추가한다. `value`는 16자리까지 신뢰할 수 있는 실수 데이터이며, `updated`는 최대 10e-6초 정확도까지 나타낼 수 있다.

- `get_data(graph_id)`

    그래프에 연결된 데이터들을 반환한다.


## Relationship Set

### `connects`
라벨과 그래프를 연결하는 테이블이다. 여기에 등록되어 있는 라벨만 그래프에 나타난다.

- `attach_label(graph_id, label_id)`

    그래프와 라벨을 연결한다. 그래프는 자신에게 연결되어 있는 라벨의 데이터에만 접근할 수 있다.

- `detach_label(graph_id, label_id)`

    그래프와 라벨의 연결관계를 삭제한다.
