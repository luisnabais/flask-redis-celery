REDIS_VERSION=4.0.1

docker run -tdi \
--name redis \
-v redis-data:/data \
-p 6379:6379 \
redis:$REDIS_VERSION-alpine \
redis-server --requirepass 'ln_pwd_123'
