# 基于官方PostgreSQL映像创建一个新的映像
FROM postgres

# 在容器中创建一个新的数据库
ENV POSTGRES_DB postgres

# 将SQL文件复制到容器中的docker-entrypoint-initdb.d目录中
COPY init.sql /docker-entrypoint-initdb.d/


# 启动数据库
CMD ["postgres"]