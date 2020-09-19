#Setup should pull a sql server docker container
#It should create a demo DB
#It should create the tables to be tested
docker_pull_image = "docker pull microsoft/mssql-server-linux"
docker_run_command =  "docker run -d --name sql_server_demo -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=reallyStrongPwd123' -p 1433:1433 microsoft/mssql-server-linux"
sql_server_connection = "mssql -u sa -p reallyStrongPwd123"
create_tables = "CREATE TABLE sales.stores ( \
	store_id INT IDENTITY (1, 1) PRIMARY KEY, \
	store_name VARCHAR (255) NOT NULL, \
	phone VARCHAR (25), \
	email VARCHAR (255), \
	street VARCHAR (255), \
	city VARCHAR (255), \
	state VARCHAR (10), \
	zip_code VARCHAR (5) \
);"