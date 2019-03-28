#!/bin/bash
PWD="2nmM_F~#^b8-"
INIT="winpty"

$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source dropCruft.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source droptables.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source ced_prod.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source dropCruft.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source subact_tables.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source migrateScript.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD -e "source version2changes.sql"
$INIT mysql -h localhost ced -u sgce --password=$PWD
