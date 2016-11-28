drop database if exists idb;

source sql/ddl.sql;
source sql/device.sql;
source sql/label.sql;
source sql/graph.sql;
source sql/data.sql;
source sql/connects.sql;
source sql/load_page.sql;

use idb

call create_device();
call create_device();
call create_label(2);
call create_label(2);
call create_label(2);
call create_label(2);
call create_label(2);
call create_graph();
call create_graph();
call create_graph();
call toggle_graph(2);
call toggle_graph(3);
call attach_label(2, 1);
call attach_label(2, 2);
call attach_label(3, 3);
call attach_label(3, 4);
call attach_label(3, 5);
call set_data_count(2, 20);
call set_data_count(3, 30);
