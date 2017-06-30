REDIS_PWD=ln_pwd_123
REDIS_VERSION=3.2.9

docker run -tdi \
--name redis \
-v redis-data:/data \
-p 6379:6379 \
redis:$REDIS_VERSION-alpine \
redis-server --requirepass 'ln_pwd_123'
